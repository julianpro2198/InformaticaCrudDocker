from itertools import product
from flask import Flask,request,jsonify
import sqlite3 as sql
import json

app=Flask(__name__)


con=sql.connect("infdb.db")
con.row_factory=sql.Row
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT,valor INTEGER,id INTEGER,PRIMARY KEY(id))")


@app.route('/product-all')
def product_all():
    con=sql.connect("infdb.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from productos")
    data=cur.fetchall()
    productlist = []
    for row in data:
        productlist.append([x for x in row])
    return json.dumps(productlist)
    
@app.route("/product-edit",methods=['POST'])
def product_edit():

    data = request.get_json()
    productid = data['id']
    nnombre = data['nnombre']
    nprecio = data['nprecio']

    con=sql.connect("infdb.db")
    cur=con.cursor()
    cur.execute("update productos set nombre=?,valor=? where id=?",(nnombre,nprecio,productid))
    con.commit()
        
    return "200 : product updated"

@app.route("/product-delete",methods=['POST'])
def product_delete():
    
    data = request.get_json()
    productid = data['id']

    con=sql.connect("infdb.db")
    cur=con.cursor()
    cur.execute("delete from productos where id=?",(productid,))
    con.commit()
    return "200: Product deleted"


@app.route("/product-create",methods=['POST'])
def client_create():
    
    data = request.get_json()
    productid = data['id']
    productname = data['nnombre']
    productvalue = data['valor']

     
    con=sql.connect("infdb.db")
    cur=con.cursor()
    cur.execute("insert into productos(nombre,valor,id) values (?,?,?)",(productname,productvalue,productid))
    con.commit()
      
    return ("200: Product created")

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
