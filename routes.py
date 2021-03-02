from flask import Blueprint, render_template, request, redirect
from .generator import ai #will have class AI in generator.py which instantiates an object called ai
import re

# Flask uses concept of Blueprint for making application components,
# and supporting common patterns within app or accross apps
# can greatly simplify how large applications work
generator = Blueprint('generator', __name__)

@generator.route('/')
def index():
    return render_template('index.html', parameter="") #will search inside of templates folder and return correct file we require
    # can access parameter inside of html file
    # can do opposite, put parameter = request.form('parameter') inside our index function to have html access stuff from this file

@generator.route('/analyze', methods=['POST'])
def analyze():
    ctx = request.form['context']
    #ctx = request.form['context']
    qst = request.form['question']
    ans = '[ANSWER]:'
    prefix = '<|startoftext|>\n[CONTEXT]: ' + ctx + '\n[QUESTION]:' + qst + '\n' + ans #+ "\'"
    text = ai.generate_text(prefix)
    text = re.sub('[!\'\]\[\,]', '', text) #getting rid of any extra symbols
    print("Please wait...")

    return render_template('index.html', text=text) #text is response that ai generates
