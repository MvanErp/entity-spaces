
# coding: utf-8

# In[50]:


# This script take the output of the disambiguation page linker
# It then checks whether the gold standard link is present in the
# suggested disambiguation page
# It writes a new file, where the gold standard link is filled into the
# prediction slot if present
# (to be able to evaluate using the conll script, which breaks if there are too many columns in a line)

# Load disambiguation information from DBpedia and store into a dict
disamb = {}
with open('../disambiguations_en.ttl', 'r') as d:
    for line in d:
        elems = line.split(" ")
        elems[0] = elems[0][0:-1].replace('<http://dbpedia.org/resource/', '')
        elems[2] = elems[2][0:-1].replace('<http://dbpedia.org/resource/', '')
        if elems[0] not in disamb:
            disamb[elems[0]] = {}
            disamb[elems[0]][elems[2]] = 1
        else:
            disamb[elems[0]][elems[2]] = 1

with open('../wikidisambiguationpages_complete.tsv', 'r') as w:
    for line in w:
        elems = line.split("\t")
        if elems[0] not in disamb:
            disamb[elems[0]] = {}
            disamb[elems[0]][elems[1].rstrip()] = 1
        else:
            disamb[elems[0]][elems[1].rstrip()] = 1


# In[42]:


# Shouldn't be necessary anymore as it's solved in the earlier conversion, but let's not throw it away just yet

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_escaped_unicode(str):
    #how do I determine if this is escaped unicode?
    if is_ascii(str): # escaped unicode is ascii
        return True
    return False

#if is_escaped_unicode(str):
#        str = str.decode("unicode-escape")


# In[46]:


import sys

inputfile = sys.argv[1]
outputfile = inputfile[0:-4]+"sourc.txt"
output = open(outputfile, "w")

with open(inputfile, 'r') as f:
#with open('/Users/marieke/Work/entityspaces/data/expresults/aida_b_neural_ner_disambig_full.txt', 'r') as f:
    for line in f:
        elems = line.split(" ")
        if len(elems) > 1 and is_escaped_unicode(elems[1]):
            elems[1] = elems[1].encode().decode("unicode-escape")
        if len(elems) > 2 and 'disambiguation' in elems[2]:
            #print(elems[1],elems[2][2:].rstrip())
            if elems[2][2:].rstrip() in disamb:
                if elems[1][2:] in disamb[elems[2][2:].rstrip()]:
                    elems[2] = elems[2][0:2] + elems[1][2:]
        if len(elems) > 2:
           # print(elems[0], elems[1], elems[2].rstrip())
            output.write(elems[0] + " " + elems[1] + " " + elems[2].rstrip() + "\n")
        else:
           # print(line.rstrip())
            output.write(line)

output.close()



# In[49]:


# Fix unicode stuff in original matches
#output = open("/Users/marieke/Work/entityspaces/data/expresults/aida_b_neural_ner_disambig_full_fixunicode.txt", "w")

#with open('/Users/marieke/Work/entityspaces/data/expresults/aida_b_neural_ner_disambig_full.txt', 'r') as f:
#    for line in f:
#        if is_escaped_unicode(line):
#            line = line.encode().decode("unicode-escape")
#        output.write(line)
