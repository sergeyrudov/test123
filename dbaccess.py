# -*- coding:utf-8 -*-
import json

def save(db):
    json.dump(db,open(r'db.json','w'),indent =4)

def load():
    return json.load(open(r'db.json','r'))