#!/bin/bash
python3 methods/tagging-based/tagging.py  -input_file data/topic_dataset/topic_embeddings/test.csv \
                    -topic_seeds data/topic_dataset/topic_seeds.csv \
                    --text_column article \
                    --summary_column highlights \
                    --topic_column topic \
                    --chunksize 1000 \
                    --output_file data/topic_dataset/tagging_data/test.csv \
