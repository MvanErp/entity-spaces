import sys

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_escaped_unicode(str):
    #how do I determine if this is escaped unicode?
    if is_ascii(str): # escaped unicode is ascii
        return True
    return False

inputfile = sys.argv[1]
#outputfile = "../evaluate_withNMEs_e2e/" + inputfile[0:-2]+"xt"
outputfile = "../evaluate_withNMEs_agdistis/" + inputfile[0:-2]+"xt"

output = open(outputfile, "w")

previous = ""
#with open("/Users/marieke/Work/entityspaces/data/expresults/aida_b_mag.tsv", "r") as f:
with open(inputfile, "r") as f:
    for line in f:
        #print(line)
        if "https://www.github.com/nvidia/apex" in line:
                continue
        line = line.replace("http://en.wikipedia.org/wiki/", "")
        line = line.replace("http://dbpedia.org/resource/", "")
        line = line.replace("http://aksw.org/notInWiki/","")
        if "DOCSTART" in line:
            line = "DOCSTART\tO\tO"
        elems = line.split("\t")
        if len(elems[3]) == 0:
            elems[3] = "O"
        if not elems[0].strip():
            continue
        if len(elems) > 1 and len(elems[1]) < 1:
            del(elems[1:])
        if len(elems) > 1 and elems[2] == "--NME--":
            elems[3] = "--NME--"
        if len(elems) > 2: #and elems[2] != "--NME--":
            if is_escaped_unicode(elems[3]):
                elems[2] = elems[3].encode().decode("unicode-escape")
            elems[3] = elems[3].replace("http://en.wikipedia.org/wiki/", "")
            elems[3] = elems[1] + "-" + elems[3]
    #    if len(elems) > 2: # and "http://en.wikipedia.org/wiki" in elems[2]:
    #        elems[2] = elems[2].replace("--NME--", "O")
        if len(elems) > 4 and len(elems[4]) > 1:
            if previous != elems[4]:
        #        print(elems[0] + " " + elems[2] + " B-" + elems[4].rstrip())
                output.write(elems[0] + " " + elems[3] + " B-" + elems[4].rstrip() + "\n")
                previous = elems[4]
            else:
         #       print(elems[0] + " " + elems[2] + " I-" + elems[4].rstrip())
                output.write(elems[0] + " " + elems[3] + " I-" + elems[4].rstrip() + "\n")
        elif len(elems) > 2:
         #   print(elems[0] + " " + elems[2].rstrip() + " O")
            output.write(elems[0] + " " + elems[3].rstrip() + " O\n")
        elif len(elems) == 1 and len(line.rstrip()) > 0:
            #print(elems[0].rstrip(), "O O", file=open("/Users/marieke/Work/entityspaces/data/expresults/aida_b_mag.txt", "a"))
         #   print(elems[0].rstrip(), "O O")
            output.write(elems[0].rstrip() +" O O\n")
            previous = ""
        elif len(elems) == 2:
            #print(elems[0], elems[1].rstrip(), "O", file=open("/Users/marieke/Work/entityspaces/data/expresults/aida_b_mag.txt", "a"))
          #  print(elems[0], elems[1].rstrip(), "O")
            output.write(elems[0] + " " + elems[1].rstrip() + " O\n")
        else:
            #print(line.rstrip().replace("\t"," "), file=open("/Users/marieke/Work/entityspaces/data/expresults/aida_b_mag.txt", "a"))
           # print(line.rstrip().replace("\t"," "))
            output.write(line.rstrip().replace("\t"," ") + "\n")

output.close()
