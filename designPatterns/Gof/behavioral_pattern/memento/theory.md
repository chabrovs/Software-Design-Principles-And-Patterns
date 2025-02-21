# Behavioral pattern: Memento


## Introduction


The **Memento Pattern** is a behavioral design pattern that allows an object to 
capture and store its current state, and restore it later, without exposing its 
internal encapsulation.  


### Problems it Solves:


- When an object needs to store its state to a previous version.  
- When implementing *undo/redo* functionality without breaking encapsulation.  
- When saving **checkpoints** in application (e.g., Game state, database snapshot).  


### Solution:


- Introduce an **Originator** object that encapsulates its state and business logic.  
- Create a **Memento** object that stores the current Originator's state.
- Introduce a **Caretaker** objects that stores Mementos.  


### Schema


```
+------------------+
|   Memento        |  (Stores State)
|------------------|
| - state          |
+------------------+
        ▲
        │
+------------------+
|  Originator      |  (Creates & Restores State)
|------------------|
| - state          |
| + save_state()   |
| + restore()      |
+------------------+
        ▲
        │
+------------------+
|  Caretaker       |  (Stores Mementos)
|------------------|
| - history        |
| + undo()         |
+------------------+

```


## Key Components


1. **Originator**: This is the object whose state needs to be saved. It creates and 
uses **Mementos**. It also has methods to set is state from **Memento**.  
2. **Memento**: This is the object that stores the internal state of the **Originator**. 
The **Memento** itself is often immutable (ot a least should be treated as immutable 
by the **Originator** and **Caretaker**). It is the "snapshot" of the **Originator**'s state.  
3. **Caretaker**: The objects that is responsible for storing and managing **Mementos**. 
It does not know anything about the internal structure of the **Memento**. It simply 
holds onto it. The **Caretaker** does not have access to the **Memento**'s internal state.  


### Key Relationships and How it Works



## Example1:


### 1. Example 1


- *memento.py*: Text editor that supports save and undo.
    - Originator: 'textEditor'.
    - Memento: 'TextMemento'
    - Caretaker: 'HistoryManager'


### 2. Example 2


- *memento.py*: Game.
    - Originator: 'Game'.
    - Memento: 'GameMemento'.
    - Caretaker: 'SameManger'.
