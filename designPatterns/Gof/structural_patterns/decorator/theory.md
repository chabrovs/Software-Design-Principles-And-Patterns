# Structural Pattern: Decorator


## Introduction


The **Decorator Pattern** is a structural design pattern that allows dynamically adding 
behavior to an object without modifying the objects` existing code. Instead of modifying a 
class directly, it is possible to wrap the object with the decorator that enhances 
object's functionalities.


### Problems it solves


- When there is a need to extend the object's behavior dynamically without modifying the 
original class.  
- When using subclassing (inheritance) is impractical due to many variations.  
- When there is a need to add features selectively instead of modifying all instances.  


### Solution


- Create a base interface (or ABC).
- Implement concrete decorators that wraps the original object and extend its behavior dynamically.  


### Schema


```
+----------------+
|   Component    |  (Defines the interface)
+----------------+
        ▲
        │
+----------------+
|  ConcreteComp  |  (Base Object)
+----------------+
        ▲
        │
+----------------+
|  Decorator     |  (Wraps & Extends Component)
+----------------+
        ▲
        │
+----------------+
|  ConcreteDec1  |  (Adds Behavior)
+----------------+
        ▲
        │
+----------------+
|  ConcreteDec2  |  (Adds More Behavior)
+----------------+
```


## When to Use


- Add responsibilities dynamically instead of modifying the class.  
- Reduce the number of subclasses need for multiple variations.  
- Existing code violated the **OCP**.  
- Layer multiple behaviors on an object.  


## Key Components


1. **Component Interface (or Abstract Component)**: The interface that defines common operations 
both **Concrete component** and **Decorator** implement. It is the interface the client interacts 
with.  

2. **Concrete Component**: The original object to which new behaviors can be added. It implements 
the **Component interface**. 

3. **Decorator (or Abstract Decorator)**: The base class for all decorators. It implements the 
**Component interface** and holds the reference to a **Component object** 
(usually through composition). It typically delegates all operations to the wrapped component 
by default.  

4. **Concrete Decorators**: These are the classes that add specific behaviors to the Component. 
They inherit from the decorator class and override specific methods to add their functionality. 
They can add functionality before or after delegating to the wrapped Component.   


### Key Relationships and How it Works


- The **Client** interacts with the **Component Interface**.  
- The **Client** can wrap a **Concrete Component** into one or more Decorators.  
- Each **Decorator** adds it own behavior and then delegates the wrapped components.  
- The chain of Decorators and the **Concrete Component** form a *decorated* Object.  
- When the **Client** calls a method on the decorated object, the call is passed through 
the chain of decorators, with each **Decorator** adding its behavior.  


## Examples


### 1. Example 1


- *class_decorator.py*: Basic Decorator.


### 2. Example 2


- *python_decorator.py*: Python decorators implementation. 