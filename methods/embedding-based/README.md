# Embedding-based formulation

This directory contains code to perfοrm topic-based summarization using topic embeddings.

To fine-tune your own model using topic embeddings, you can run the run.summarization.py as follows:

```
python3 run_summarization.py \
    --model_name_or_path facebook/bart-large \
    --tokenizer facebook/bart-large \
    --do_train \
    --do_eval \
    --train_file PATH_OF_TRAIN_FILE \
    --test_file  PATH_OF_TEST_FILE \
    --validation_file PATH_OF_VALIDATION_FILE \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=12 \
    --predict_with_generate \
```

*NOTE: Currently, the only model that is supported for summarization with topic embeddings is BART-large. You can adjust the architecture of other Transformers models similarly with [modelling_bart.py](methods/embedding-based/modelling_bart.py) file to add topic embeddings.*

Note that this code requires a topic-assigned document collection in order to successfully fine-tune BART-large for topic-controllable summarization. The dataset that is used for this work uses as a basis the  CNN/DailyMail and can be found on [datasets directory](data/topic_dataset/topic_embeddings). We use the version 3.0.0. of CNN/DailyMail as provided from [Hugging Face hub](https://huggingface.co/datasets/cnn_dailymail).

For more information about the dataset creation, you can read our paper.

For more information about run_summarization.py arguments, visit Hugging Face [repository]([https://github.com/huggingface/transformers]).
