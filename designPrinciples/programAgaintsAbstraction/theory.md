# Program against abstraction


## Introduction


The **Program against abstraction** principle is a cornerstone of software design. 
It emphasizes writing code that depend on __abstraction__ rather than __concrete implementations__.  

This principle allows developers to design systems that are flexible, reusable, and easy extensible.  

This principle is closely tied to the __Dependency Inversion Principle (DIP)__ and the broader idea of __interface-driven development__.  


## Definition


The **Program Against Abstraction** advocates for:  
- Writing code that depends on interfaces or abstract classes rather than specific implementations.  
- Allowing details (concrete implementations) to vary without requiring changes to the high-level logic.  


### Real-World Analogy:

Imagine you are designing a power socket.  
- **Concrete approach**: a socket is designed specifically for a particular plug type (e.g., US or EU).  
- **Abstract approach**: a universal socket (interface) works with any plug type as long as the plug adheres to the socket interface.  


## How to implement in code ? 

A. Interfaces and Abstract Base Classes:  
B. Dependency Injection.   
C. Factories.   


# Examples

### 1. Example 1

- *anti-pattern.py*: Describes anti-pattern for software design.  
- *abstraction.py*: Describes how to use an abstraction (or build an interface) by 
utilizing the `abc` (*Abstract Base Class*) module in Python.


### 2. Example 2

- *abstraction.py*: One more example of abstraction.  


### 3. Example 3

- *factory.py*: Describes how to use factories in Python. 
A **factory** is a class or method that return a instance (object) of a concrete implementation class.  
The **factory** usually takes a type (a string in case of Python) as an argument.  
