import os
import pickle


def load_data(path):
    """
    Load Dataset from File
    """
    input_file = os.path.join(path)
    with open(input_file, "r") as f:
        data = f.read()

    return data

def preprocess_and_save_text(text, token_lookup, create_lookup_tables):
    token_dict = token_lookup()
    for key, token in token_dict.items():
        print('key', key)
        text = text.replace(key, ' {} '.format(token))

    print('lower')
    text = text.lower()
    print('split')
    text = text.split()

    print('create lookup')
    vocab_to_int, int_to_vocab = create_lookup_tables(text)
    print('to int')
    int_text = [vocab_to_int[word] for word in text]
    print('pickle')
    pickle.dump((int_text, vocab_to_int, int_to_vocab, token_dict), open('preprocess.p', 'wb'))

    
def preprocess_and_save_data(dataset_path, token_lookup, create_lookup_tables):
    """
    Preprocess Text Data
    """
    text = load_data(dataset_path)
    
    # Ignore notice, since we don't use it for analysing the data
    text = text[81:]

    preprocess_and_save_text(text, token_lookup, create_lookup_tables)

def load_preprocess():
    """
    Load the Preprocessed Training data and return them in batches of <batch_size> or less
    """
    return pickle.load(open('preprocess.p', mode='rb'))


def save_params(params):
    """
    Save parameters to file
    """
    pickle.dump(params, open('params.p', 'wb'))


def load_params():
    """
    Load parameters from file
    """
    return pickle.load(open('params.p', mode='rb'))
