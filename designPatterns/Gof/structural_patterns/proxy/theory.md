# Structural pattern: Proxy


## Introduction


The **Proxy Pattern** is a structural design pattern that provides a surrogate or placeholder 
for another object to control access to it. It allows intercepting, modifying, or delaying 
requests before reaching the actual object.  


### Problems it Solves


- When a direct access to an object is not desirable or practical 
(e.g., security, performance, logging).  
- When an object initialization is resource-heavy, and lazy initialization cam improve 
performance.  
- When access to an object needs to be controlled or restricted 
(e.g., authentication, caching, etc.).  


### Solution


- Introduce a **Proxy class** that wraps the real object and controls access to it.  
- The Proxy implements the same interface as the real object, so the client does not know 
the difference.  


### Schema


```
+----------------+
|    Client      |
+----------------+
        │
        ▼
+----------------+
|    Proxy       |  (Controls Access)
|----------------|
| + request()    |
+----------------+
        │
        ▼
+----------------+
|   RealSubject  |  (Actual Object)
|----------------|
| + request()    |
+----------------+

```


## When to Use


- **Virtual Proxy**: Delay object creation until it is really needed (*Lazy initialization*).  
- **Protection Proxy**: Restrict access to sensitive data (*Authentication*).  
- **Logging Proxy**: Record interactions with an object.  
- **Caching Proxy**: Store frequently accessed data.  
- **Remote Proxy**: Interact with an object over network (*RPC*, *gRPC*).  


## Key components


1. **Subject Interface**: This interface defines the common methods that both **Real class** 
and **Proxy class** implement. It is the interface the client interacts with.   
2. **Real class**: This is the object that the **Proxy** represents. It is the object that 
perform the read work.  
3. **Proxy**: The class tha acts as a placeholder for the **Read object**. It implement the 
**Subject interface** and forward request to the **Real object** when necessary. The **Proxy** 
can also add it own logic, such as caching, security checks, or lazy loading.  


### Key relationships and How it Works


- The **Client** interacts with the **Proxy** within the **Subject interface**.  
- The **Proxy** receives the **client's** request.  
- The **Proxy** might perform some actions (e.g., logging).  
- The **Proxy** then forwards the request to the **Real Subject**.  
- The **Real Subject** performs the actual work.  
- The **Proxy** can perform additional actions before returning the result back to the client.  


## Examples


### 1. Example 1

- *virtual_proxy.py*: Virtual Proxy (Lazy initialization). Used when it is expensive to initiate 
the read object. Therefor, we delay the initiation until the real object is actually needed.  
- *protection_proxy.py*: Protection Proxy (Access COntrol). Used when it is required to restrict 
the access bases on roles (e.g., Admin, Guest).  
- *caching_proxy.py*: Cache repeated operations results.  