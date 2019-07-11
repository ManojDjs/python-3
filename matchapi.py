import pymongo
from pymongo import MongoClient, DESCENDING
from flask import Flask, jsonify,render_template
import requests
from difflib import SequenceMatcher
from pymongo import MongoClient
app = Flask(__name__,template_folder='template')
@app.route('/',methods=['GET'])
def success():
    client = MongoClient('mongodb://jobiak:j0Bi%40kSt%40ge@18.223.47.109:28015/stage_jobs')
    if(client): print("connected")
    db=client.stage_jobs
    collection=db.users
    doc=collection.find({})
    lis=[]
    for i in doc:
        name=i['user_name']
        email=i['user_email']
        print(name)
        dic={}
        dic['user']=name
        dic['email']=email
        lis.append(dic)
    print(lis)
    return render_template('index.html',dic=lis)
if __name__ == '__main__':
    app.run(port=3804)
