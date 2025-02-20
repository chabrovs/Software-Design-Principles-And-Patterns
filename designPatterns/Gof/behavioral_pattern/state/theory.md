# Behavioral pattern: State


## Introduction


The **State Pattern** is a behavioral design pattern that allows an object ot change its 
behavior when its internal state changes, as it the object's class changed dynamically.  
The pattern is useful when an object need to to exhibit different behaviors based on its state, 
while keeping state specific logic encapsulated in a separate class.  


### Problems it Solves


- When an object behaves differently based on its internal state.  
- Whn using conditional statements to handle state transmission makes code complex and hard to 
maintain. *(Violating the OCP)*. 
- When theres is a need to encapsulate each state in a separate object for better organization.  


### Solution


- Define a state interface that declares behavior for different states.  
- Implement **Concrete State** classes for different behaviors.  
- The **Context (Main Object)** delegates tasks to the current **State** object, making 
transition seamless.   


### Schema


```
+------------------+
|    Context       |  (Maintains current state)
|------------------|
| - state          |
| + set_state()    |
| + request()      |  (Delegates behavior to state)
+------------------+
        ▲
        │
+------------------+
|   State (ABC)    |  (Defines behavior interface)
|------------------|
| + handle()       |
+------------------+
        ▲
        │
+------------------+    +------------------+    +------------------+
| ConcreteStateA   |    | ConcreteStateB   |    | ConcreteStateC   |
| (Implements A)   |    | (Implements B)   |    | (Implements C)   |
+------------------+    +------------------+    +------------------+

```


## Key Components


1. **Context (Main Object)**: This is the object whose behavior changes based on its internal 
state. It holds reference to the current **State** object.  
2. **State Interface (or Abstract State)**: This interface defines the methods that represent 
different behaviors of the object. All **Concrete State** classes must implement this interface.  
3. **Concrete States**: These classes implement the **State** interface. Each **Concrete State** 
represents a specific state of the object and provides implementation for the behavior in this 
state.  


### Key Relationships and How it Works


- The **Context** has a reference to the current **State** object.  
- The **State** object performs the action, which may depend on the specific **State**.  
- The **State** object can also change the **Context's** state, transforming it to 
different **Concrete State**.  


## Examples


### 1. Example 1


- *state.py*: State pattern implementation <u>with</u> dynamic state change propagation.


### 2. Example 2


- *state.py*: State pattern implementation <u>without</u> dynamic state propagation.