# Behavioral pattern: Command


## Introduction


The **Command Pattern** is a behavioral design pattern that turns a request into an object, 
allowing it to parameterize, queue, and execute request later.  
It decouples the sender (who requests an action) from the receiver (who performs the action) 
by encapsulating the request as a command object.    


### Problems it Solves


- When there is a need to implement **undo, queue, or store operations**.  
- When a request needs to be executed later, or logged.  
- When there is a need to **decouple the initiator of a request from the action itself**.  


### Solution


- Define a **Command Interface** with an `execute()` method.  
- Implement **Concrete Commands** that call different actions.  
- A **Command Invoker** executes the command without knowing their details.  


### Schema


```
+--------------------+
|     Command        |  (Defines execute method)
|--------------------|
| + execute()        |  
+--------------------+
        ▲
        │
+--------------------+    +--------------------+
|  ConcreteCommandA  |    |  ConcreteCommandB  |
|  (Performs Action) |    |  (Performs Action) |
+--------------------+    +--------------------+
        ▲
        │
+--------------------+
|  Invoker (Executor)|  (Stores and executes commands)
+--------------------+
        ▲
        │
+--------------------+
|    Client          |  (Creates and sets commands)
+--------------------+

```


## Key Components


1. **Command Interface (or Abstract Command)**: This interface declares a method for executing 
the command, ofter named `execute()`. It might also include methods for undoing the command 
`undo()`, logging `log()`, etc; if these functionalities are necessary.  
2. **Concrete Commands**: These classes implement the **Concrete Interface**. 
Each **Concrete command** represents a specific action. It holds the receiver object 
(the object on which the operation is performed) and implements the `execute()` command by 
calling the appropriate methods in the **Receiver**.   
3. **Receiver**: The object that performs the actual operation. The **Concrete Command** holds 
a reference to the **Receiver** and delegates the execution to it.  
4. **Invoker**: This is the object that invokes the command. It does not know anything about 
the specific method being executed. It simply calls the `execute()` methods on the 
**Command** object.  
4. **Client**: The client creates the **Concrete Command** object to the **Invoker**.  


### Key relationships and How it Works


- The **Client** creates a **Concrete Command** object, associating it with a **Receiver**.   
- The **Client** passes the **Command object** to the **Invoker**.  
- The **Invoker** calls the `execute()` method o the **Command** object.  
- The **Command** calls the appropriate method on the **Receiver** to perform operation.  


## Examples


### 1. Example 1


- *command.py*: This example implement a simple Command pattern.  
    - Receiver: remote server.
    - Commands:
        1. Turn On: turns the remote server on.
        2. Turn off: turns the remote server off.
    - Invoker: remote server controller.



### 2. Example 2


- *command.py*: Implementing undo command. 
    - Receiver: a text editor.
    - Commands:
        1. Write: writes text to the editor.
    - Invoker: stores all the executed command in a list.