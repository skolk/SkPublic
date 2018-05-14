import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database2' user='postgres' password='greyink' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database2' user='postgres' password='greyink' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)" , (item,quantity,price))
    conn.commit()
    conn.close()

#insert("coffee cup",4,6)

def view():
    conn=psycopg2.connect("dbname='database2' user='postgres' password='greyink' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database2' user='postgres' password='greyink' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(item,quantity,price):
    conn=psycopg2.connect("dbname='database2' user='postgres' password='greyink' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

#insert("apple",10,15)
#insert("orange",10,15)
#delete("apple")
#create_table()
update("orange",1,2)

#insert("coffee cup",8,7)
#update("coffee cup", 2, 3)
print(view())
