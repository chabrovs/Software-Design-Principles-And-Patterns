# Behavioral Pattern: Chain of Responsibility


## Introduction


The **Chain of Responsibility (CoR)** is a behavioral design pattern that allows multiple 
objects to handle a request sequentially, forming a chain.  

Instead of a single handler, the request moves through a chain of handlers until of one 
of them processes it or reaches the end the chain.  


### Problems it Solves


- When multiple handlers can process a request, but we do not know which one if advance.  
- When we want to avoid hardcoding conditions in a single handler.  
- When we want to decouple senders from receivers dynamically.  


### Solutions


- Define a common interface for handlers.  
- Implement concrete handlers that process request or pass them to the next handler.  
- The request flows through the chain until a handler processes it.  


### Schema


```
+--------------------+
|    Handler         |  (Defines common interface)
|--------------------|
| - next_handler     |
| + set_next()       |  (Sets next handler)
| + handle()         |  (Handles request or passes to next)
+--------------------+
        ▲
        │
+--------------------+    +--------------------+    +--------------------+
|  ConcreteHandlerA  |    |  ConcreteHandlerB  |    |  ConcreteHandlerC  |
|(Handles or Passes) |    |(Handles or Passes) |    |  (Handles Request) |
+--------------------+    +--------------------+    +--------------------+

```


## When to Use ?


- The request **must be handled by one of multiple handlers**.  
- The set of handlers **must be dynamically changeable**.
- Avoid complex `if-else` statements in a single class.  
- Share the same interface but process requests differently.     


## Key Components


1. **Handler Interface (or Abstract Handler)**: The interface defines the methods for 
handling requests. It typically includes a methods like `handle_request()` or similar. 
It may also define a methods for setting the next handler in the chain.   
2. **Concrete handlers**: These classes implement the **Handler Interface**. 
Each **Concrete Handler** is responsible for handling a specific type of request 
or a specific condition. They decide whether to process the request or pass t on.  


### Key Relationships and How it Works


- The **Client** send a request to the first handler in the chain.  
- Each handler in the chain examines the request.  
    - If a handler can handle the request, it does so and may optionally stop the chain. 
    - If a handler can not handle the request, it passes the request ot the next 
    handler in the chain. 
- The request continues down the chain until it handled by a handler or reaches the end of 
the chain.  


## Examples


### 1. Example 1


- *chain_of_responsibility.py*: The technical support example. A support request should be 
processes by the first available agent. If Level1 cannot handle the request it passes to 
the next level.  


### 2. Example 2


- *chain_of_responsibilities.py*: The multilevel logging system.   