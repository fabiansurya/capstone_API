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
    SELECT genres.Name as Genre, invoice_items.InvoiceLineId, invoices.BillingCity,
    invoices.BillingCountry, invoices.CustomerId, invoices.InvoiceDate, invoices.Total  
    FROM invoices
    LEFT JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
    LEFT JOIN tracks ON tracks.TrackId = tracks.TrackId
    LEFT JOIN genres ON genres.GenreId = tracks.GenreId
    WHERE Genre = 'Rock' AND invoices.InvoiceDate >= '2012-06-01'
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

@app.route("/docs")
def documentation():
    return '''
        <h1> Documentation </h1>
        <h2> Static Endpoints 1 </h2>
        <ol>
            <li>
                <p> /bestbook/ methods=['GET'] </p>
                <p> Merupakan static endpoint untuk mengembalikan informasi dari books_c.csv dengan rating minimal 4  </p>
            </li>
        </ol>
        
        <h2> Static Endpoints 2 </h2>
        <ol>
            <li>
                <p> /Genre2012/ methods=['GET'] </p>
                <p> Merupakan static endpoint untuk mengembalikan informasi dari chinook.db untuk seluruh invoice dari tahun 2012 untukgenre 'Rock</p>
            </li>
        </ol>
         
        <h2> Dynamic Endpoints 1</h2>
        <ol start = "2">
            <li>
                <p> /rating_book/&lt;value&gt;methods=['GET'] </p>
                <p> Merupakan dynamic endpoint untuk mengembalikan informasi dari books_c.csv dengan rating dibawah sesuai dengan keinginan kita dalam bentuk JSON </p>
            </li>
        </ol>
    '''
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
