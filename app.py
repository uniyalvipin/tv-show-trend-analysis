import os
from flask import Flask, render_template, request, send_from_directory
import fetch
import dirwalk
import pandas as pd

app = Flask(__name__)

resultlist = []
query = " "


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        global query
        global resultlist
        query = request.form['query']
        if query not in dirwalk.showslist():
            resultlist = fetch.main(query)
        else:
            df=pd.read_csv('data/'+query+'.csv')
            resultlist.append(len(df))
            resultlist.append(df["polarity"].mean())
            resultlist.append(df['subjectivity'].mean())
            if int(resultlist[1]) > 0:
                resultlist.append('Positive')
            elif int(resultlist[1]) == 0:
                resultlist.append('Neutral')
            else:
                resultlist.append('Negative')
    return render_template('index.html')


# favicon route
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/result', methods=['POST', 'GET'])
def result():
    '''resultlist = []
    if request.method == 'POST':
        query = request.form['query']
        if query not in dirwalk.showslist():
            resultlist = fetch.main(query)'''
    return render_template("result.html", query=query, tweets_count=resultlist[0], avgpol=resultlist[1],
                           avgsub=resultlist[2], pol=resultlist[3])


@app.route('/list')
def list():
    showlist = dirwalk.showslist()
    return render_template("list.html", showlist=showlist)


if __name__ == '__main__':
    app.run(debug=True)

