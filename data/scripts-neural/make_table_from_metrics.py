from tabulate import tabulate
import sys

#accuracy:  97.53%; precision:  85.83%; recall:  80.54%; FB1:  83.10

def process(filename, type):
    try:
        with open(filename) as f:
            for _ in range(2):
                line = f.readline()
                if "accuracy" in line:
                    s = line.split(";")
                    if type == "precision":
                        return s[1].split(":")[1].replace("%", "").strip() + " P"
                    if type == "recall":
                        return  s[2].split(":")[1].replace("%", "").strip() + " R"
                    if type == "F1":
                        return s[3].split(":")[1].strip() + " F"
    except FileNotFoundError:
        print("No file: " + filename)
        return " "



if __name__ == "__main__":
    results = {}
    cset = set([])
    mset = set([])
    for file_name in sys.argv[1:]:
        cname = file_name.split("neural")[0]
        cset.add(cname)
        mset.add(file_name[len(cname):].split(".")[0])

    corpora = list(cset)
    corpora = sorted(corpora, key=str.lower)

    #models = list(mset)
    #models = sorted(models, key=len)
    models = ["neural", "neural_flair_ner_fast", "neural_flair_ner_fast_disambig_10", "neural_flair_ner_fast_disambig_08",
    "neural_flair_ner_fastadistis", "neural_flair_ner_fast_disambig_10adistis",
    "neural_flair_ner_fast_disambig_08adistis"]

    #print(corpora)
    #print(models)
    table = []
    for c in corpora:
        prec = [c]
        for m in models:
            r = process(c + m + ".metrics", "precision")
            prec.append(r)
        table.append(prec)

        recall = [""]
        for m in models:
            b = process(c + m + ".metrics", "recall")
            recall.append(b)
        table.append(recall)

        fmeasure = [""]
        for m in models:
            fmeas = process(c + m + ".metrics", "F1")
            fmeasure.append(fmeas)
        table.append(fmeasure)

    headers = [" "] + models

    print(tabulate(table, headers=headers, tablefmt="latex"))
