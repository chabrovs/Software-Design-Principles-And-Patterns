# Creation design pattern: Prototype


## Introduction


The **Prototype** is a creational design pattern that allows to clone existing objects instead of 
creating new ones from scratch. It help in copying complex objects while reducing expensive 
instantiation cost.  


### Problems it solves


- Creating new objects from scratch can be costly.  
- Copying an object manually can be error-prone.  
- Creating multiple instances of an object with slight modifications can be cumbersome.  


### Solution


- Define a prototype interface with a `clone()` method.  
- Implement `clone()` in concrete classes to returns a copy of the object (use deep copy only!).  
- Instead of using `new()`, the client creates copies of an existing object.  


## When to user the pattern 


- Object creation is expensive (e.g., database queries, network responses).  
- Cloning an object is faster than creating a new one.  
- When a class has a large number of configurations and creating a new object with minor changes 
is inefficient.  
- Object prototypes should me copied dynamically at runtime.  


## Disadvantages


- Deep Copy vs. Shallow copy issues: Improper copying may lead to shared mutable states.  
- Not always necessary: If object creating is not expensive, cloning adds unnecessary complexity.  
- Complicates dependency management: some objects should not be copied (e.g. DB connections).  


## Anti-Patterns


### Shallow copy Pitfalls


**Anti-Pattern**: Implementing a shallow copy when a deep copy is required, causing unintended 
shared state between clones.  

**Example**:

```
import copy

class Prototype:
    def __init__(self, items=[]):
        self.items = items  # Shared reference if shallow-copied

    def clone(self):
        return copy.copy(self)  # Shallow copy

# Usage
proto = Prototype([1, 2, 3])
clone = proto.clone()
clone.items.append(4)

print(proto.items)  # Output: [1, 2, 3, 4] → Shared state!
```

**Problem**:

- Changes to the clone affect the original prototype due to shared references.  

**Solution**: Use deep copy for nested and mutable objects.  


### Overusing prototype for simple objects


**Anti-Pattern**: Using the Prototype pattern for objects that are trivial to instantiate.  

**Example**:

```
class User:
    def __init__(self, name):
        self.name = name

    def clone(self):
        return User(self.name)  # Unnecessary for simple objects

# Constructor is already efficient:
user = User("Alice")
clone = User(user.name)  # No need for Prototype!
```

**Problem**:

- Adding unnecessary complexity for objects with cheap constructors.  

**Solution**: Reserve Prototype for objects with expensive instantiation.  


### Tight Coupling to Concrete Class


**Anti-Pattern**: Client depend directly on concrete prototype class instead of interfaces.  

**Example**:

```
class ConcretePrototype:
    def clone(self):
        return ConcretePrototype()  # Clients use this class directly

# Client code
prototype = ConcretePrototype()
clone = prototype.clone()
```

**Problem**:

- Hard to introduce new prototypes without modifying client code.  

**Solution**: Use interface or ABC for prototype.   


### God Prototype (Monolithic Prototype)


**Anti-Pattern**: A single prototype class tries to clone unrelated or overly complex objects.  

**Example**:

```
class MonsterPrototype:
    def __init__(self, health, items, spells):
        self.health = health
        self.items = items  # Items list
        self.spells = spells  # Spells dictionary

    def clone(self):
        return MonsterPrototype(self.health, self.items, self.spells)

class NPCPrototype:
    def __init__(self, dialogue, quests):
        self.dialogue = dialogue
        self.quests = quests  # Quests list

    def clone(self):
        return NPCPrototype(self.dialogue, self.quests)

# A "God Prototype" combining both:
class UniversalPrototype:
    def __init__(self, type, **kwargs):
        self.type = type
        self.data = kwargs  # Stores all possible fields

    def clone(self):
        return UniversalPrototype(self.type, **self.data)
```

**Problem**:

- Violates the SRP. Cloning logic becomes chaotic.    

**Solution**: Creates separate prototypes for distinct object categories.  


### Ignoring Clone Initialization


**Anti-Pattern**: Not allowing post-clone customization, forcing clients to manually reconfigure 
clones.  

**Example**:

```
class Enemy:
    def __init__(self, health, position):
        self.health = health
        self.position = position

    def clone(self):
        return Enemy(self.health, self.position)  # No way to reset position

# Client must modify every clone:
original = Enemy(100, (0, 0))
clone = original.clone()
clone.position = (5, 5)  # Tedious for many properties
```

**Problem**:

- Forcing client to modify the clone.  

**Solution**: Add a post-clone hook for initialization.  

```
def clone(self, **overrides):
    clone = copy.deepcopy(self)
    for key, value in overrides.items():
        setattr(clone, key, value)
    return clone

# Usage:
clone = original.clone(position=(5, 5))  # Customize during cloning
```


### Registry management


**Anti-Pattern**: Using a poorly designed registry management (e.g., global mutable registry).  

**Example**:

```
_prototype_registry = {}  # Global mutable registry

class Shape:
    def clone(self): ...

def register_prototype(key, prototype):
    _prototype_registry[key] = prototype  # No access control

def unregister_prototype(key):
    del _prototype_registry[key]  # Dangerous!
```

**Problem**:

- Registry becomes a global mutable state, risking key collisions or unintended modifications.  

**Solution**: Encapsulate the registry and limit access.  

```
class PrototypeRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, key, prototype):
        self._registry[key] = prototype

    def unregister(self, key):
        del self._registry[key]

    def clone(self, key):
        return self._registry[key].clone()
```


###  Circular References in Clones


**Anti-Pattern**: Prototype with circular references (e.g., a node pointing to itself) causing 
infinite recursion during cloning.  

**Example**:

```
class Node:
    def __init__(self, parent=None):
        self.parent = parent

node = Node()
node.parent = node  # Circular reference

clone = copy.deepcopy(node)  # Stack overflow!
```

**Problem**:

- `deepcopy` fails due to infinite recursion.  

**Solution**: Implement custom `__deepcopy__` logic to handle circular references.  

```
def __deepcopy__(self, memo):
    if id(self) in memo:
        return memo[id(self)]
    copy_obj = Node()
    memo[id(self)] = copy_obj
    copy_obj.parent = copy.deepcopy(self.parent, memo)
    return copy_obj
```
