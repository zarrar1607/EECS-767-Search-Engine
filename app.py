from flask import Flask, render_template, request
from lib.query_processor import *
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    # Get the query text from the HTML form
    query = request.form['query']
    print(query)
    
    search_results = search_query(query)
    save_table(pd.DataFrame(search_results).head(5),'result')
    
    result = pd.read_csv('./Data/result.csv')
    # Convert the document IDs to document titles
    print(result.head())
    #titles = result['doc_id']
    # iterate over the rows of the DataFrame and print each row
    '''for index, row in result.iterrows():
        print(f"doc_id: {row['doc_id']}, score: {row['0']}")'''
    # Render the search results template with the top documents
    return render_template('results.html', query=query, titles= result)
    #df = titles
    #return render_template('simple.html',  tables=[result.to_html(classes='data')], titles=df.columns.values)


if __name__ == '__main__':
    app.run()