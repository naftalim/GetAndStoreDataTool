# GetAndStoreDataTool

process data feeds. get data from somewhere/somehow and store data somewhere/somehow

* a controller function gets a collection of datafeed objects from a datafeedFactory object
* controller iterates through the collection and calls a getData and populateDB method on each datafeed object

a datafeed is a class that inherits from a baseDataFeed class. a datafeed class implemnents its own getData and populateDB methods. the baseDataFeed class defines a logging method and a instance map for the instances to 
maintain state between thier getData and populateDB method calls. 

#### to add datafeed
* define a datafeed class 
* implement your custom getData and poplulateDB methods
* register class with the datafeedfactory 

#### register datafeed with factory
* simply instantiate the class and append it the collection that's returned by the factory's getDataFeeds method

# TODO
Lot's, I wrote this code to deal with data for a particular project and realized only later that the pattern was general enough for a tool

## Generalize the data storage srategy (will get to it when I need this)
* getData is appropriately generalized in that it makes no assumptions about where and how your feed will get data (this is because my application, itself, contained this ambiguity)
* populateDB is not generlized in that the methods receive a db connection from the controller who manages getting the conn and the commit. I did this because all my datafeeds where being stored in an SQL DB and I wanted a straightforward place of authority for managing those connections, but for this to be a general tool, the controller cannot make any assumptions about how and where a feed will store its data.

## datafeedFactory 
* better registration strategy, instantiating datafeeds and appending them to the returned collection may not be the best way forward, see next item
*  add support for different sets of datafeeds, maybe by supporting different implementations of datafeedFactory classes

## refactor JSON based feed classes into subclasses of a more general jsonDataFeed class that handles the common functionality

## refactor Excel based feed classes into subclasses of a more general ExcelDataFeed class that handles the common functionality

## Logging
I used this as command line tool, and the basic printing to standard out worked for me, this is too crude for a production server based type scenario

## Error handling
THERE IS NONE! {blush}
See above for the logging, same explaination

## More efficient handling of postgres inserts on the datafeeds 
right now it's iterating though the data and inserting records. the python postgres driver provides a couple of faster methods, where basically I'd iterate the data, build up a string, and on completion, insert everythig at one time, using one of these methods to avoid the unneeded back and forth trips. this should make things faster at the expense of mainting more data in memory. Right now, neither are bottlenecks. 

