from helpers import is_csv_format
from data_tagger import tag_data
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-input_file", required=True,
                        help="The input file (.csv) which contains any textual data.")
    parser.add_argument("-topic_seeds", required=True, help="The topic input file (.csv) which contains "
                                                            "the particular "
                                                            "topics along "
                                                            "with their seed words")
    parser.add_argument("--text_column", required=False, help='The corresponding column of text that you want to tag. '
                                                              'If not specified, the first column of file is assumed '
                                                              'for text.')
    parser.add_argument("--summary_column", required=False, help='The corresponding column of summary.'
                                                                 'If not specified, the second column of file is '
                                                                 'assumed '
                                                                 'for summary')
    parser.add_argument("--topic_column", required=False, help='The corresponding column of topic.'
                                                               'If not specified, the third column of file is '
                                                               'assumed '
                                                               'for topic')
    parser.add_argument("--chunksize", required=False, help="Size of the chunk-size that will be processed. Use "
                                                            "this "
                                                            "when processing large input data that do not fit in "
                                                            "memory (default value 1000)")
    parser.add_argument("--output_file", required=False, help="The directory for the output file. If not specified, "
                                                              "the output file will be created into the directory data/created_data.")

    args = parser.parse_args()
    print(args.text_column)

    if not is_csv_format(args.input_file) or not is_csv_format(args.topic_seeds):
        raise ValueError("The input file " + args.input_file + "must be formatted as csv.")

    tag_data(input_data_path=args.input_file,
             text_column=args.text_column,
             summary_column=args.summary_column,
             topic_column=args.topic_column,
             topic_word_seeds_path=args.topic_seeds,
             chunksize=args.chunksize,
             output_data_path=args.output_file)
