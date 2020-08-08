# API Capstone
API ini dinominasikan sebagai capstone project yang berguna untuk mengirimkan data kepada user. Proses wrangling dilakukan sesuai endpoint-endpoint dibawah. Base url dari aplikasi ini adalah https://fabfabfab99.herokuapp.com
Endpoints: 
```
    1. /bestbook/ methods=['GET']
    Merupakan static endpoint untuk mengembalikan informasi dari books_c.csv dengan rating minimal 4  
    
    2. /rating_book/<value>methods=['GET']
    Merupakan dynamic endpoint untuk mengembalikan informasi dari books_c.csv dengan rating dibawah sesuai dengan keinginan kita dalam bentuk JSON
        
    3. /Genre2012/ methods=['GET']
    Merupakan static endpoint untuk mengembalikan informasi dari chinook.db untuk seluruh invoice dari tahun 2012 untuk genre 'Rock', 'Jazz', 'Metal'
```
___
## Dependencies
- Pandas    (pip install pandas)
- Flask     (pip install flask)
- Gunicorn  (pip install gunicorn)

__
# Link untuk akses
- https://fabfabfab99.herokuapp.com/bestbook/
- https://fabfabfab99.herokuapp.com//rating_book/3.5
- https://fabfabfab99.herokuapp.com/Genre2012
