# Liskov Substitution Principle (LSP)


## Introduction


The **Liskov Substitution Principle** was introduces by Barbara Liskov in 1987.  

It ensures that subtypes (subclasses) can be used interchangeably with their base 
types (superclasses) without altering the correctness of the program. LSP is fundamental 
for building robust and maintainable object-oriented systems by preserving 
*behavioral integrity in class hierarchies*.  


## Definition


> "Object of  a superclass should be replaceable with objects of its subclasses 
> without affecting the correctness of the program".

This means that a subclass should extend the behavior of the superclass without 
changing its internal behavior.   


### Key Consideration for LSP compliance

**A subclass should:**  
1. **Preserve behavior**: Maintain the expectation set by the superclass.  
2. **Follow type safely**: Accept input and return output consistent with the superclass.  
3. **Avoid violating postconditions**: Do not impose stricter conditions in a subclass.  
4. **Support inheritance properly**: The derived class should not remove functionality 
expected by the superclass.  


## Violation of LSP:


**A class hierarchy violates LSP if:**  
- A subclass overrides methods but changes its behavior significantly.  
- A subclass removes functionality expected in the superclass.  
- A subclass introduces new constraints that break substitution. 
- Using a subclass required checking its type (breaking polymorphism).  
    For example, using the `isinstance()` or type comparison in a method 
    to determine its behavior.  


## How to adhere to LSP in code ?


1. Ensure that subclass honers the contract of the superclass.  
2. Use composition instead of inheritance if the behavior changes dramatically.  
3. Follow the "Tell, Do not ask" principle to avoid checking subclass type explicitly.  
4. Apply the Interface Segregation Principle (ISP) to avoid forcing subclasses to 
implement unnecessary methods.  


## Examples: 

### 1. Example 1:


- *violatingLSP.py*: An example of violation LSP by brutal method overriding in the 
subclass.  
- *complyingLSP.py*: An example of complying to LSP by introducing a new abstraction 
layer.   


### 2. Example 2:

A usage of a subclass must not require a type checking by using methods like `isinstance()`. 

- *violatingLSP.py*: Violates the LSP because requires a type check before subclass usage.  
- *complyingLSP*: Complies to the LSP because does not require a type check, but if a wrong 
type was provides raises a runtime Type Error (which is acceptable!). 


### 2. Example 2:

Shows common violation of LSP and OCP. 

- *violatingLSP.py*: Violates the LSP and OCP.  
- *complyingLSP*. 