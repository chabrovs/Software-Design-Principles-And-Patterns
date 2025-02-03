# Interface Segregation Principle (ISP)


## Introduction


The **Interface Segregation Principle (ISP)** states that client should not be forced to depend on interfaces 
they do not use. This principle encourages breaking down large, general purpose interfaces into smaller, 
more specific ones tailored to the needs of different clients.  

By following IPS, we ensure that classes remain focused, dependencies are minimized, and code is more 
maintainable ans scalable.  


## Definition


> Client should not be forced to depend on interfaces they do not use  

In other words, an interface should contain only the methods that relevant to the client (class). 
If a class is required in implement methods that it does not need, this means that the interface 
is too broad and should be split into multiple, smaller interfaces.  


## Key problems solved by ISP:


- **Prevents code pollution**: Avoids forcing classes to implement unnecessary methods.  
- **Improves maintainability**: Modifications to an interface will not impact unrelated classes.  
- **Reduces dependency coupling**: Ensures each class depends only on the functionality in requires.  
- **Facilitates testability**.


## Common violation of ISP:


**An interface violates ISP if:**
- It has too many unrelated methods that do not apply to all concrete classes.   
- Concrete classes are forces to provide empty or dummy method implementations.  
- Changes to the interface break many unrelated classes that do not need the changed behavior.  


## Common Pitfalls using ISP:


- **Over-engineering**: Creating too many interfaces can lead to excessive complexity.  
- **Unnecessary abstractions**: Only split interfaces when it adds clarity.  
- **Poor interface design**: Ensure interfaces are meaningful and logical.  



## How to adhere to the ISP in code ?


1. Analyze existing interfaces.  
2. If interfaces violate the ISP you can: 
    - Split large interfaces into smaller, role specific.  
    - Use multiple interfaces instead of a single general-purpose interface.  
    - (caution): Use multiple inheritance to implement several interfaces in a concrete class.  
    - Favor Composition Over Inheritance if behavior varies significantly.  
    - Apply Dependency Inversion by depending on abstractions with only the necessary methods.   


## Examples


### 1. Example 1:

- *violatingISP.py*: Violates ISP by having a large interface.  
- *complyingISP.py*: Complies the ISP by splitting the large interface into several specific-purpose.  


### 1. Example 1:

- *violatingISP.py*: Violates ISP and OCP.
- *complyingISP.py*: Complies with ISP and OCP by having specific interfaces.   