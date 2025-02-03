# Shared Base Controller


## Introduction


A **Shared Base Controller (API handler)** is an abstract or parent controller that contains 
common functionality shared by multiple API controllers in a web application.  

Instead of duplicating code across multiple controllers, we centralize it in base controller 
that other controllers inherit from.  

*Note: Controllers are also called as "API endpoints", and "API handlers"*


### Key concept


Common logic should be written once and reused across multiple API endpoints, following the 
DRY principle.  


### Applies to:


- **REST APIs**.
- **GraphQL APIs**.
- **Microservices**.


## Common use cases for Shared Base Controller:


- **Request Validation**: Avoid repeated validation logic in each controller.  
- **Response Formatting**: Ensure all responses follow a consistent format.  
- **Error Handling**: Standardize error messaging across APIs.  
- **Authentication and Authorization**: Centralize Auth logic.
- **Logging**: Implement a single login layer for all incoming requests and outgoing responses.  


## When to use a Shred Base Controller


|Use When...|Avoid When...|
|-|-|
|Multiple APIs share common logic|API have very different behaviors|
|You need consistent error handling|Each controller has unique validation rules.|
|Standardized API responses are required|A simple project with a few endpoints.|


## Examples


### 1. Example # 1. 

- *singleController.py*: A Flask application without a Shared Base Controller. 
(Violates the DRY principle).  
- *sharedBaseController.py*: A Flask application that implements the Shared 
Base Controller to encapsulate reusable functionality.  