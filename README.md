# GetAndStoreDataTool

process data feeds. get data from somewhere/somehow and store data somewhere/somehow

* a controller function gets a collection of datafeed objects from a datafeedFactory object
* controller iterates through the collection and calls a getData and populateDB method on each datafeed object

a datafeed is a class that inherits from a baseDataFeed class which defines a logging method and also a instance map for the instances 
maintain state between thier getData and PopulateDB method calls. 

#### to add datafeed
* define a datafeed class 
* implement your custom get data and poplulate db methods
* register class with the datafeedfactory 

#### register datafeed with factory
* simply instantiate the class and append it the collection that's returned by the factory's getDataFeeds method

# Todo
Lot's, I wrote this code to deal with data for a particular project and realized only later that the pattern was general enought for tool

## Generalize the data storage srategy (will get to it when I need this)
* getData is appropriately generalized in that it makes no assumptions about where and how your feed will get data (this is because my application, itself, contained this ambiguity
* populate DB is not generlized, in that the methods receive a db connection from the controller, I did this because all my datafeeds where being stored in an SQL DB and I wanted a straightforward place of authority for managing that connection, for this to be a tool, the controller cannot make any assumptions about how and where a feed will store its data

## refactor JSON based feed classes into subclasses of a more general jsonDataFeed class that handles the common functionality

## refactor Excel based feed classes into subclasses of a more general ExcelDataFeed class that handles the common functionality

## Logging
I used this as command line based tool, and the basic printing to standard out worked for me, this is too crude from a production server based type scenario

## Error handling
THERE IS NONE! {blush}
See above for the logging, same explaination

## More efficient handlig of postgres inserts
right now it's iterating though the data and inserting records, the python postgres driver provides a coupld of faster methods where basically I'd iterate build up a string and insert one time using one of these methods to avoid the unneeded trips.

