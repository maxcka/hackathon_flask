from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    title = 'My Flask App'
    name = 'Home'
    return render_template('home.html', title=title, name=name)
    
@app.route('/events')
def events():
    title = 'Events'
    name = 'Events'
    return render_template('events.html', title=title, name=name)

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
    location = request.form['location']
    date = request.form['date']
    time = request.form['time']
    description = request.form['description']

    if not date or not time:
        error = "Please Fill Out All Fields!"
        prev_title = "Create Event"
        prev_name = prev_title
        return render_template('create.html', title=prev_title, name=name, error=error)

    #new_event = FUNCTION(title=title, location=location,\
    #                    date=date, time=time, description=description)
    #db.session.add(new_event)
    #db.session.commit()

    # redirect after submission
    return render_template('thanks.html', title=title, location=location, date=date, time=time)


if __name__ == '__main__':
    app.run()
