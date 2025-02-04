# Creation pattern: Factory method. 


## Introduction


The **Factory Method Pattern** that provides an interface for creating object.  

- Follows the Single Responsibility Principle (SRP): each concrete factory instantiates only one 
type of products.  
- Follows Open Close Principle (OCP):  In order add new Product you need to create new Product concrete 
class and new Factory to instantiate the new Product. Modification of existing code is not required.  
- Follows the Dependency Inversion Principle (DIP): Factories return an abstract Product type 
(Product interface).  


### Problems it solves


- High coupling in object creation. 


## Use cases:


- When a class shouldn’t depend on concrete classes for object creation.  
- When the exact type of the object isn’t known until runtime.  
- When you need to centralize object creation logic.  
- When you expect future extensions, allowing new product types to be added easily.  


## When _not_ to use:


- When only one or two objects are created → A simple function or class instantiation is enough.  
- If no variation in object creation exists, using new directly is simpler.  


## Implementations in Python:


### Product 


- **Abstract product**: an interface for the concrete Products.
- **Concrete class**: instantiated by the Factory.  


### Factory

- **Abstract Factory**: an interface for the concrete Factories.
- **Concrete class**: a class that has a method (e.g., `create_object`) that instantiates an 
concrete product class and return it. 


## Anti-Patterns


### 1. God Factory


- A single class that creates all types of products (objects), violating 
the Single Responsibility and Open Close Principles:

Example:

```
class DodFactory(FactoryI):
    def create_object(self, object_type: str):
        match object_type:
            case "sqldatabse":
                return SQLDatabase()
            case "redisdatabase":
                return RedisDatabase()
            case _:
                raise NotImplementedError()
```

- **Problem**: The factory becomes bloated and hard to maintain as more types are added.


### 2. Static Factory

- Using a static method or class method to create objects, which limits flexibility 
and makes testing harder.

Example: 

```
class DodFactory(FactoryI):
    @staticmethod
    def create_object(object_type: str):
        match object_type:
            case "sqldatabse":
                return SQLDatabase()
            case "redisdatabase":
                return RedisDatabase()
            case _:
                raise NotImplementedError()
```

- **Problem**: Static methods cannot be overridden, making it harder to extend or modify behavior.


