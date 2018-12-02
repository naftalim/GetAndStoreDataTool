import my_helpers
from datafeed import datafeedfactory

def processDataFeeds():
    conn = my_helpers.getDbConnection()
    feedFactory = datafeedfactory.DataFeedFactory()
    for feed in feedFactory.getFeeds():
        feed.log("getDataStart ")
        feed.getData()
        feed.log("getDataEnd ")
        feed.log("PopulateDBStart ")
        feed.populateDB(conn)
        conn.commit()
        feed.log("PopulateDBEnd ")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    processDataFeeds()    
