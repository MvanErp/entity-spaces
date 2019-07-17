#!/bin/bash

INPUT_FILE="../evaluation_datasets/ace2004_yago.tsv"

AMSTEL_DIR="../../amstel"
CONLL_CONV_DIR="../../conll_conversion"

#EL
python3 $AMSTEL_DIR/tagger_neural_fulldoc2.py $INPUT_FILE ace2004_yago_neural.tsv

python3 $CONLL_CONV_DIR/convertSysOutput2CoNLLEvalInput.py ace2004_yago_neural.tsv
#
python3 $CONLL_CONV_DIR/conlleval.py ace2004_yago_neural.txt > ace2004_yago_neural.metrics

#No Disambiguation
#  python3 $AMSTEL_DIR/tagger_neural_fulldoc_disambig.py $INPUT_FILE ace2004_yago_neural_flair_ner_fast.tsv ner-fast false 1.0
# #
#  python3 $CONLL_CONV_DIR/convertSysOutput2CoNLLEvalInput.py ace2004_yago_neural_flair_ner_fast.tsv
# #
#  python3 $CONLL_CONV_DIR/conlleval.py ace2004_yago_neural_flair_ner_fast.txt > ace2004_yago_neural_flair_ner_fast.metrics
#
# # #Disambiguation 1.0
# python3 $AMSTEL_DIR/tagger_neural_fulldoc_disambig.py $INPUT_FILE ace2004_yago_neural_flair_ner_fast_disambig_10.tsv ner-fast true 1.0
#
# python3 $CONLL_CONV_DIR/convertSysOutput2CoNLLEvalInput.py ace2004_yago_neural_flair_ner_fast_disambig_10.tsv
#
# python3 $CONLL_CONV_DIR/DisambiguationMatches.py ace2004_yago_neural_flair_ner_fast_disambig_10.txt
#
# python3 $CONLL_CONV_DIR/conlleval.py ace2004_yago_neural_flair_ner_fast_disambig_10sourc.txt > ace2004_yago_neural_flair_ner_fast_disambig_10.metrics
#
# # #Disambiguation 0.8
# python3 $AMSTEL_DIR/tagger_neural_fulldoc_disambig.py $INPUT_FILE ace2004_yago_neural_flair_ner_fast_disambig_08.tsv ner-fast true 0.8
#
# python3 $CONLL_CONV_DIR/convertSysOutput2CoNLLEvalInput.py ace2004_yago_neural_flair_ner_fast_disambig_08.tsv
#
# python3 $CONLL_CONV_DIR/DisambiguationMatches.py ace2004_yago_neural_flair_ner_fast_disambig_08.txt
#
# python3 $CONLL_CONV_DIR/conlleval.py ace2004_yago_neural_flair_ner_fast_disambig_08sourc.txt > ace2004_yago_neural_flair_ner_fast_disambig_08.metrics
