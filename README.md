# Entity Spaces for Tolerant Entity Linking: Code and Data
April 10th, 2019


This package includes the experimental code and data and experimental results.

**Note on data**
For the review, in this package, we include the evaluation datasets used in the This is not for redistribution as we do not have the licenses to all the data. In the published version we will include the appropriate links and the data we can distribute.

* The taggers here run on python3.
* We assume you're running in a virtualenv
* pip install -r requirements.txt
* You'll need to have installed:
    * [https://github.com/dalab/end2end\_neural\_el](https://github.com/dalab/end2end_neural_el)
    * [https://github.com/dice-group/AGDISTIS](https://github.com/dice-group/AGDISTIS)
* In ./amstel - you'll find the taggers used in the pipeline.
* All data and evaluation results and scripts are in /data
* Experimental results are in this includes intermediate output.
    * data/experiment-results-agdistis
    * data/experiment-results-neural
* Shell scripts to run experiments are in:
   * scripts-neural
   * scripts-agdistis
   * Note, you'll need to uncomment different parts of the scripts to run el and ed variants for the neural based entity linker. This is because the end2end\_neural\_el runs on the same port for both services.
   * This will generate results in the file.

* Paper Pipelines to Scripts mapping:
   * [neural el] - Run end2end\_neural\_el in its entity linking setting. This uses tagger\_neural\_fulldoc2.py.
   * [neural ed] - Run end2end\_neural\_el in it entity disambiguation setting. This uses tagger_neural\_fulldoc\_disambig.py
   * [neural d1.0] - parameters are shown in the scripts
   * [neural d0.8] - parameters are shown in the scripts
   * [mag ed] -  Run AGDISTIS. Assumes you are running locally. You can modify tagger\_agdistis\_fulldoc.py to use the remote services.
   * [mag d1.0] - parameters are shown in the scripts
   * [mag d0.8] - arameters are shown in the scripts

* To generate the evaluation data for non-linkable entities:
	*  run the script conll_conversion/convertSysOutput2CoNLLEvalInput\_NMEsKeptIn.py on the data in data/experiments-results-agdistis and data/experiments-results/neural 
	*  results can be found in data/evaluate\_with-non-linkable-entities\_agdistis and data/evaluate_with-non-linkable-entities\_neural 
