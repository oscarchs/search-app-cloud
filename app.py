from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from sys import stdin
import re
import os

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'database-1.c7bfmd9vlb4s.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'MAhm6vOGUsDkKsdNmHaT'


mysql = MySQL(app)


def call_page_rank():
  os.system("hdfs dfs -put page_rank_input.txt cloudcomputing/page_rank_input/")



def generate_adj_matrix(inverted_index):
  matrix = []
  for line in inverted_index:
    documents = line[1]
    list_documents = documents.split(',')
    tmp = [re.sub(':[0-9]{1,999}', '', document) for document in list_documents]
    matrix.append(tmp)


  adjacency_list = {}
  for row in matrix:
    for element in row:    
      pivot = element    
      for neighbor in row:
        if pivot!=neighbor:
          key = pivot + ':' + neighbor
          adjacency_list[key] = {'from': pivot, 'to': neighbor}

  page_rank_input = ""
  for key in adjacency_list:
      page_rank_input += '%s\t%s\n' % (adjacency_list[key]["from"], adjacency_list[key]["to"])
  file = open('page_rank_input.txt', 'w')
  file.write(page_rank_input)
  call_page_rank()

@app.route("/search", methods=["POST", "GET"])
def search():
  if request.method == 'POST':    
    keywords = request.form['keywords']	
    print(keywords)
    keyword_array = keywords.split()
    cursor = mysql.connection.cursor()
    query = "SELECT word, inverted_index_value FROM `search_engine_dataset`.`inverted_index` where word in ("
    if keyword_array:
      if len(keyword_array) == 1:
        query += "'%s');" % keyword_array[0]
      else:
        for idx, word in enumerate(keyword_array):
          if idx == len(keyword_array)-1:
            query = query[:-1]
            query += ",'%s');" % word        
          else:
            query += "'%s'," % word
    print(query)
    cursor.execute(query)
    from_inverted_index = cursor.fetchall()
    output = []
    for record in from_inverted_index:
      output.append(record)
    #print(output)
    generate_adj_matrix(from_inverted_index)
    return render_template('resultados.html', result = ':D')
  return render_template('index.html')


@app.route('/')
def hello_world():
	return ':D'

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=4000, debug=True)
