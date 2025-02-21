# Behavioral pattern: Template Method


## Introduction


The **Template Method Pattern** is a behavioral design pattern that defines the skeleton of an 
algorithm in a base class but lets subclasses override specific steps of the algorithms without 
changing its overall structure.  
This pattern is useful when multiple classes share the same structure but have slightly different 
implementations for specific steps.  


### Problems it solves


- When there are different variations of algorithm but there is a need to reuse the overall  
structure.  
- Avoid code duplication while allowing customization in subclasses.  
- Enforce a specific sequence of operations across multiple subclasses.  


### Solution


- Define the template method (the skeleton of the algorithm) in the base class.  
- Let subclasses override specific steps of the algorithm as needed.  
- Keep the code logic consistent while allowing flexibility in certain parts.  


### Schema


```
+----------------------------+
| AbstractClass (Base)       |  (Defines the algorithm skeleton)
|----------------------------|
| + template_method()        |  (Defines algorithm steps)
| + step1()                  |  (Default implementation or abstract)
| + step2()                  |  (May be overridden)
+----------------------------+
        ▲
        │
+----------------------------+    +----------------------------+
| ConcreteClassA             |    | ConcreteClassB             |
| (Implements/Overrides)     |    | (Implements/Overrides)     |
+----------------------------+    +----------------------------+

```


## Key Components


1. **Abstract Class (Template Class)**: This class defines the template method, which is the 
skeleton the the algorithm. It consists of abstract methods that represents the steps of the 
algorithm. The template method calls these abstract method in a specific order. The Abstract
class also provides default implementations for some of the steps, or got the template itself
(though it is common for the template method to be `final` to prevent subclasses from 
overriding it).  
2. **Concrete Classes**: These classes inherit from the Abstract class and implement the 
Abstract methods. Each Concrete Class provides its specific implementation for the steps of 
the algorithms. They can override some steps while using default implementations for others.  


### Key Relationships and How it Works


- The **Client** interacts with the **Abstract Class** (through its subclasses).  
- The **Abstract Class** defines the complete methods, which calls the abstract methods in a 
specific sequence.  
- The **Concrete Classes** implement the abstract methods, providing their specific 
implementations for the steps of the algorithms.  
- The **Template Method** ensures that the steps of the algorithms are executed in the 
correct order.  


## Examples


### 1. Example 1


- *template_method.py*: Simple implementation of the template method design pattern.



### 2. Example 2


- *template_method.py*: Abstract implementations of the template method design pattern.  