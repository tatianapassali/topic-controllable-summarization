#!/bin/bash
python3 methods/tagging-based/tagging.py  -input_file data/test.csv \
                    -topic_seeds data/topic_seeds.csv \
                    --text_column article \
                    --summary_column highlights \
                    --topic_column topic \
                    --chunksize 10 \
                    --output_file data/tagged_test.csv \
