# hello.py
import pandas as pd
import random
from flask import Flask, request, render_template

def getQA(fname):
    df = pd.read_excel(fname)
    QA = df.T.to_dict()
    Question = []
    for i in QA.values():
        Question.append(i)
    return Question

def selectionModifier(s):
    return f'<button>{s}</button>'
def getoneQ(thisQA):
    # tmpQ = thisQA.pop()
    i = random.randrange(0,len(thisQA))
    tmpQ = thisQA.pop(i)
    return tmpQ,thisQA

app = Flask(__name__)

@app.route("/")
def index():
    with open('index.html','r',encoding='utf8')as f:
        return f.read()#"<h1>Hello Word</h1>"

@app.route("/start/<Playertype>")
def start(Playertype):
    global thisQA
    if Playertype=='professional':
        thisQA = pQAs.copy()
    elif Playertype=='normal':
        thisQA = nQAs.copy()
    resp,thisQA = getoneQ(thisQA)
    return render_template('Q.html',Question=resp,RightNum=0)

@app.route("/next/<int:score>")
def next(score):
    if score >= 5:
        return render_template('win.html')
    global thisQA
    resp,thisQA = getoneQ(thisQA)
    return render_template('Q.html',Question=resp,RightNum=score)

@app.route("/error")
def error():
    raise RuntimeError

if __name__ == "__main__":
    pQAs = getQA('prof.xlsx')
    nQAs = getQA('normal.xlsx')
    thisQA = []
    app.run()