import pymongo
import json

# Define variables
data = './data/chargePoints.json'
dbPortNumber = '27017'    # --> Confirm with mongod.log 'waiting for connections on port 27017'

# Read the json file and assign it to a variable
with open(data, mode = 'r') as jsonFile:
    jsonData = json.load(jsonFile)

# Print the items in the json data
for item in jsonData:
    print(item)
# Result:
# Scheme
# ChargeDevice    --> Obviously, this is what we are going to populate the MongoDB with

# Create a client to connect to host/server DB
mongoClient = pymongo.MongoClient(f'mongodb://localhost:{dbPortNumber}')
# Create database if it doesn't exist. Same object can be used for connecting to an existing database.
chargePointsDB = mongoClient['chargePointsDB']
# Create collection/table in the database.
chargePointsCollections = chargePointsDB['chargePointsCollections']
# Populate the charge points data in the table
for chargePoint in jsonData['ChargeDevice']:
    chargePoint['_id'] = chargePoint['ChargeDeviceId']    # We need to assign a unique ID, unless we want MongoDB does for us.
    insertProcess = chargePointsCollections.insert_one(chargePoint)


print(chargePointsDB.list_collection_names())
x = chargePointsDB.drop_collection('chargePointsCollections')
