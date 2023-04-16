import db
from datetime import datetime

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
 #   print(db.query('SELECT %s, %s FROM team10.events', ['event_name', event]))