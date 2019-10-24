from flask import Flask, redirect , request, url_for
from pymongo import MongoClient
client = MongoClient('mongo',27017)
db = client.todo
coll = db.mylist
  

app = Flask(__name__)
def printlist():
  st = """<h1> list of tasks </h1> 
  <h3>"""
  p = coll.find()
  
  for doc in p:
          word = doc['task']
          st = st + word + '<br>'
  st = st + '</h3>\n'

  return st

@app.route('/update',methods=['GET','POST'])
def apply():
  types = request.form['type']
  task = request.form['task']

  if types=='add':
     coll.insert_one({'task':task})
  else:
     coll.delete_one({'task':task})
  
  return redirect(url_for('index'))

@app.route('/')
def index():
  st=printlist()
  form_word = '''<form action="/update" method="post">
  <h3>add/delete  <input type='text' name='type' /><br>
  task  <input type='text' name='task' /><br>
  <input type='submit'>
  '''
  return st+form_word


if __name__ == "__main__":
        app.run(host="0.0.0.0",debug=True,port="9000")