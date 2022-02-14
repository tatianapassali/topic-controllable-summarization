import nltk
from nltk.corpus import wordnet

lemmatizer = nltk.stem.WordNetLemmatizer()  # Initiate nltk lemmatizer


def simple_tokenize(sentence):
    """ Simple function for tokenizing text with nltk """
    return nltk.word_tokenize(sentence)


def nltk_to_pos(pos):
    """ Simple function for converting nltk pos to wordnet pos"""
    if pos.startswith('J'):
        return wordnet.ADJ
    elif pos.startswith('V'):
        return wordnet.VERB
    elif pos.startswith('N'):
        return wordnet.NOUN
    elif pos.startswith('R'):
        return wordnet.ADV
    else:
        return None


def lemmatize_text(text):
    """ Function to lemmatize text according to the wordnet POS of each token """

    tokenized_text = nltk.word_tokenize(text)
    POS_assigned_text = nltk.pos_tag(tokenized_text)

    available_POS = map(lambda x: (x[0], nltk_to_pos(x[1])), POS_assigned_text)

    lemmatized_text = [token if pos is None
                       else lemmatizer.lemmatize(token, pos)
                       for token, pos in available_POS]

    return lemmatized_text
