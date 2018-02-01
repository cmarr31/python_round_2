from flask import Flask, render_template, request, redirect, session
from random import *
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'your_gold' not in session:
        session['your_gold'] = 0
        session['activity'] = []
    return render_template("index.html", your_gold = session['your_gold'], activity = session['activity'])

@app.route('/process_money', methods=['POST'])
def process():
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    print time
    building = request.form['building']
    if building == 'farm':
        gold = randint(10,20)
        session['your_gold'] += gold
        session['activity'] = 'You entered a ' + building + ' and earned ' + str(gold) + ' gold.' + ' ' + str(time)
    elif building == 'cave':
        gold = randint(5,10)
        session['your_gold'] += gold
        session['activity'] = 'You entered a ' + building + ' and earned ' + str(gold) + ' gold.' + ' ' + str(time)
    elif building == 'house':
        gold = randint(2,5)
        session['your_gold'] += gold
        session['activity'] = 'You entered a ' + building + ' and earned ' + str(gold) + ' gold.' + ' ' + str(time)
    elif building == 'casino':
        gain_lose = randint(0,1)
        gold = randint(0,50)
        if gain_lose == 0:
            session['your_gold'] += gold
            session['activity'] = 'You entered a ' + building + ' and earned ' + str(gold) + ' gold.' + ' ' + str(time)
        else:
            session['your_gold'] -= gold
            session['activity'] = 'You entered a ' + building + ' and lost ' + str(gold) + ' gold.' + ' ' + str(time)
    return redirect('/')

app.run(debug=True)