#!/bin/bash

INPUT_FILE="../evaluation_datasets/AIDA-YAGO2-dataset-testb_only_useful_columns.tsv"

AMSTEL_DIR="../../amstel"
CONLL_CONV_DIR="../../conll_conversion"

#EL
#python3 $AMSTEL_DIR/tagger_neural_fulldoc2.py $INPUT_FILE AIDA-YAGO2-dataset-testb_only_useful_columns_neural.tsv

#python3 $CONLL_CONV_DIR/convertSysOutput2CoNLLEvalInput.py AIDA-YAGO2-dataset-testb_only_useful_columns_neural.tsv

#python3 $CONLL_CONV_DIR/conlleval.py AIDA-YAGO2-dataset-testb_only_useful_columns_neural.txt > AIDA-YAGO2-dataset-testb_only_useful_columns_neural.metrics

#No Disambiguation
 python3 $AMSTEL_DIR/tagger_agdistis_fulldoc.py $INPUT_FILE AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast.tsv ner-fast false 1.0
#
 python3 $CONLL_CONV_DIR/convertSysOutput2CoNLLEvalInput.py AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast.tsv
#
 python3 $CONLL_CONV_DIR/conlleval.py AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast.txt > AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast.metrics
#
# #Disambiguation 1.0
 python3 $AMSTEL_DIR/tagger_agdistis_fulldoc.py $INPUT_FILE AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast_disambig_10.tsv ner-fast true 1.0
#
 python3 $CONLL_CONV_DIR/convertSysOutput2CoNLLEvalInput.py AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast_disambig_10.tsv
#
 python3 $CONLL_CONV_DIR/DisambiguationMatches.py AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast_disambig_10.txt
#
 python3 $CONLL_CONV_DIR/conlleval.py AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast_disambig_10sourc.txt > AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast_disambig_10.metrics

# #Disambiguation 1.0
python3 $AMSTEL_DIR/tagger_agdistis_fulldoc.py $INPUT_FILE AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast_disambig_08.tsv ner-fast true 0.8
#
python3 $CONLL_CONV_DIR/convertSysOutput2CoNLLEvalInput.py AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast_disambig_08.tsv
#
python3 $CONLL_CONV_DIR/DisambiguationMatches.py AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast_disambig_08.txt
#
python3 $CONLL_CONV_DIR/conlleval.py AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast_disambig_08sourc.txt > AIDA-YAGO2-dataset-testb_only_useful_columns_neural_flair_ner_fast_disambig_08.metrics


head n -2 AIDA-YAGO2-dataset-testb_only_useful_columns*metrics
