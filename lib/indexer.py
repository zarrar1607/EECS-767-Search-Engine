import pandas as pd
import numpy as np
import math
from sklearn.metrics.pairwise import cosine_similarity
from lib.data_handler import *

def build_inverted_index(documents):
    inverted_index = {}
    for doc_id, doc_content in documents.items():
        terms = re.findall(r'\w+', doc_content.lower())
        for term in terms:
            if term not in inverted_index:
                inverted_index[term] = {}
            if doc_id not in inverted_index[term]:
                inverted_index[term][doc_id] = 0
            inverted_index[term][doc_id] += 1
    save_table(pd.DataFrame(inverted_index), 'inverted_index')
    return inverted_index

def calc_term_freq(inverted_index):
    # build a list of all terms in the inverted index
    all_terms = sorted(list(set(term for term in inverted_index.keys())))
    
    save_as_text(all_terms, 'all_terms')

    # build a list of all documents in the inverted index
    all_docs = sorted(list(set(doc_id for term in inverted_index.keys() for doc_id in inverted_index[term].keys())))
    save_as_text(all_docs, 'all_docs')
    

    # calculate term frequency for each document
    term_frequency = {}
    for term in all_terms:
        term_frequency[term] = {}
        for doc_id in all_docs:
            if doc_id in inverted_index[term]:
                term_frequency[term][doc_id] = inverted_index[term][doc_id]
            else:
                term_frequency[term][doc_id] = 0
    
    
    return term_frequency

def normalize_vectors(tfidf_table):
    """
    Given a TF-IDF table, normalize each document vector using L2 normalization.
    Returns a new normalized TF-IDF table.
    """
    norm_table = tfidf_table.copy()
    norm_table.iloc[:, 1:] = norm_table.iloc[:, 1:].apply(lambda x: x / np.sqrt(np.sum(np.square(x))), axis=1)
    return norm_table

def create_tf_idf(inverted_index):
    term_frequency = calc_term_freq(inverted_index)
    print(term_frequency)
    all_terms = load_from_txt('all_terms')
    all_docs = load_from_txt('all_docs')

    # calculate inverse document frequency
    doc_count = len(all_docs)
    inverse_doc_frequency = {}
    for term in all_terms:
        doc_freq = len(inverted_index[term])
        inverse_doc_frequency[term] = math.log(doc_count / doc_freq) # log(N/df)

    
    idf = pd.DataFrame.from_dict(inverse_doc_frequency, orient='index', columns=['idf'])
    idf = idf.T
    #print(idf_df.head())
    save_table(idf, 'idf')

    # calculate tf-idf
    tf_idf = {}
    for term in all_terms:
        tf_idf[term] = {}
        for doc_id in all_docs:
            tf = term_frequency[term][doc_id]
            idf = inverse_doc_frequency[term]
            tf_idf[term][doc_id] = tf * idf
    
    # convert to pandas DataFrame
    df = pd.DataFrame(tf_idf)

    normalized_df = normalize_vectors(df)
    normalized_df.to_csv("./data/tf_idf.csv", index_label="doc_id")
    return normalized_df



