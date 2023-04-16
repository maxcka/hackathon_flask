import db
from datetime import datetime
import json

from db import query

class Event:
    def __init__(self, loc, type, date, time, name, host):
        self.loc = loc
        self.type = type
        self.date = date
        self.time = time
        self.name = name
        self.host = host
    
    def toJSON(self):
        return "{}"


def addEvent(e_location, e_type: str, e_date: str, e_time: str, e_name, e_host):
    e_datetime = e_date + e_time
    #date_object = datetime.strptime(e_date, "%m ")
    return db.query(
        """
        insert into team10.events 
            (event_location, event_type, event_date, event_name, event_host) 
        values (%s, %s, %s, %s, %s)
        """,
        [e_location, e_type, e_date, e_name, e_host]
    )

def getEvents():
    events =  query("select * from team10.events").fetchall()
    
    print("Hello")

    events_list = []

    for event in events:
        events_list.append({
            "name": event[4],
            "loc": event[1],

        })
        # print(*event)
        # temp_event = Event(*event)
        # events_list.append(temp_event)

    return events_list

 #   print(db.query('SELECT %s, %s FROM team10.events', ['event_name', event]))