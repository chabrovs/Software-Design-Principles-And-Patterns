# Behavioral pattern: Iterator


## Introduction


The **Iterator Pattern** is a behavioral design pattern that allows to traverse a collections of 
elements without exposing its internal structure.  

Instead of manually handling loops, the **Iterator** encapsulates traversal logic, making it 
consistent and reusable across different collections (polymorphic).  


### Problems it solves


- Traversing a collection without exposing its internal details (implementation). It does not 
matter the way the collection is implemented as long as it adheres to the Iterator Interface.  
- Enables multiple ways to traverse a collection (e.g., forward, backward, filtering).  
- When a collections should be iterable but should not depend on a specific traversal logic.  


### Solution


- Define an **Iterator Interface** with `next()` and `has_next()` methods.  
- Implement **Concrete Iterators** that traverse different collections.  
- The client code does not interact with the collection directly but uses the **Iterator** instead.


### Schema


```
+--------------------+
|   Iterable (ABC)   |  (Defines an Interface for Collections)
|--------------------|
| + create_iterator()|
+--------------------+
        ▲
        │
+--------------------+
|  ConcreteIterable  |  (Actual Collection)
|--------------------|
| + create_iterator()|
+--------------------+
        ▲
        │
+--------------------+
|  Iterator (ABC)    |  (Defines traversal methods)
|--------------------|
| + next()           |
| + has_next()       |
+--------------------+
        ▲
        │
+--------------------+
| ConcreteIterator   |  (Implements Traversal)
+--------------------+

```


## Key components


1. **Iterator Interface (or Abstract Iterator)**: This interface defines methods for traversing 
the aggregate (traversable object). Common methods include `next()`, `has_next()`, and sometimes 
`current_item()` or similar.  
2. **Concrete Iterator**: Implements the concrete interface. It keeps track of the current 
position in the traversal and knows how to access the next element. Each **Concrete Iterator** is 
associated with a specific **Aggregate**.  
3. **Aggregate Interface (or Abstract Aggregate)**: This interface defines the method for 
creating an iterator object. It is the interface the client uses to get the **Concrete Iterator** 
object.   
3. **Aggregate**: This class implements the **Aggregate Interface**. It is the collection or 
container object whose elements are being iterated over. It creates and returns a 
**Concrete Iterator** object.  


### Key Relationships and How it Works


- The **Client** asks the **Aggregate** for an **Iterator**.  
- The **Aggregate** creates a **Concrete Iterator**, which is associated with the **Aggregate**.  
- The **Client** uses the **Iterator** to traverse the **Aggregates's** elements.  
- The **Iterator** keeps track of the current position and provides methods to access the next 
element.  


## Examples


### 1. Example 1

- *iterator.py*: Classical Implementation


### 2. Example 2


- *forward_iterator.py*: Python iterator implementation.
- *reverse_iterator.py*: Python iterator implementation.