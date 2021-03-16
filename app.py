import requests
from flask import Flask,Request,jsonify,render_template
import json
import os
app = Flask(__name__)
app.secret_key = os.urandom(12)


@app.route('/find_symbols_in_names', methods = ['GET','POST'])
def loadContent():
    
    task = {
        "chemicals": ['Amazon', 'Microsoft', 'Google'],
        "symbols": ['I', 'Am', 'cro', 'Na', 'le', 'abc']}    
    res = []
    for vals in task["chemicals"]:
        s= ''
        for val in task["symbols"]:
            found = vals.find(val)
            if found!=-1:
                for i in range(0,len(vals)):
                    if i == found:
                        s+='['+vals[i]
                    elif i==found+len(val)-1:
                        s+=vals[i]+']'
                    else:
                        s+=vals[i]
                res.append(s)
    dict1 = {"Result":res} 
    return jsonify(dict1)

if __name__ == '__main__':
    app.run(debug = True)