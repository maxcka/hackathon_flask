from flask import Flask
from db import query

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/dbs")
def dbs():
    return query("select * from team10.events")



@app.route("/search")
def search(request):
    locations = request.args.get('location')
    if (locations == None):
        locations = ["The Hill", "Campus", "Off-Campus", "Bruinwalk"]
    types = request.args.get('type')
    if (types == None):
        types= ["Social Event", "Club Event", "Fundraiser", "Free Food", "Other"]
    
    from datetime import date, timedelta, time
    startDate = request.args.get('startDate')
    if(startDate == None):
        startDate = date.today()
    endDate = request.args.get('endDate')
    if(endDate == None):
        endDate = startDate + timedelta(days=10)
    delta = timedelta(days=1)
    dates = []
    while startDate <=endDate:
        dates.append(startDate)
        startDate += delta

    #startTime = request.args.get('startTime')
    #if(startTime == None):
    #    startTime = datetime.time(0,0,0)
    # endTime = request.args.get('endTime')
    # if(endTime == None):
    #     endTime = datetime.time(23,59,59)

    events = [] #list of json items - needs to be edited once database has been created
    filtered = []
    for event in events:
        if (event.location in locations and event.type in types and event.date in dates):
            filtered.append(event)
    return filtered

