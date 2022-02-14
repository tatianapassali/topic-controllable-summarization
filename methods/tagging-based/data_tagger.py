from utils import lemmatize_text, simple_tokenize
from helpers import check_columns, check_chunk
import pandas as pd


def tag_data(input_data_path, text_column, summary_column, topic_column, topic_word_seeds_path, chunksize,
             output_data_path):

    # Extract all the available topics from file
    topics_df = pd.read_csv(topic_word_seeds_path)

    chunksize = check_chunk(chunksize)

    for data in pd.read_csv(input_data_path, chunksize=chunksize):

        text_column, summary_column, topic_column = check_columns(data, text_column, summary_column, topic_column)

        print("Processing data with chunk-size ", len(data))
        print("Initiate tokenization...")
        data['original_tokens'] = data[text_column].apply(lambda x: simple_tokenize(x))
        print(u'\u2713' + " Tokenization completed")

        print("Initiate lemmatization...")
        print("Warning: This process might take a little longer")
        data['lemmatize'] = data['article'].apply(lambda x: lemmatize_text(x))
        print(u'\u2713' + " Lemmatization completed")

        lemmatized_tokens = data['lemmatize'].values.tolist()
        original_tokens = data['original_tokens'].values.tolist()
        assigned_topics = data['topic'].values.tolist()

        tagged_tokens = []

        print("Processing lemmatized tokens....")
        for i in range(len(lemmatized_tokens)):
            if assigned_topics[i] not in topics_df.columns:
                raise ValueError("Topic " + str(assigned_topics[i]) + "is not included in topic file.")

            # Extract all the seed words according to the corresponding topic
            token_topics = topics_df[assigned_topics[i]].values.tolist()
            original_list = original_tokens[i]

            for j, token in enumerate(lemmatized_tokens[i]):
                # If the lemmatized form of the token is in topic seeds, tag the original token
                if token.lower() in token_topics:
                    original_list[j] = '[TAG]' + original_list[j] + '[TAG]'

            tagged_tokens.append(" ".join(original_list))

        data["tagged_text"] = tagged_tokens

        if output_data_path is None:
            output_dir = 'data/created_files/tagged_data.csv'
        else:
            output_dir = output_data_path

        print("Saving to directory " + str(output_dir))
        data = data[['tagged_text', summary_column, topic_column]]
        data.to_csv(output_dir, mode='a', header=False, index=False)
