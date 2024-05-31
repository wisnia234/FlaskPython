from flask import Blueprint
import random

endpoints = Blueprint('endpoints', __name__)

@endpoints.route('/get-item')
def getRandomNumber():
    return f"{random.random()}"

@endpoints.route('/get-author-name')
def getAuthorName():
    return "<h1>Michal Wisniewski</h1>"