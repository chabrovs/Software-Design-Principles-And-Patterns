# Composition Over Inheritance


## Introduction


All **Aggregation**, **Composition**, or **Inheritance** are the methods to establish inter-class communication.  
These methods define the relationships between classes.  

The **Composition Over Inheritance** is a design principle that advocates to use the composition over inheritance.  
This design principle can be widely applied when the inheritance classes bring overcomplicated hierarchies. 
Additionally, the inheritance approach does introduce separation of concerns but does not introduce decoupling. 
All classes participating in an inheritance hierarchy are considered to be tightly coupled together.  

On the other hand, there is a new approach that enables loosely coupling but has not a strict hierarchy.  

### Use case


This principle may be widely applied in cases where the hierarchy brings  


## Definition


### Inheritance (is-a-type-of)


**Inheritance**: a type of inter class relationships that makes a derived class inherit data and behavior from the superclass.   


### Aggregation (has-a weak)


**Aggregation**: a type of association where one class consist of other classes, but tge contained object can exist independently.  
The lifecycle of the contained objects is __independent__ from the container lifecycle.  


### Composition (has-a strict)


**Composition**: class can be composed of each other, thereby establishing composition between enclosing class and its embedded classes. 
Compositional relationships also knows as "has-a" relationship.  
The lifecycle of the composed (contained) object is dependent (tied to) on the container (enclosing class) lifecycle.  


## Examples


### 1. Example 1

-*aggregation.py*: In Python aggregation can be achieved through dependency injection.  
By creating a aggregated component, and then injecting it to the container.  

-*composition.py*: In Python composition is achieved by instantiating compose objects right in a class constructor.  

-*inheritance.py*: Python has a build-in Inheritance support. 
The inheritance in Python supports building hierarchies, using method from a superclass and it has its ows 
method resolution order.  
