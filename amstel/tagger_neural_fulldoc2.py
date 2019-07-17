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

NEURAL_EL_SERVER = "http://localhost:5555"



def process_conll_doc(input_file_name, output_file_name):

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

            myjson = {"text":unidecode.unidecode(d.to_tokenized_string()), "spans":[]}
            res = requests.post(NEURAL_EL_SERVER, json=myjson)
            info = res.json()
            #print(info)
            for i in info:
                entity_ran = range(i[0], i[0]+i[1])
                #print(i[2] + " " + str(entity_ran))
                for t in d.tokens:
                    #print(t.text + " " + str(t.start_pos))
                    if t.start_position in entity_ran:
                        #print("found tag")
                        t.add_tag("pnme", i[2])

            for t in d:
                output_file.write(t.text + "\t" + t.get_tag("nero").value + "\t" + t.get_tag("nme").value + "\t" + unidecode.unidecode(t.get_tag("wiki").value) + "\t" + t.get_tag("pnme").value + "\n")


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    process_conll_doc(input_file_name, output_file_name)
