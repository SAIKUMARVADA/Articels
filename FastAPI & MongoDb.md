#  FastAPI + 🍃 MongoDB 

## Section-1 Introduction to FastAPI
* A Modern Web Framework for Python

In the ever-evolving world of web development, FastAPI has quickly become one of the most loved and fastest-growing Python frameworks. Designed for building high-performance APIs, FastAPI combines simplicity, power, and modern Python features to deliver an outstanding developer experience.

##  What is FastAPI?
* FastAPI is a modern, high-performance web framework for building RESTful APIs with Python 3.7+ based on type hints.

   ✅ Created by Sebastián Ramírez
   
   ✅ Built on Starlette for web handling and Pydantic for data validation
   
   ✅ Supports asynchronous programming using async/await

## Section-2 Key Features of FastAPI

### 1. High Performance
* Built on Starlette and Pydantic

* Asynchronous support using async/await

* One of the fastest Python frameworks, rivaling Node.js and Go

###  2. Automatic Interactive API Docs
* FastAPI automatically generates two types of documentation:

    * Swagger UI: /docs

    * ReDoc: /redoc

* Helps in testing and understanding the API without extra tools

###  3. Data Validation and Serialization
* Uses Pydantic models for:

    * Input validation

    * Output formatting

* Validates data before it reaches your code

```python

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```
---

###  4. Async Support
* Built with asyncio, supports async def for concurrent I/O operations

* Perfect for modern use-cases like real-time apps, background tasks, etc.

```python

@app.get("/users")
async def get_users():
    return await fetch_users_from_db()
```
---

### 5. Dependency Injection System
* Built-in support for injecting dependencies like DB sessions, auth, etc.

```python

from fastapi import Depends

def get_db():
    db = connect_db()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
def read_items(db = Depends(get_db)):
    return db.query_items()

```
---

###  6. Type Hints = Fewer Bugs
* Leverages Python type hints for:

    * Data validation

    * Auto-generated documentation

    * Editor support (auto-complete, linting)

###  7. Built-in OAuth2, JWT, and Security Utilities
* Easily handle user authentication, token generation, and permission handling

### 8. Request and Response Models
* Use models to control how data enters and leaves your API

* Supports JSON and other media types

### 9. Path, Query, and Body Parameter Handling
* Automatically handles:

    * Path params: /users/{id}

    * Query params: /users?name=Sai

    * Body params: JSON input

###  10. Testability
* Compatible with Pytest, and you can easily test endpoints using TestClient

```python

from fastapi.testclient import TestClient
client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
```
---

###  11. Extensible and Modular
* Easily split code into routers, services, and models

* Great for microservices or modular design

## Section-3  Example: Simple Inventory API with FastAPI
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

## Section-1  What is MongoDB?
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

## Section-3  Prerequisites
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

##  View the data in MongoDB Compass under:

* Database: test_db
* Collection: people

## ▶ How to Run
* Save the code in a file named mongo_examples.py.

* Open the terminal and navigate to the directory.

*cd C:\Temp-1 python mongo_examples.py*

Open MongoDB Compass, connect using your connection string.

Check if test_db > people collection is visible.

View inserted data. 

## Section-5  Key Terminology

| Term       | Meaning                                                         |
| ---------- | --------------------------------------------------------------- |
| Document   | A JSON-like object (e.g., `{ "name": "Sai", "age": 25 }`)       |
| Collection | A group of related documents (like a table in SQL)              |
| Database   | A container for collections (like a database in SQL)            |
| BSON       | A binary representation of JSON used by MongoDB for performance |
| ObjectId   | Unique identifier generated for every document                  |


## Basic Commands (Mongo Shell / Compass)

### 1. Connect to MongoDB
If using the MongoDB Shell:

