# hello.py
import random,json
from flask import Flask, render_template

def getQA(fname):
    # df = pd.read_excel(fname)
    # QA = df.T.to_dict()
    # Question = []
    # for i in QA.values():
    #     Question.append(i)
    with open(fname,'r',encoding='utf8')as f:
        Question = json.loads(f.read())
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
        thisQA = getQA('prof.json')
    elif Playertype=='normal':
        thisQA = getQA('normal.json')
    resp,thisQA = getoneQ(thisQA)
    return render_template('Q.html',Question=resp,RightNum=0)

@app.route("/next/<int:score>")
def next(score):
    global thisQA
    if score >= 5:
        return render_template('win.html')
    if len(thisQA)==0:
        return render_template('lose.html')
    resp,thisQA = getoneQ(thisQA)
    return render_template('Q.html',Question=resp,RightNum=score)

@app.route("/error")
def error():
    raise RuntimeError

if __name__ == "__main__":
    pQAs = getQA('prof.json')
    nQAs = getQA('normal.json')
    thisQA = []
    app.run()