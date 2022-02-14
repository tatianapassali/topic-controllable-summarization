def is_csv_format(file):
    """ Simple function for checking if input file is formatted as .csv file """

    file_type = file.split(".")[-1]
    if file_type != 'csv':
        return False
    else:
        return True


def check_columns(data, text_column, summary_column, topic_column):
    """ Simple function for returning correct text, summary and topic column from dataframe"""

    if text_column is None:
        text_column = data.columns[0]

    if summary_column is None:
        summary_column = data.columns[1]

    if topic_column is None:
        topic_column = data.columns[4]

    return text_column, summary_column, topic_column


def check_chunk(chunksize):
    """ Simple function for checking if chunksize is defined"""
    if chunksize is None:
        chunksize = 1000
    else:
        chunksize = int(chunksize)
    return chunksize
