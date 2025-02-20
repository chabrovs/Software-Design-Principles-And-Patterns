# Behavioral pattern: Strategy


## Introduction


The **Strategy Pattern** is a behavioral design pattern that allows to define a family of 
algorithms, encapsulating each one, and making them interchangeable dynamically without 
modifying the client code.  
This pattern is useful when theres is a need to select different algorithms at runtime 
without using complex conditional statements.  


### Problems it Solves


- When multiple algorithms perform the same task differently (e.g., sorting, processing payments).  
- When selecting algorithms should not affect the reset of the application.  
- When using conditional statements to select algorithms makes the code difficult to maintain.  


### Solution


- Define a Strategy Interface with a common method (e.g., `execute()` or `calculate()`).  
- Implement Concrete Strategies that provide different algorithm implementations.  
- The Conte (main object) delegates the operation to a selected Strategy object,allowing dynamic 
switching.  


### Schema


```
+--------------------+
|   Strategy (ABC)   |  (Defines a common interface)
|--------------------|
| + execute()        |
+--------------------+
        ▲
        │
+--------------------+    +--------------------+    +--------------------+
| ConcreteStrategyA  |    | ConcreteStrategyB  |    | ConcreteStrategyC  |
| (Implements A)     |    | (Implements B)     |    | (Implements C)     |
+--------------------+    +--------------------+    +--------------------+
        ▲
        │
+--------------------+
|    Context         |  (Uses a strategy dynamically)
|--------------------|
| - strategy         |
| + set_strategy()   |
| + execute()        |
+--------------------+

```


## Key Components


1. **Strategy Interface (or Abstract Strategy)**: This interface defines common methods for 
all different algorithms (strategies). It declares methods that the client will use to interact 
with the chosen strategy.  
2. **Concrete Strategies**: These classes implement the **Strategy Interface**. Each 
**Concrete Strategy** represents a specific algorithm.  
2. **Context**: This is an object that chooses and uses a Strategy object. It does not implement 
the algorithm itself; it delegates the work to the chosen Strategy. The **Context** maintains 
a reference to the current Strategy.  


### Key Relationships and How it Works


- The **Client** creates a **Context** object and configures it with a specific **Strategy** 
object.  
-  When the **Client** calls a method in the **Context**, the Context delegates the call to 
the currently selected **Strategy** object.  
- The Strategy object execute the algorithm.  
- The **Client** can change the **Strategy** at runtime, allowing the **Context** to switch 
between different algorithms.  


## Examples


### 1. Example 1


- *strategy.py*: sorting strategies.  