# Connect to Mongo Cluster
# Connect to Mongo DB
#  Insert => insert_one, Insert_many, nested insert
#  Select => Find, Find_one, fnd with filter, projection, find with sort
#  Delete
# pip install pymongo



from pymongo import MongoClient

mongo_cluster = "mongodb+srv://saikumarvada23:Saikumar143@resumestore.arpzpqu.mongodb.net/?retryWrites=true&w=majority&appName=Resumestore"
database_name = "test_db"
collection = "people"
client = MongoClient(mongo_cluster) # conect to Mango Cluster

database = client[database_name] # Get access to Database

people_collection = database[collection]

# ******************************************* Insert ***********************************************
# insert_one_statement = {"name": "Mohan", "age":25, "city": "hyderabad", "pin_code":500045}
# insert_one_statement = {"name": "Vonna", "age":25, "city": "hyderabad", "designation": "Agentic AI Dev", "pin_code":500045}
# insert_one_statement = {"first_name": "Veenitha", "Top_Skill": "Java, C#, Python"}
# insert_one_statement = {"Hellow": "World"}
# people_collection.insert_one(insert_one_statement)

#********************************** Bulk Insert - Insert many ********************************************************
# people_collection.insert_many(
#     [
#         {"name" :"Ganga", "designation" :"Agentic AI Developer", "Salary":60000 , "doj":"05/5/2025"},
#         {"name" :"haridev", "designation" :"Agentic AI Developer", "Salary":50000 , "doj":"05/5/2025"},
#         {"name" :"saides", "designation" :"Agentic AI Developer", "Salary":45000, "doj":"05/5/2025"},
#         {"name" :"Mohan gandhi", "designation" :"Agentic AI Developer", "Salary":75000 , "doj":"05/5/2025"},
#         {"name" :"Abhinayasri", "designation" :"Agentic AI Developer", "Salary":30000 , "doj":"05/5/2025"},
#         {"name" :"Abhinay", "designation" :"Java Developer", "Salary":50000, "doj":"05/5/2025"},
#     ]
# )


#************************************** Nested Insert ********************************************************

# people_collection.insert_one(
#     {
#         "name": "Mohan Sai",
#         "City": "Hyderabad",
#         "Salary": 50000,
#         "address": {"street": "Hitechcity road", "lane":"3rd lane ", "pin_code":500045}
#     }
# )

# #********************************************* Find All *********************************************************

# for document in people_collection.find():
#     print (document)
    
# #********************************************** Find One **********************************************************

# document = people_collection.find_one()
# print (document)



# #************************************************ Find One - Filter **********************************************
# document = people_collection.find ({
#     "name": "Mohan sai ",
#     "Salary" : 50000,
# })


# for doc in document:
#     print (doc)



# people_collection.find({
#     "Salary": {"$gt": 50000}
# })

# for document in document:
#     print(document)


# #********************************************** Find One - Sort ****************************************************
# document=  people_collection.find ().sort("Salary", -1).limit(2)

# documents = people_collection.find (
#     {
#        "_id": 0, "name": 1, "designation": 2,"Salary": 3 
#     }
# )

# for document in document:
#     print(document)


# #************************************ Find one - Start with **********************************************************

# people_collection.find({
#     "name": {"$gt": "^M" }
# })

# for doc in document :
#      print(doc)
    
# #*************************************** Delete ***************************************************************************

people_collection.delete_one({
    "name": "Mohan Sai"
})



