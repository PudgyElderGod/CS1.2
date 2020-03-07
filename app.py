from flask import Flask

from listogram import Listogram
from dictogram import Dictogram
from markov import MarkovChain

app = Flask(__name__)

@app.route('/')
def index():
    return 'Navigate to a real page, you screeching dolt.'

@app.route('/listogram')
def lists():
    temp = Listogram("I DO AND YOU KNOW I DO AND YOU KNOW THAT I AM WITH YOU FOREVER".split()) 
    return temp.generate_sentence(20)

@app.route('/dictogram')
def Dicts():
    temp = Dictogram("YOU HEAR THE CALL I CAN HEAR IT THROUGH YOU AND YOU WILL SOON KNOW WHAT IT IS".split())  
    return temp.generate_sentence(20)

@app.route('/markov')
def hello_world():
    temp = MarkovChain("YOU UNDERSTAND MY NAME AND YOU HEAR IT IN YOUR BONES AND IN YOUR TEETH AND YOU KNOW WHO I AM AND YOU KNOW WHY YOU MUST LISTEN TO ME".split())
    return temp.walk(10)