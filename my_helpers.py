import requests, psycopg2, datetime, private


def nullToZero(value):
    if value == '': 
        return 0
    return value

def filterListOfDicts(lod, key, value):
    for d in lod:
        if d[key] != value:
            continue
        yield d

def getMonthDayYear(DaysFromNow):
    t = datetime.datetime.now() + datetime.timedelta(DaysFromNow)
    s = t.strftime("%m-%d-%Y")
    return s

def getDbConnection(autoCommitParam=False): 
    conn = psycopg2.connect(private.CONNECTION_STRING)
    conn.set_session(autocommit=autoCommitParam)
    return conn

