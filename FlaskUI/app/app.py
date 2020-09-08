from flask import Flask, render_template
import json # py library

file = open('/Users/Julian/Documents/GitHub/BayAreaHax/FlaskUI/app/repData.json', 'r')
dic = json.load(file)
def getTop(n):
    result = []
    sort = sorted(dic.items(), key = lambda rep: rep[1]['Score'], reverse=True)
    for i in range(n):
        result.append(sort[i][1])
    return(result)

app = Flask(__name__)

app.config.from_object('config.Config')

@app.route('/')
@app.route('/index/')
def home():
	return render_template('index.html')

@app.route('/dashboard/')
def dashboard():
	return render_template('dashboard.html', data=getTop(5))

@app.route('/choose_campaign/')
def choose_campaign():
	return render_template('choose_campaign.html')


@app.route('/contacts/')
def contacts():
	return render_template('contacts.html', data=getTop(159))

@app.route('/login/')
def login():
	return render_template('login.html')


if __name__ == "__main__":
	app.run(host='localhost', port=app.config['PORT'], debug=app.config['DEBUG'])