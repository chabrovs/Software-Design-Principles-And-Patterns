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


## Anti-Patterns:


### 1. Telescoping constructors (instead of using a Builder)


**Anti-Pattern**: Using a constructor with many parameters or multiple overloaded constructors to handle 
object creation.  

**Example**:  

```
class Pizza:
    def __init__(self, size, cheese=False, pepperoni=False, mushrooms=False, onions=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions

# Usage becomes unwieldy:
pizza = Pizza("large", True, True, False, True)
```

**Problem**:

- Hard to read and maintain (what does True, True, False, True mean ?).  
- Force clients to pass `None` or Default for unused parameters.  


### 2. God builder  


**Anti-Pattern**: A single builder class that tries to build unrelated or overly complex objects, 
violating the **SRP**. 

**Example**:

```
class MonsterBuilder:
    def set_head(self, head): ...
    def set_arms(self, arms): ...
    def set_wheels(self, wheels): ...  # Wait, wheels for a monster?
    def build(self): return Monster(...)
```

**Problem**:

- The builder handles conflicting logic (e.g., a monster with wheels).  
- Hard to maintain.  

**Solution**: Split into separate builders for distinct object type.  


### 3. Mutable Product  


**Anti-Pattern**: Allowing the object built by the Builder to change after construction 
(e.g., adding setters).  

**Example**:

```
class Rocket:
    def __init__(self): ...
    def set_fuel(self, fuel): ...  # Mutable after construction

class RocketBuilder:
    def build(self):
        rocket = Rocket()
        rocket.set_fuel("hydrogen")
        return rocket
```

**Problem**:

- Violates the goal of creating immutable, consistent objects.  
- Clients many modify the object in an invalid state.  

**Solution**: Make the product immutable after construction.  


### 4. Overly Complex Fluent Interface  


**Anti-Pattern**: Creating a "fluent" builder with too many chained methods, making it confused 
to use.  

**Example**:

```
class BurgerBuilder:
    def add_patty(self): ...  # Returns self
    def add_cheese(self): ...  # Returns self
    def add_layers(self, n): ...  # Returns self
    # 10 more methods...
```

**Problem**:

- Overwhelms the user with options and chaining steps.  
- Hard to enforce required parameters.  

**Solution**: Simplify the API or split into smaller builders.  


### 5. Ignoring Validation


**Anti-Pattern**: Failing to validate parameters in the `build()` method, leading to 
invalid objects.  

**Example**: 

```
class CarBuilder:
    def __init__(self):
        self.wheels = 0

    def build(self):
        return Car(self.wheels)  # No validation!

builder = CarBuilder()
builder.wheels = 3  # Invalid: cars need 4 wheels
car = builder.build()  # Creates an invalid car
```

**Problem**:

- Produces object in an inconsistent state.  

**Solution**: Validate all parameters in `build()` and raise errors if invalid.  


### 6. Exposing Construction Internals

**Anti-Pattern**: Allowing client to access the product until it is fully built.  

**Example**: 

```
class HouseBuilder:
    def __init__(self):
        self.house = House()  # Exposed too early

    def add_walls(self):
        self.house.walls = 4  # Clients can modify directly!

builder = HouseBuilder()
builder.house.walls = 2  # Unauthorized change
```

**Problem**:

- Client can corrupt the object's state during construction.  

**Solution**: Keep the product private until the `build()` is called.  