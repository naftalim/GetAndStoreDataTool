from datafeed import datafeeds 
class DataFeedFactory(object):
    feeds = []
    def __init__(self):
        #To Add a Feed to the Factory for processing, create child class of DataFeed
        #implement getDate and populateDB methods
        #instantiate class here, and append it to the 'feeds' list, below.
        game_teamStatsPerGameFeed = datafeeds.Game_TeamStatsPerGameFeed()
        self.feeds.append(game_teamStatsPerGameFeed)
        playerFeed = datafeeds.PlayerFeed()
        self.feeds.append(playerFeed)
        playerStatsPerGameFeed = datafeeds.PlayerStatsPerGameFeed()
        self.feeds.append(playerStatsPerGameFeed)
       
    def getFeeds(self):
        return iter(self.feeds)

