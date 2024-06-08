from flask import Blueprint
from flask import request
import archiveItems
import random

endpoints = Blueprint('endpoints', __name__)

@endpoints.route('/get-item')
def getRandomNumber():
    item = random.random()
    archiveItems.writeItem(item)

    return f'{item}'

@endpoints.route('/get-author-name')
def getAuthorName():
    return "<h1>Michal Wisniewski</h1>"

@endpoints.route('/get-from-query', methods=['GET'])
def getFromQuery():
    query = request.args.get('query')
    return f'{query}'