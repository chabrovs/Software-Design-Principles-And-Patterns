# Creation design pattern: Builder


## Introduction


The **Builder** is a creational design pattern that separated object creations from its
representation, allowing step-by-step creation of complex objects.  


### Schema

```
+------------------+    +------------------+    +------------------+
|    Director      |    |   Builder        |    |     Product      |
|------------------|    |------------------|    |------------------|
| + constructA()   |--->| + set_partA()    |--->| + partA          |
| + constructB()   |    | + set_partB()    |    | + partB          |
|                  |    | + get_result()   |    | + show()         |
+------------------+    +------------------+    +------------------+
```


## Problems it solves

- Creating object with **many optional parameters** using constructor leads to messy code 
and hard-to-read parameter lists.  
- IF a class has multiple configuration results in constructor overload issues.   


### Solution


1. Define a **Builder class** that constructs an object step-by-step.  
2. The client uses a fluent interface to configure the object before finalizing the build.  


## Components


1. **Builder interface (or ABC)**: this interface defines the methods for building different 
parts of the complex object.   
2. **Concrete builder**: these classes implement the builder interface. Each concrete builder 
is responsible of the complex object. They provide the actual implementation for building parts. 
3. **Director (optional)**: the director is the class that orchestrates the building process. 
It takes the builder object and calls its methods in a specific sequence to construct the complex 
object. The director often shields the client from the details of the construction process.  
4. **Product (the final object)**: this is the object that is being built. The product can be 
composed of many different parts, and the **Builder patter** helps to assemble these parts in 
a controlled and organized way.  


### Key relationships:  

- The client code interacts with the **Director** (if exists) ot directly with a **Concrete Builder**. 
- The client tells the **Director** or the **Builder** what to build.  
- The **Director (or Builder)** uses the Builder interface methods to construct the different parts 
of the product.  
- The **Concrete builder** provides the specific implementation for building each part.  
- Once the construction is complete, the **Builder** returns the fully assembled product to the 
client.  


## Examples:

### Example 1:

- *builder.py*: Builder pattern with director.  