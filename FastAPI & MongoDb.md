#  FastAPI + 🍃 MongoDB 

## Section-1 Introduction to FastAPI
A Modern Web Framework for Python

In the ever-evolving world of web development, FastAPI has quickly become one of the most loved and fastest-growing Python frameworks. Designed for building high-performance APIs, FastAPI combines simplicity, power, and modern Python features to deliver an outstanding developer experience.

## 🔍 What is FastAPI?
FastAPI is a modern, high-performance web framework for building RESTful APIs with Python 3.7+ based on type hints.

✅ Created by Sebastián Ramírez

✅ Built on Starlette for web handling and Pydantic for data validation

✅ Supports asynchronous programming using async/await

## Section-2⚡ Key Features of FastAPI

### Blazing Fast:
Among the fastest Python frameworks—comparable to Node.js and Go.

### Automatic Documentation:
Generates Swagger UI and ReDoc docs at /docs and /redoc.

### Data Validation:
Uses Pydantic to validate request data and define schemas.

### Async Support:
Native support for async operations makes it ideal for performance-heavy apps.

### Developer Friendly:
Minimal setup, readable code, and amazing community support.

## Section-3 💡 Example: Simple Inventory API with FastAPI
### ✅ Step 1: Install Dependencies
```bash

pip install fastapi
pip install uvicorn
```
### ✅ Step 2: Create main.py
```python

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str = None

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

```

---

### ✅ Step 3: Run the Server
```bash

uvicorn main:app --reload
```
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

## Section-4 Core Concepts in FastAPI

| Concept              | Description                               |
| -------------------- | ----------------------------------------- |
| Path Parameters      | Dynamic data in URL paths                 |
| Query Parameters     | Filters or modifiers in the query string  |
| Request Body         | Uses Pydantic models for structured input |
| Response Models      | Clean output with auto-formatting         |
| Dependency Injection | For DB, authentication, etc.              |

# 🍃 MongoDB

## Section-1 🔍 What is MongoDB?
MongoDB is a NoSQL document database, built for flexibility and scalability. Instead of tables (SQL), MongoDB uses:

* Document → JSON Object

* Collection → Table Equivalent

It is widely used in modern backend development due to its support for unstructured data and ease of scaling.

## Section-2 FastAPI + MongoDB Integration
### 🛠️ Project Workflow
* Set up FastAPI project

* Connect MongoDB (Atlas or Local)

* Create APIs to insert/retrieve data

* Run server and test using Postman or browser

## Section-3 📋 Prerequisites
### Make sure the following tools are installed:

* Python 3.8+
* MongoDB (Local or Cloud Atlas)
* VS Code or any IDE
* Postman
* MongoDB Compass (GUI for MongoDB)

## 🔌 Install Required Packages

```bash

pip install fastapi uvicorn pymongo pydantic motor
```
### Section-4 Connect FastAPI with MongoDB
## ✅ Sample MongoDB Connection Code (mongo_examples.py)

```python

from pymongo import MongoClient

mongo_cluster = "mongodb+srv://<username>:<password>@resumestore.arpzpqu.mongodb.net/?retryWrites=true&w=majority&appName=Resumestore"
database_name = "test_db"
collection_name = "people"

client = MongoClient(mongo_cluster)
database = client[database_name]
people_collection = database[collection_name]

--------- Bulk Insert - Insert many employee records ----------


people_collection.insert_many([
    {"name": "Ganga", "designation": "Agentic AI Developer", "Salary": 60000, "doj": "2025-05-05"},
    {"name": "Haridev", "designation": "Agentic AI Developer", "Salary": 50000, "doj": "2025-05-05"},
    {"name": "Saides", "designation": "Agentic AI Developer", "Salary": 45000, "doj": "2025-05-05"},
    {"name": "Mohan Gandhi", "designation": "Agentic AI Developer", "Salary": 75000, "doj": "2025-05-05"},
    {"name": "Abhinayasri", "designation": "Agentic AI Developer", "Salary": 30000, "doj": "2025-05-05"},
    {"name": "Abhinay", "designation": "Java Developer", "Salary": 50000, "doj": "2025-05-05"},
])


```

---

## 📊 View the data in MongoDB Compass under:

* Database: test_db
* Collection: people

## ▶️ How to Run
* Save the code in a file named mongo_examples.py.

* Open the terminal and navigate to the directory.

*cd C:\Temp-1 python mongo_examples.py*

Open MongoDB Compass, connect using your connection string.

Check if test_db > people collection is visible.

View inserted data. 

## Section-5 📌 Key Terminology

| Term       | Meaning                                                         |
| ---------- | --------------------------------------------------------------- |
| Document   | A JSON-like object (e.g., `{ "name": "Sai", "age": 25 }`)       |
| Collection | A group of related documents (like a table in SQL)              |
| Database   | A container for collections (like a database in SQL)            |
| BSON       | A binary representation of JSON used by MongoDB for performance |
| ObjectId   | Unique identifier generated for every document                  |


## Basic Commands (Mongo Shell / Compass)
* show dbs                         # Show all databases
* use test_db                      # Switch to a database
* db.createCollection("people")    # Create a collection
* db.people.insertOne({name: "Sai", age: 25})    # Insert document
* db.people.find()                 # Retrieve all documents

## 📈 MongoDB vs SQL

| Feature       | MongoDB                 | SQL (e.g., MySQL)       |
| ------------- | ----------------------- | ----------------------- |
| Schema        | Flexible                | Fixed, predefined       |
| Data Format   | JSON-like (BSON)        | Rows & columns          |
| Relationships | Manual (via references) | Built-in (foreign keys) |
| Performance   | Faster for large data   | Depends on structure    |


## Section-6 FastAPI Questions

What is FastAPI and who created it?

What are the core advantages of FastAPI over Flask or Django?

Explain how FastAPI supports asynchronous programming.

What is Pydantic and how does FastAPI use it?

What is the role of BaseModel in FastAPI?

## MongoDB Questions

What is MongoDB and how does it differ from SQL databases?

What are documents and collections in MongoDB?

What is MongoDB Compass and how is it used?

What is MongoDB Atlas?

What Python library do we use to connect MongoDB?

