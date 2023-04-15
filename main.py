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
#from flask import Flask
#
#app = Flask(__name__)
#
#@app.route("/")
#def hello_world():
#    return "<p>Hello, World!</p>"
#
#@app.route("/search")
#def search(request):
#    locations = request.args.get('location')
#    if (locations == None):
#        locations = ["The Hill", "Campus", "Off-Campus", "Bruinwalk"]
#    types = request.args.get('type')
#    if (types == None):
#        types= ["Social Event", "Club Event", "Fundraiser", "Free Food", "Other"]
#    
#    from datetime import date, timedelta, time
#    startDate = request.args.get('startDate')
#    if(startDate == None):
#        startDate = date.today()
#    endDate = request.args.get('endDate')
#    if(endDate == None):
#        endDate = startDate + timedelta(days=10)
#    delta = timedelta(days=1)
#    dates = []
#    while startDate <=endDate:
#        dates.append(startDate)
#        startDate += delta
#
#    #startTime = request.args.get('startTime')
#    #if(startTime == None):
#    #    startTime = datetime.time(0,0,0)
#    # endTime = request.args.get('endTime')
#    # if(endTime == None):
#    #     endTime = datetime.time(23,59,59)
#
#    events = [] #list of json items - needs to be edited once database has been created
#    filtered = []
#    for event in events:
#        if (event.location in locations and event.type in types and event.date in dates):
#            filtered.append(event)
#    return filtered

