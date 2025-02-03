# Dependency Inversion Principle (DIP)


## Introduction


The **Dependency Inversion Principle** promotes loose coupling between software components by 
by ensuring that hight-level modules do not depend on low-level modules, but instead, both 
depend on abstraction.  


## Definition


> "High-level modules should not depend on low-level modules. Both should depend on abstractions
> (e.g., interfaces, ABSs)"

> "Abstraction should not depend on details, details should depend on abstractions" - Robert C. Martin


### Breaking it Down:

1. **High-Level Module**: Containing business logic (e.g, business rules). 
2. **Low-Level Module**: Perform specific tasks (e.g., database, APIs, etc.).
3. **Abstraction (e.g., interfaces, ABCs)**: Define contracts between High-Level and Low-level 
modules adhere to.  


## Violations of DIP:

**A system violates DIP if**:
- High-level modules depend on low-level modules.  
- Concrete classes are directly instantiated in high-level modules.  
- Changing low-level module requires modifying high-level modules.  
- String coupling between components.  


## Design Pattern That Support DIP:

Several design patterns naturally enforce DIP:

1. **Dependency Injection (DI)**: Inject dependencies via constructors, methods, frameworks.  
2. **Factory Method Pattern**: Decouple object creating logic from business logic.  
3. **Strategy Pattern**: Allows different algorithms and implementation to be interchangeable.  
4. **Adapter Pattern**: Bridge incomplete interfaces without modifying existing code.  
5. **Observer Pattern**: Implements event-driven programming where subscribers depend on abstraction.  


## Common PitFalls: 

- **Over-Abstraction**: Introducing too many abstractions can make code harder to maintain.  
- **Complex Dependency Management**: Without a DI framework managing dependencies can be tedious.  
- **Performance Overhead**: Excessive layers of abstraction might introduce slight performance cost.  
- **Poorly Design Interfaces**: A bad abstraction can cause unnecessary complexity rather than solve problem.  


## How to adhere to the DIP in code:


### 1. Using interface

The first step to achieve DIP is introducing abstractions so that high-level modules depend on interfaces 
rather than concrete implementations.  

- ***See example # 1***


### 2. Using Dependency Injection

|Type|How it Works|Used for|
|-|-|-|
|Constructor injection|Dependencies are passed via constructor|Best for mandatory dependencies|
|Method injection| Dependencies are passed into via method parameters|Best for optional dependencies|
|Property injection (setter method)|Dependencies via a setter method|Best if dependency can change at the runtime|

1. **Constructor Injection**: ***See Example # 2***.  
The dependency is provided as an argument to the constructor (initializer) method `__init__`. 
And the dependency is used all throughout the class.  

2. **Method Injection**: ***See Example # 3***.
Provides dependencies via method parameters (but not to the constructor method).  
The method dependency is used when:
    - The dependency is optional (can use `None` as the default value).
    - Different dependencies may be used for different method calls.  
    - The dependency is used only in a single method, rather than throughout the class.  
    - Easies Unit testing as dependencies can be mocked.  

3. **Property (setter) Injection**: ***See Example # 4***.
Injecting Dependencies dynamically by setting attributes. 

- *propertyInjection.py*:
- *setterMethod.py*: User decorator to set a value to the property.  


### Summary

|To DO This|To Avoid|
|-|-|
|Depend on abstraction (interfaces/ABSs) | Depending on concrete classes (concrete implementations). |
|Use Dependency Injection (DI) | Creating dependencies inside a class |
|Apply Inversion of Control (IoC) | Manually managing dependencies |
| Use Factories for object creation | Instantiating objects directly in business logic |
| Implement Strategy/Adapter/Observer patterns| Hardcode behaviors in class |