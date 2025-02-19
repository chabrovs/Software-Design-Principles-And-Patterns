# Behavioral pattern: Observer


## Introduction


The **Observer Pattern** is a behavioral design pattern where an object (Subject) maintains a 
list of dependents (Observers) that need to be notified whenever its state changes.  
This pattern is useful when there is one-to-many relationships where multiple objects need to 
react to changes in a central object without being tightly coupled.  

*(This pattern supports different changes stated propagation strategies (e.g., Push-Based, Pull-Based))*


### Problems it Solves


- When multiple object need to be updated automatically whenever a subject changes.  
- When subject should not be tightly coupled, allowing dynamic addition or removal of observers.  
- In Event-Driven programming (e.g., UI-updates, messaging systems, etc.).  


### Solution


- Define a **Subject (Observable)** that maintains a list of **Observers**.  
- **Observers** subscribe to the **Subject** and get notified when its state changes.  
- This creates a loosely coupled, reactive system.  


### Schema


```
+------------------+
|   Subject        |  (Maintains a list of observers)
|------------------|
| - observers      |
| + attach()       |
| + detach()       |
| + notify()       |
+------------------+
        ▲
        │
+------------------+
|  ConcreteSubject |  (Stores state & notifies observers)
+------------------+
        ▲
        │
+------------------+
|   Observer       |  (Interface for listeners)
|------------------|
| + update()       |
+------------------+
        ▲
        │
+--------------------+    +--------------------+
|  ConcreteObserverA |    |  ConcreteObserverB |
| (Receives updates) |    | (Receives updates) |
+--------------------+    +--------------------+

```


## Use cases


- when multiple objects depend on a single resource (e.g., stock prices, weather updates).  
- Real time notifications (e.g., chat systems, event listeners).  
- Event-Driven programming.  
- Decoupling components to resource dependencies.   


## Key Components


1. **Subject (Observable)**: This is the object whose state is of interest. It maintains a list 
of dependents (Observers) and provides methods for attaching and deleting observers. It also 
has a method (or mechanism) for notifying observers when its state changes.  
2. **Observer Interface (or Abstract Observer)**: The interface defines the method that 
**Observers** must implement to receive updates from the **Subject**. Often called as 
`update()` or `notify()`.  
3. **Concrete Observers**: These classes implement the **Observer Interface**. Each 
**Concrete Observer** is interested in **Subject's** state and perform some actions when 
notified of a change.  


### Key Relationships and How it Works


- The **Subject** maintains a list of **observers**.  
- **Observers** register (attach) themselves with the **Subject**.  
- When the **Subject's** state changes, it notifies all registered **Observers** by calling their 
`update()` method *(it is in case of Push-Based change propagation)*.  
- Each **Observer** then performs its specific action based on the **Subject's** new state.  


## Examples:


### 1. Example 1


- *observer.py*: Default implementation of the pattern.  