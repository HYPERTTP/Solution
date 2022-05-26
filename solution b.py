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


database.create_collection("roads")

# Adding sample data to city from city.json file

roads_collection = database.get_collection("roads")

# open the cities json file
with open("roads.json") as f:
    file_data = json.load(f)

# insert the data into the collection
roads_collection.insert_many(file_data)


# Quering roads that have length greater than
# Check roads.json file for refrence
# it should return two values

result_2 = roads_collection.find({
    "length" : {"$gt" : "0.00"}

})



# going through all the values and returning
for i in result_2:
    print(i)

print(result_2)


# This result 2 canbe used to create a graph then that graph canbe used in C and D

