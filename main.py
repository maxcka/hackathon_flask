from flask import Flask, render_template, request
from db import query
from models.events import addEvent, getEvents

app = Flask(__name__)


@app.route("/dbs")
def dbs():
    return getEvents()
    return query("select * from team10.events").fetchall()

@app.route("/view_events")
def viewEvents():
    return query("select * from team10.events").fetchall()

@app.route('/')
def index():
    title = 'My Flask App'
    name = 'Home'
    return render_template('home.html', title=title, name=name)

@app.route('/filter_by_date', methods=['GET'])
def filter_by_date():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    filtered_data = query.filter(MyModel.date >= start_date, MyModel.date <= end_date).all()
    return render_template('events.html', data=data)


@app.route('/events')
def events():
    title = 'Events'
    name = 'Events'
    events_list = getEvents()
    return render_template('events.html', title=title, name=name, events_list = events_list)

@app.route('/search')
def search():
    title = 'Search Results'
    name = 'Search Results'
    query = request.args.get('query')
    return render_template('search.html', title=title, name=name, query=query)

@app.route('/create')
def create():
    title = 'Create Event'
    name = 'Create Event'
    return render_template('create.html', title=title, name=name, error=False)


@app.route('/process_event', methods=['POST'])
def process_event():
    title = request.form['title']
    event_type = request.form['type']
    host = request.form['host']
    location = request.form['location']
    date = request.form['date']
    time = request.form['time']
    description = request.form['description']

    if not date or not time:
        error = "Please Fill Out All Fields!"
        prev_title = "Create Event"
        prev_name = prev_title
        return render_template('create.html', title=prev_title, name=name, error=error)

    new_event = addEvent(location, description, date, time, title, "Ucla")
    #db.session.add(new_event)
    #db.session.commit()

    # redirect after submission
    return render_template('thanks.html', title=title, location=location, date=date, time=time)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/create_account")
def create_account():
    return render_template("createacc.html")


if __name__ == '__main__':
    app.run()
