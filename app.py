from flask import Flask, request 
import pandas as pd 
import sqlite3
import numpy as np
app = Flask(__name__) 

@app.route('/bestbook/')
def data():
    df = pd.read_csv('data/books_c.csv')
    df = df[df['average_rating'] >= 4]
    return (df.to_json())

@app.route('/Genre2012/')
def genre():
    conn = sqlite3.connect("data/chinook.db")
    invoice2012 = pd.read_sql_query(
    '''
    SELECT genres.Name as Genre, invoices.*, invoice_items.InvoiceLineId
    FROM invoices
    LEFT JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
    LEFT JOIN tracks ON tracks.TrackId = tracks.TrackId
    LEFT JOIN genres ON genres.GenreId = tracks.GenreId
    WHERE Genre = 'Rock' AND invoices.InvoiceDate >= '2012-01-01'
    ''',
    conn
    )
    return (invoice2012.to_json())

@app.route('/rating_book/<value>', methods=['GET'])
def min_rating(value):
    book = pd.read_csv('data/books_c.csv')
    mask = book['average_rating'] <= float(value)
    book = book[mask]
    return (book.to_json())  
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)