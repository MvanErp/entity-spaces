#!/bin/bash

INPUT_FILE="../evaluation_datasets/ACE2004_first20_CoNLL.tsv"

AMSTEL_DIR="../../amstel"
CONLL_CONV_DIR="../../conll_conversion"

#EL
python3 $AMSTEL_DIR/tagger_neural_fulldoc2.py $INPUT_FILE ACE2004_first20_CoNLL_neural.tsv

 python3 $CONLL_CONV_DIR/convertSysOutput2CoNLLEvalInput.py ACE2004_first20_CoNLL_neural.tsv
#
 python3 $CONLL_CONV_DIR/conlleval.py ACE2004_first20_CoNLL_neural.txt > ACE2004_first20_CoNLL_neural.metrics

##No Disambiguation
#  python3 $AMSTEL_DIR/tagger_neural_fulldoc_disambig.py $INPUT_FILE ACE2004_first20_CoNLL_neural_flair_ner_fast.tsv ner-fast false 1.0
# #
#  python3 $CONLL_CONV_DIR/convertSysOutput2CoNLLEvalInput.py ACE2004_first20_CoNLL_neural_flair_ner_fast.tsv
# #
#  python3 $CONLL_CONV_DIR/conlleval.py ACE2004_first20_CoNLL_neural_flair_ner_fast.txt > ACE2004_first20_CoNLL_neural_flair_ner_fast.metrics
#
# # #Disambiguation 1.0
# python3 $AMSTEL_DIR/tagger_neural_fulldoc_disambig.py $INPUT_FILE ACE2004_first20_CoNLL_neural_flair_ner_fast_disambig_10.tsv ner-fast true 1.0
#
# python3 $CONLL_CONV_DIR/convertSysOutput2CoNLLEvalInput.py ACE2004_first20_CoNLL_neural_flair_ner_fast_disambig_10.tsv
#
# python3 $CONLL_CONV_DIR/DisambiguationMatches.py ACE2004_first20_CoNLL_neural_flair_ner_fast_disambig_10.txt
#
# python3 $CONLL_CONV_DIR/conlleval.py ACE2004_first20_CoNLL_neural_flair_ner_fast_disambig_10sourc.txt > ACE2004_first20_CoNLL_neural_flair_ner_fast_disambig_10.metrics
#
#
# # #Disambiguation 0.8
# python3 $AMSTEL_DIR/tagger_neural_fulldoc_disambig.py $INPUT_FILE ACE2004_first20_CoNLL_neural_flair_ner_fast_disambig_08.tsv ner-fast true 0.8
#
# python3 $CONLL_CONV_DIR/convertSysOutput2CoNLLEvalInput.py ACE2004_first20_CoNLL_neural_flair_ner_fast_disambig_08.tsv
#
# python3 $CONLL_CONV_DIR/DisambiguationMatches.py ACE2004_first20_CoNLL_neural_flair_ner_fast_disambig_08.txt
#
# python3 $CONLL_CONV_DIR/conlleval.py ACE2004_first20_CoNLL_neural_flair_ner_fast_disambig_08sourc.txt > ACE2004_first20_CoNLL_neural_flair_ner_fast_disambig_08.metrics
