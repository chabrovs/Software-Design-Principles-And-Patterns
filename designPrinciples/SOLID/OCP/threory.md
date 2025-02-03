# Open/Closed Principle (OCP)


## Introduction


The **Open/Closed Principle** formulated by Bernart Myyer in 1988.  

It stands that software entities (e.g., classes, modules, functions) should be open for 
extension but close for modification.  This means that the behavior of a module can be 
extended to meet new requirements, but its existing code should not be modified.   


## Definition


> "A software module should be open for extension but closed for modification". 

- **Open for extension**: modules behavior can be extended to accommodate new functionality.  
- **Closed for modification**: the module's existing code remains unchanged.  


### Real-Wold analogy: consider a power strip. 

- You can extend functionality by plugging new devices (extension).  
- You do not need to open the power strip and modify its internal wiring to add more devices 
(no modification).  


## Common Pitfalls:

1. **Over-Engineering**.  
2. **Rigid Abstraction**: poorly designed abstractions can make it difficult to implement extensions.  


## Design Pattern supporting OCP:


1. **Strategy**: Defines a family of algorithms and encapsulates each one in a separate class.   
2. **Decorator**: Dynamically adds new functionality to an object without modifying the code.  
3. **Factory Method**: Delegates object creations ti subclasses, allowing new types to be introduced without 
altering existing code.  
4. **Observer**: Enables loosely couples notification mechanism, supporting new observer types without 
changing the subject (observable).  


## How to adhere OCP in code ?


To adhere the **Open/Closed Principle**, you must design systems in a way that new functionality is added 
through extension, not modification.  


### 1. Abstraction with Interfaces or Abstract classes:  


- Use abstract classes to define contracts.  
- Extend functionality by implementing new concrete classes.  

***See Example # 1***


### 2. Polymorphism:  


Replace conditional (e.g., `if`, `switch`) statements with Polymorphic behavior.  

***See Example # 2***


### 3. Dependency injection: 


1. Use Dependency injection to supply dependencies (e.g., services, components) from 
the outside scope rather than hardcoding them. This makes it easier to swap or extend 
implementation.  

***See Example # 3***




### 4. Composition over Inheritance: 


1. Favor object composition to dynamically add behavior instead of modifying code.  

***See Example # 4***


### 5. Use plugins or Extensions


1. Design system that supports plugins or extensions in order to load new functionality 
dynamically, rather than modifying existing code.    

***See Example # 5***


### 6. Use configuration files: 


1. Move behavior and rules into config files (e.g., JSON, XLM, YAML) instead of hardcoding them.  
This way you can change rules and behavior without modifying the code.

***See Example # 6***


### 7. Open extensions by using Callbacks and Events:


1. Use callbacks or event-driven programming to allow the system to invoke external logic 
without modifying the code. 

***See Example # 7***


### 8. Utilize factories for object creation (class instantiation):  


1. Use factories to abstract the creation process, enabling extension without modifying 
existing code.  

***See Example # 6***


### 9. Modular design with Packages:


1. Separate distinct functionalities by different packages or modules that can be 
extended or replaces individually. 


### 10. Use Middleware for extensible workflows:  


1. For systems with layered or sequential processing, use the middleware to allow dynamic insertion 
of new behaviors.  

***See Example # 8***


