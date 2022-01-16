import json
from flask import Flask, render_template, jsonify

# Data Store  
app = Flask(__name__)

with open("county_fast_food_final.json") as fp:
    search_results1 = json.load(fp)
   #  print(search_results)
   
with open("county_dollar_stores_final.json") as fp2:
    search_results2 = json.load(fp2)
   #  print(search_results)

with open("county_grocery_stores_final.json") as fp3:
    search_results3 = json.load(fp3)
   #  print(search_results)
   
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/data1/')
def data1():
    return jsonify(search_results1)
 
@app.route('/data2/')
def data2():
    return jsonify(search_results2)

@app.route('/data3/')
def data3():
    return jsonify(search_results3)
    
if __name__ == '__main__':
   app.run(debug=True, port=5001)