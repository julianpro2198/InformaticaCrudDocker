from flask import Flask,request,jsonify
import sqlite3 as sql
import json

app=Flask(__name__)


con=sql.connect("infdb.db")
con.row_factory=sql.Row
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS clientes (nombre TEXT,apellido TEXT,cedula INTEGER,PRIMARY KEY(cedula))")


@app.route('/client-all')
def client_all():
    con=sql.connect("infdb.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from clientes")
    data=cur.fetchall()
    clientlist = []
    for row in data:
        clientlist.append([x for x in row])
    return json.dumps(clientlist)
    
@app.route("/client-edit",methods=['POST'])
def client_edit():

    data = request.get_json()
    userid = data['id']
    nnombre = data['nnombre']
    napellido = data['napeliido']

    con=sql.connect("infdb.db")
    cur=con.cursor()
    cur.execute("update clientes set nombre=?,apellido=? where cedula=?",(nnombre,napellido,userid))
    con.commit()
        
    return "200 : Client updated"

@app.route("/client-delete",methods=['POST'])
def client_delete():
    
    data = request.get_json()
    userid = data['id']

    con=sql.connect("infdb.db")
    cur=con.cursor()
    cur.execute("delete from clientes where cedula=?",(userid,))
    con.commit()
    return "200: Client deleted"


@app.route("/client-create",methods=['POST'])
def client_create():
    
    data = request.get_json()
    userid = data['id']
    nnombre = data['nnombre']
    napellido = data['napeliido']

     
    con=sql.connect("infdb.db")
    cur=con.cursor()
    cur.execute("insert into clientes(nombre,apellido,cedula) values (?,?,?)",(nnombre,napellido,userid))
    con.commit()
      
    return ("200: Client created")

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
