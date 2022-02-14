# Tagging-based formulation

This directory contains code for topic-controllable summarization using a simple tagging-based formulation.
This method employs a trivial mechanism to shift the summary
generation towards the desired topic, assuming the
existence of a set of representative terms for each
thematic category. After lemmatization, the most representative words for the desired topic are tagged with special tag tokens before
feeding to the summarization model.


To fine-tune your own model with tagging, you can run the run.summarization.py as follows:

```
python3 run_summarization.py \
    --model_name_or_path MODEL_NAME \
    --tokenizer MODEL_NAME \
    --do_train \
    --do_eval \
    --train_file PATH_OF_TRAIN_FILE \
    --test_file  PATH_OF_TEST_FILE \
    --validation_file PATH_OF_VALIDATION_FILE \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=12 \
    --predict_with_generate \
```

For more information about run_summarization.py arguments, visit Hugging Face [repository]([https://github.com/huggingface/transformers]).

### Preprocess the data

To create a tagging-based dataset, you will need a topic-assigned document collection along with a set of most representative terms for each topic.
You can use the topic-assigned dataset along with the provided file that contains most representative words for each thematic category.

First, clone the repository and move to the main directory

```
git clone 
cd topic-controllable-summarization/
```

Download the data from [here](https://drive.google.com/drive/folders/1j7ZHsza0kyo5QlB2b7_UH_aWEaBNEbPR?usp=sharing) and unzip it under the data directory. Then you can run the script for creating the tagged data for each file

```
sh methods/tagging-based/tagging_data.sh
```

You can modify the above script to tag any textual data, provided that a set of most representative terms exist.

