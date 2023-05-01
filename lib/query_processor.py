from lib.data_handler import *
import numpy as np

def search_query(query):
    # Get tf_idf_table
    tf_idf = load_table('tf_idf')
    # Preprocess the query text
    query = preprocess_text(query)
    # Split the query into individual terms
    query_terms = query.split()
    # Initialize a vector of zeros with the same number of columns as the tfidf_df
    query_vec = np.zeros(tf_idf.shape[1])

    #print(query_terms)
    #print(query_vec)
    # Loop through each term in the query
    for term in query_terms:
        # Check if the term is in the columns of the tfidf_df
        if term in tf_idf.columns:
            # Get the column number of the term in the tfidf_df
            col_num = tf_idf.columns.get_loc(term)
            # Increment the corresponding element in the query_vec by 1
            query_vec[col_num] += 1
    #print(query_vec)
    
    # Load the idf_table.csv file into a pandas dataframe
    idf = load_table('idf')
    
    # Loop through each unique term in the query
    for term in set(query_terms):
        # Check if the term is in the columns of the tfidf_df
        if term in tf_idf.columns:
            # Get the column number of the term in the tfidf_df
            col_num = tf_idf.columns.get_loc(term)
            # Multiply the corresponding element in the query_vec by the idf value for that term
            query_vec[col_num] *= idf.values[0][col_num]
    #print(idf)
    #print(query_vec)
    # Normalize the query vector to unit length
    if not np.all(query_vec == 0):
        query_vec /= np.linalg.norm(query_vec)
    
    # Compute the cosine similarity between the query vector and each document vector in the tfidf_df
    scores = tf_idf @ query_vec

    # Sort the documents by their cosine similarity score in descending order
    ranked_docs = scores.sort_values(ascending=False)
    
    return ranked_docs


