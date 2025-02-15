# Structural pattern: Bridge


## Introduction


The **Bridge Pattern** is a Structural design pattern that decouples an abstraction from 
its implementation, allowing them to vary independently.   


### Problems it solves


- When a class has multiple dimensions of variation and creating multiple subclasses leads to 
over complexity.  
- When there is a need to change the implementation without modifying abstraction.  
- When using inheritance leads to class explosion due to many combinations.  


### Solution


- Separate abstraction from implementation into independent hierarchies.  
- The abstraction defines high-level logic, while implementation handles low-level details.  
- The abstraction holds a reference to an implementation, allowing it to be changed dynamically.  


### Schema 


```
+--------------------+
|     Abstraction    |   (Defines the high-level interface)
|--------------------|
| - implementor      |   (Holds reference to an implementation)
| + operation()      |   (Delegates work to implementor)
+--------------------+
        ▲
        │
+--------------------+
| RefinedAbstraction |  (Extends abstraction)
+--------------------+
        │
        ▼
+--------------------+
|  Implementor       |  (Defines low-level details)
|--------------------|
| + operation_impl() |
+--------------------+
        ▲
        │
+--------------------+    +--------------------+
|  ConcreteImplA     |    |  ConcreteImplB     |
+--------------------+    +--------------------+

```


## Key Components


1. **Abstraction**: Defines the high-level interface that the client uses. Ot does not deal
with specifics of implementation. It holds a reference to an **implementor**.
2. **Refined Abstractions (Optional)**: This an extension of **Abstraction**. It provides more 
specialized or higher-level operations, still using the **implementor**.  
3. **Implementor Interface**: This defines the interface for the implementation. 
It is the interface that concrete implementation must adhere to.  
4. **Concrete Implementors**: These classes provide the specific implementations of the 
**Implementor Interface**.  


### Key Relationships and How it Works


- The **Client** interacts with the **Abstraction (or Refined Abstraction)**.
- The **Abstraction** holds a reference to an **implementor** 
(through the **Implementor Interface**).  
- When the **Client** class a method on the **Abstraction**, the abstraction delegates the 
actual work to the implementor.  
- The **Concrete Implementor** provides the specific implementation of the operation.  


## Examples


### 1. Example 1


- *bridge.py*: A simple implementations of the Bridge Pattern.