```bash

mongo
If you're connecting to a remote server:

bash

mongo "mongodb+srv://<username>:<password>@cluster0.mongodb.net/test"
```
---
###  2. Show Databases
```js

show dbs
```
---
###  3. Use a Database
```js
use myDatabase
```
---
###  4. Show Collections (Tables)
```js
show collections
```
---
### 5. Create or Insert Data into Collection
```js
db.users.insertOne({ name: "Sai", age: 25, city: "Hyderabad" })
```
---
```js

db.users.insertMany([
  { name: "Kiran", age: 27 },
  { name: "Anu", age: 23 }
])
```
---
### 6. Find Documents
* Find all:

```js

db.users.find()
```
---
* Find with condition:

```js

db.users.find({ age: 25 })
```
---
### 7. Update Documents
* Update one:

```js

db.users.updateOne({ name: "Sai" }, { $set: { age: 26 } })
```
---
* Update many:

```js

db.users.updateMany({ city: "Hyderabad" }, { $set: { country: "India" } })
```
---
### 8. Delete Documents
* Delete one:

```js

db.users.deleteOne({ name: "Kiran" })
```
---
* Delete many:

```js

db.users.deleteMany({ city: "Hyderabad" })
```
---
### 9. Drop Collection
```js

db.users.drop()
```
---
### 10. Drop Database
```js

db.dropDatabase()
```
---
### 11. Count Documents
```js

db.users.countDocuments()
```
---
###  12. Sort and Limit
* Sort by age:

```js

db.users.find().sort({ age: 1 }) // Ascending
```
---
* Limit results:

```js

db.users.find().limit(5)
```
---
### 13. Create Index
```js

db.users.createIndex({ name: 1 }) // 1 = ascending, -1 = descending
```
---
### 14. Aggregation Example
```js

db.users.aggregate([
  { $match: { city: "Hyderabad" } },
  { $group: { _id: "$city", total: { $sum: 1 } } }
])
```
---


## 📈 MongoDB vs SQL

| Feature       | MongoDB                 | SQL (e.g., MySQL)       |
| ------------- | ----------------------- | ----------------------- |
| Schema        | Flexible                | Fixed, predefined       |
| Data Format   | JSON-like (BSON)        | Rows & columns          |
| Relationships | Manual (via references) | Built-in (foreign keys) |
| Performance   | Faster for large data   | Depends on structure    |


## Section-6 FastAPI Questions

* 1 What is FastAPI and who created it?
* 2 What are the core advantages of FastAPI over Flask or Django?
* 3 Explain how FastAPI supports asynchronous programming.
* 4 What is Pydantic and how does FastAPI use it?
* 5 What is the role of BaseModel in FastAPI?
* 6 How does FastAPI generate automatic API documentation?
* 7 What is the difference between @app.get() and @app.post() in FastAPI?
* 8 How do you define path, query, and request body parameters in FastAPI?
* 9 What is dependency injection in FastAPI and how does it work?
* 10 How do you handle exceptions and custom error messages in FastAPI?
* 11 How do you write asynchronous routes using async def in FastAPI?
* 12 How do you test FastAPI applications?
* 13 What are the key components of a typical FastAPI project structure?
* 14 How do you implement authentication (e.g., JWT) in FastAPI?
* 15 What are Background Tasks in FastAPI and how are they used?
* 16 What is CORS and how do you configure it in FastAPI?

## MongoDB Questions

* 1 What is MongoDB and how does it differ from SQL databases?
* 2 What are documents and collections in MongoDB?
* 3 What is MongoDB Compass and how is it used?
* 4 What is MongoDB Atlas?
* 5 What Python library do we use to connect MongoDB?
* 6 How do you connect FastAPI with MongoDB?
* 7 What is motor and why is it used with FastAPI?
* 8 How do you insert a Pydantic model into MongoDB in FastAPI?
* 9 How do you convert MongoDB ObjectId to a JSON serializable format?
* 10 How do you update MongoDB documents using FastAPI?
* 11 How do you handle MongoDB connection errors in FastAPI?
* 12 How do you structure a FastAPI project that uses MongoDB?
* 13 How do you use dependency injection to manage MongoDB client in FastAPI?
* 14 How do you ensure data uniqueness (like email) in MongoDB using FastAPI?
* 15 How do you serialize MongoDB query results before returning them in FastAPI?
