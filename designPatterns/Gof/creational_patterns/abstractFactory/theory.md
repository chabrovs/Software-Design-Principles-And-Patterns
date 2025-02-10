# Creation pattern: Abstract factory. 


## Introduction


The **Abstract Factory** is a creational design pattern that provides an interface for crating 
families of related products without specifying concrete classes.  


## Components: 

1. **Abstract Factory**: the interface that declares method for creating abstract products. 
It does not define how object are created, only that they must be creatable.  
2. **Concrete Factories**: these classes implement the __Abstract Factory__ interface. 
Each concrete factory is responsible for creating a family of related products. Crucially, 
each factory creates products that are compatible with each other.  
3. **Abstract Product**: the interface for a type of product. It declares methods that all 
concrete classes of this type must implement.  
4. **Concrete Products**: these classes implement interface of the Abstract product.  

### Key relationships 

- The client code interacts with abstract factory.  
- The client asks the factory to create products. 
- The specific concrete factory being used determines which concrete product are created. 
- The client then works with the abstract products, but the actual objects it is using 
are concrete products.


## Pros and Cons

### Pros:

- **Encapsulates object creations**: The client does not know which concrete class is used.  
- **Ensures consistency**: Guarantees that only compatible objects are created together.  
- **Supports the OCP**: New product families can be added without modifying existing code.  

### Cons:

- **Increased complexity**.
- **Harder to extend individual products**: Adding a new type of a product required 
modifying multiple factory classes. 
