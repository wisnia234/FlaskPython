from flask import Blueprint
from flask import request
import archiveItems
import bigQueryUploader
import random
import os
from timeit import default_timer as timer
from datetime import timedelta

endpoints = Blueprint('endpoints', __name__)

@endpoints.route('/')
def firstPage():
    return 'Welcome !'

@endpoints.route('/get-item')
def getRandomNumber():
    start = timer()
    item = random.random() 
    end = timer()
    bigQueryUploader.logDataToBigQuery(f'{timedelta(seconds=end-start)}', item)
    #archiveItems.writeItem(item)

    return f'{item}'

@endpoints.route('/get-author-name')
def getAuthorName():
    return "<h1>Michal Wisniewski</h1>"

@endpoints.route('/get-from-query', methods=['GET'])
def getFromQuery():
    query = request.args.get('query')
    return f'{query}'

@endpoints.route('/get-even-number', methods=['GET'])
def getEvenNumber():
    return f'{random.randrange(0, 41) * 2}, EnvNameSample value: {os.getenv('EnvNameSample')}'

@endpoints.route('/get-odd-number', methods=['GET'])
def getOddNumber():
    return f'{random.randrange(1, 41, 2) * 2.5 }, EnvNameSample value: {os.getenv('EnvNameSample')}'

@endpoints.route('/get-env-value', methods=['GET'])
def getEnvVariable():
    return f'{os.getenv('EnvNameSample')}'