# Author - Shivdeep Singh
# Date 26-05-2022


import pymongo
import pprint
import json
import warnings
warnings.filterwarnings('ignore')

# connect to the mongoclient
client = pymongo.MongoClient('mongodb://localhost:27017')

# get the database
database = client['sample_db']

# creating two sample collections cities and roads

database.create_collection("cities")

database.create_collection("roads")

# Adding sample data to city from city.json file

cities_collection = database.get_collection("cities")

# open the cities json file
with open("cities.json") as f:
    file_data = json.load(f)

# insert the data into the collection
cities_collection.insert_many(file_data)


# Quering cities that are not equal to name hello
# Check cities.json file for refrence
# it should return two values

result_1 = cities_collection.find({
    "name" : { "$ne" : "hello"}
})

# all the entries which dont have name hello are returned
# id and name is returned read the cities.json file for refrence


# going through all the values and returning
for i in result_1:
    print(i)

