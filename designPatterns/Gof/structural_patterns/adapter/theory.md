# Structural pattern: Adapter


## Introduction


The **Adapter Pattern** is a structural design pattern that allows objects with incompatible 
interfaces ti work together. It acts as a bridge between two interfaces, converting one 
interface into another without modifying existing code.  


### Problems it solves


- When two systems or components cannot communicate due to interface differences.  
- When you want to reuse existing code that expects a different interface.  
- When integration legacy code with modern components.  


### Solution


- Introduce an adapter class that wraps the incompatible interface and transform calls to the 
expected format.  
- Allows the existing code to remain unchanged.   


## Components of the Adapter Pattern


1. **Target interface**: This interface that the client code expects to use. It defines the 
methods that the client can call.   
2. **Adaptee**: This is the class that has the incompatible interface. It is the class that 
the client wants to use by can not directly due to the interface mismatch.   
3. **Adapter**: The class that makes the **Adaptee** interface compatible with the 
**Target** interface. It implements the targe interface and internally delegates calls to 
the **Adaptee**.  


### Key relationships and How it Works


- The client code interacts with the **Adapter** through the **Target interface**.  
- The **Adapter** receives the client's request and translates them into calls that the 
**Adaptee** understands.  
- The **Adapter** then translates the **Adapteree's** result back into a format that 
the client expects (according to the **Target interface**).  


### Schema

```
+------------------+   +---------------------+
|   Client         |   | Adaptee             |
| (Expects Target) |   | (Incompatible API)  |
|------------------|   |---------------------|
| + request()      |   | + specific_request()|
+------------------+   +---------------------+
        ▲                  ▲
        │                  │
        │    +-------------------------+
        └──► |    Adapter              |
             | (Bridges the Gap)       |
             |-------------------------|
             | + request()             |
             | Calls specific_request()|
             +-------------------------+

```

## When to Use


- When introducing third-party library taht do not match your system API.  
- When migrating legacy systems while maintaining backward comparability.  
- When reusing code that was design for different interface.  
- When working with inconsistent APIs across multiple services.  


## Examples:


### 1. Example 1

- *adapter.py*: Class-Based Adapter using inheritance.  


### 2. Example 2

- *adapter.py*: Object-Oriented Adapter using composition.  

