import json
import sys
import string
import unidecode


from torch import Tensor
from torch.nn import CosineSimilarity
from flair.models import SequenceTagger
from flair.data import Sentence, Token
import requests

from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.measure.jaccard import JaccardMeasure
from simstring.feature_extractor.word_ngram import WordNgramFeatureExtractor
from simstring.measure.cosine import CosineMeasure
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher

from flair.data_fetcher import NLPTaskDataFetcher

LOCATION_WIKIPEDIA_DISAMBIGUATION = "../wikidisambiguationpages.txt"
NEURAL_EL_SERVER = "http://localhost:5555"

def load_disambiguation():
    db = DictDatabase(WordNgramFeatureExtractor(2))

    with open(LOCATION_WIKIPEDIA_DISAMBIGUATION) as disambig_file:
        for line in disambig_file:
            r = line.replace("_(disambiguation)","").replace("_"," ").lower()
            db.add(r.strip())

    return Searcher(db, JaccardMeasure())


def process_conll_doc(input_file_name, output_file_name, ner_model, with_disambiguation, sim_level_disambig):

    nertagger = SequenceTagger.load(ner_model)
    columns = {0: 'text', 1: 'nero', 2: 'nme', 3: 'wiki',}
    with open(input_file_name, "r") as input_file, open(output_file_name, "w+") as output_file:
        doc = None
        docs = []
        spos = 0

        for line in input_file:
            if "DOCSTART" in line:
                if doc == None:
                    doc = Sentence()
                else:
                    docs.append(doc)
                    doc = Sentence()
                    spos = 0
            else:
                lsplit = line.split("\t")
                #print(lsplit)
                token = Token(lsplit[0].strip())
                for c in columns:
                    if c != 0:
                        if c < len(lsplit):
                            token.add_tag(columns[c], lsplit[c].strip())
                token.start_pos = spos
                token.end_pos = spos + len(token.text)
                spos = token.end_pos + 1
                doc.add_token(token)


        for d in docs:
            nertagger.predict(d)

            spans = []
            for nerspan in d.get_spans('ner'):
                start = nerspan.start_pos
                length = nerspan.end_pos - nerspan.start_pos
                spans.append({"start":start,"length":length})

            myjson = {"text":unidecode.unidecode(d.to_tokenized_string()), "spans":spans}

            res = requests.post(NEURAL_EL_SERVER, json=myjson)
            info = res.json()

            for nerspan in d.get_spans('ner'):
                for i in info:
                    if i[0] == nerspan.start_pos:
                        for t in nerspan.tokens:
                            t.add_tag("pnme", i[2])
                        break

            if with_disambiguation:
                searcher = load_disambiguation()
                for nerspan in d.get_spans('ner'):
                    if "pnme" not in nerspan.tokens[0].tags:
                        #print("calling with " + nerspan.text)
                        r = searcher.search(nerspan.text.lower(), sim_level_disambig)
                        #print(r)
                        if len(r) > 0:
                            d_tag = unidecode.unidecode((string.capwords(r[0]) + "_(disambiguation)").replace(" ","_"))
                            for t2 in nerspan.tokens:
                                t2.add_tag("pnme", d_tag)

            for t in d:
                output_file.write(t.text + "\t" + t.get_tag("nero").value + "\t" + t.get_tag("nme").value + "\t" + unidecode.unidecode(t.get_tag("wiki").value) + "\t" + t.get_tag("pnme").value + "\n")


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    ner_model = sys.argv[3]
    with_disambiguation = json.loads(sys.argv[4])
    sim_level_disambig = float(sys.argv[5])
    process_conll_doc(input_file_name, output_file_name, ner_model, with_disambiguation, sim_level_disambig)
