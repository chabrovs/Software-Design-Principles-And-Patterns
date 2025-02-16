# Structural Pattern: Composite


## Introduction


The **Composite Pattern** is a structural design pattern that lets to compose objects into tree 
structures to represent part-whole hierarchies. It allows client to treat individual objects 
and group of object uniformly. 


### Problems it solves


- When there is a need to treat individual object and group of object in the same way.  
- When dealing with tree structures (e.g., FileSystem UI components).  
- When using nested structures, but want a consistent API for both single and 
composed objects.  


### Solution


- Define a common interface for both leaf (individual object) and composite objects 
(groups of items).  
- Client does not need to know whether they are dealing with a single object or a composed one.  


### Schema


```
+----------------------+
|   Component (Base)   |  (Defines the common interface)
+----------------------+
        ▲
        │
+----------------------+    +----------------------+
|      Leaf (Item)     |    |   Composite (Group)  |
| (Represents a single |    | (Holds multiple      |
|  element)            |    |  children)           |
+----------------------+    +----------------------+

```

## Components:


1. **Component Interface (or Abstract Component)**: This interface defines the common operations 
for both leafs and composites. It typically includes methods for adding/removing child components 
and perform operations that are meaningful for both leaf and composite.  
2. **Leaf**: This class represents individual objects in the hierarchy. It implements the 
**Component interface** and does not have any children.  
3. **Composite**: This class represents container objects that can hold other components 
*(either leafs or composites)*. It implement the **Component interface** and provides methods 
for managing its children.  


### Key Relationships and How it Works


- The **client** interacts with the **Component interface**.  
- The **Client** can treat both Leafs and Composites uniformly through this interface.  
- A **Composite** can contain other components (Leafs, Composites), creating a hierarchical 
tree structure.  
- When a **Client** calls an operation on a **Composite**, the **Composite** typically delegates 
the call to its children. This allows operations to be applied recursively to the entire tree 
structure.  


## Examples


### 1. Example 1

- *composite.py*: General implementation of the Composite design pattern.  