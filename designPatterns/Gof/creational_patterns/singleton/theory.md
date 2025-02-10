# Creation Pattern: Singleton


## Introduction


The **Singleton** is a creational design pattern that ensures a class has only **one instance** 
and provides a global access point to that instance.    


### Problems it solves


- Ensures **only one instance** of a class exists (e.g., database connection, logging service).  
- Prevents **duplicate instances** that may cause inconsistent states or performance issues.  


### Solution


- Restrict instantiation to a single instance.  
- Provide a global access method to retrieve this instance.  


## Examples:


### 1. Example 1


- *singleton.py*: Basic Singleton Using a Class Variable. 


### 2. Example 2


- *singleton.py*: Singleton by using decorator.  


### 3. Example 3


- *singleton.py*: Singleton by using a Meta class.  


## Anti-Patterns


### Global state abuse


**Anti-Pattern**: Using Singleton to create a mutable global state accessible everywhere.  
**Example**:

```
class AppConfig:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.debug_mode = False  # Mutable global state
        return cls._instance

# Usage:
config = AppConfig()
config.debug_mode = True  # Anywhere else: AppConfig().debug_mode = False
```

**Problem**: Creates hidden dependencies and unpredictable size effects 
(e.g., changing `debug_mode` in one place affects all components).  

**Solution**: Avoid mutable global state. Use dependency injection or immutable configurations.  


### Overusing Singleton for Utility Classes.


**Anti-Pattern**: Forcing stateless utility classes into Singletons. 

**Example**:

```
class MathUtils:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def add(a, b):
        return a + b

# Usage: MathUtils().add(2, 3)
```

**Problem**:

- Unnecessary overhead for a stateless class.  
- Static method would suffice.  

**Solution**: Use static methods or modules instead (e.g., `math_utils.py`).


### Ignoring Thread-Safety


**Anti-Pattern**: Assuming Singleton works in multithreaded environments without 
synchronization.  

**Example**:

```
class Database:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# Thread 1: Database() | Thread 2: Database() → May create two instances.
```

**Problem**:

- Race conditions in multithreaded code.  

**Solution**: Use thread-safe initialization (e.g., locks, `@synchronized` decorator, etc.).

**Example of thread-safe Singleton**:

```
from threading import Lock

class Logger:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.logs = []
        return cls._instance

    def log(self, message):
        self.logs.append(message)
```


### Violating the SRP


**Anti-Pattern**: Mixing Singleton logic with Business logic in the same class. 

**Example**:

```
class Logger:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message):
        self.logs.append(message)  # Combines Singleton + logging logic
```

**Problem**:

- The class managed it own instance and handled logging.  


**Solution**: Create Singleton management for business logic 
(e.g., use decorator or Meta class for Singleton logic).  


### Singleton sub-classing


**Anti-Pattern**: Trying to subclass a Singleton, leading to unexpected behavior.

**Example**:

```
class SingletonBase:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class Child(SingletonBase):
    pass

# Usage:
base = SingletonBase()
child = Child()
print(base is child)  # Output: False (violates Singleton for the base class)
```

**Problem**:

- Sub-classing breaks the Singleton guarantee for the parent class.


**Solution**: Avoid sub-classing Singletons. Use composition or dependency injection.


### Singleton for Heavy Resources


**Anti-Pattern**: Using Singleton for expensive resources (e.g., database connections) without cleanup.

**Example**:

```
class DatabaseConnection:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.connection = connect_to_db()  # Expensive!
        return cls._instance

# No way to close the connection or reset the Singleton.
```

**Problem**:

- Resource leaks (e.g., unclosed connections).
- Inflexible for testing or reconfiguration.


**Solution**: Use connection pooling or dependency injection to manage resources.


### Testing mistakes


**Anti-Pattern**: Relying on Singleton instances in unit tests.

**Example**:

```
class AnalyticsTracker:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# In tests:
def test_analytics():
    tracker = AnalyticsTracker()
    tracker.track("test_event")  # Affects other tests using the same instance.
```

**Problem**:

- Shared state across tests leads to flaky or interdependent tests.


**Solution**: Use mocking frameworks (e.g., `unittest.mock`) or reset the Singleton state between tests.