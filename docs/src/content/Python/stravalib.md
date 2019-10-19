Title: Interfacing with Strava API using stavalib
Date: 2017-08-12 16:08
Authors: José Aniceto
Modified: 2017-08-13 19:54

### Instalation:
`$ pip install stravalib`

### Usage:

```python
from stravalib import Client

client = Client(access_token='fgd456fgs5dgs546dfg')
athlete = client.get_athlete()  # Get your athlete profile
athlete2 = client.get_athlete(227615)  # By providing an athlete ID you can access other people
```

To get a given activity, use the get_activity function and provide activity_id:
```python
activity = client.get_activity(207650614)

# Activity object has many basic properties such as type and distance.
print("type={0.type} distance={1} km".format(activity, unithelper.kilometers(activity.distance)))
```

Activity information:
```python
# Activities can have many streams, you can request desired stream types
types = ['time', 'latlng', 'altitude', 'heartrate', 'temp', ]

streams = client.get_activity_streams(123, types=types, resolution='medium')

#  Result is a dictionary object.  The dict's key are the stream type.
if 'altitude' in streams.keys():
    print(streams['altitude'].data)
```

List of Activities:
```python
for activity in client.get_activities(after = "2010-01-01T00:00:00Z",  limit=5):  # To get newest to oldest use before argument.
    print("{0.name} {0.moving_time}".format(activity))
```

##### Official documentation
* [Strava API Docs](http://strava.github.io/api/)
* [stravalib Docs](http://pythonhosted.org/stravalib/index.html)
