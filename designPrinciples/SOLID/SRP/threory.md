# Single Responsibility Principle (SRP)


## Introduction


The SRP focuses on ensuring that a class, method, or function has only one reason to change, 
meaning it should be responsible for only a single part of the software functionality.  


## Definition


A SRP states: 
> A class should have only one reason to change.   

This means that a class, function, or module should focus on doing one thing and doing it well. 
If it has more than one responsibility, it becomes harder to maintain and extend.  

Real-Wold analogy: Swiss Army knife vs. a screwdriver. In software, fallowing SRP ensures that 
components are focused, and efficient like that screwdriver.   


### Understanding "Responsibility" in SRP:


A *responsibility* can be thought of as:  
- **a part of functionality**: a distinct reason why a class or module might need to change.  
- **a stakeholder's concern**: a responsibility often aligns with the concerns of a specific stakeholder 
(e.g., database admins, end-users, auditors).  

**Examples os responsibilities**:  
- handling user's input.  
- processing business logic.  
- interacting with database. 


## How to implement SRP 


## Common violations of SRP


1. **Bloated classes**: Classes that handle multiple unrelated tasks.  
2. **Mixed responsibilities in functions**. 
3. **God objects**: Classes that know too much about too many parts of the system.  
4. **Monolithic modules**: Modules that contain unrelated logic (e.g., mixing DB queries and business logic). 


## How to adhere to the SRP in code ?


### 1. Decomposition:


1. Identify responsibilities within a module, class or a function.  
2. If any of there entities are overloaded with unrelated responsibilities decompose them 
into separate modules, classes, or function.  
3. If necessary, create appropriate module hierarchy, add some modules to the PATH or 
add additional path to the PATH, .pth, or environment path, site-packages.  
Note Python namespace (module) resolution order is following:
    1. Current working directory.  
    2. Python virtual environment path `PYTHONPATH`.
    3. Standard library.
    4. `.pth` files. 
    5. site-packages. 


***See example # 3***


### 2. Use Interfaces or Abstract Base Classes:


1. Identify responsibilities.  
2. Create separate interfaces (or abstract base classes) for each responsibility.  
3. Implement these interfaces in derived concrete subclasses.   

***See example # 4***


### 3. Apply Composition over Inheritance:


1. Identify distinct responsibilities.  
2. Use helper classes or services to handle each responsibility.  
3. Compose the primary class using these helper classes.  

***See example # 5***


### 4. Use design Patterns:


Certain design patterns naturally promote Singe Responsibility Principle 
by isolating responsibilities.  
For example:  
1. **Strategy Pattern:** Isolate algorithms and behaviors into separate classes.  
2. **Factory Pattern:** Encapsulates object creation logic in a dedicated factory class.  
3. **Observer Pattern:** Separate event notification logic from business logic.  
4. **Template Method Pattern:** Define's algorithm's structure in a class (usually abstract base class) 
and delegate specific steps to subclasses. 


### 5. Use services for Business logic (especially in web-applications):


1. Create a separate layer (class or module) for business logic.  
2. Move business logic from models and controller logic into the business logic.   
*Note: It is a good practice to isolate queries form the business logic layer into an additional infrastructure layer.*  
3. Create API for business logic. The orchestrating layer (e.g., controller must call business logic's API services). 
(e.g., you can create application services that use the domain logic, thereby these application services may act 
as API for a controller).

**Example of layered architecture in a Django Project:**
```
my_app/
├── application/
|   ├── service.py          # Business logic API as services. (Lower-level orchestrating layer.)
|   └── __init__.py
├── domain/
│   ├── services.py         # Business logic.
│   └── __init__.py
├── infrastructure/
│   ├── repositories.py     # Repository implementation.
│   ├── third_party_api.py  # Third party API calls.
│   └── __init__.py
├── models.py               # Django ORM models
├── views.py                # Higher level orchestrating layer. 
└── __init__.py
```


### 6. Leverage dependency injection:


1. Create dependencies in a higher-level component.  
2. Inject dependencies into a lover-level component.  


***See example # 6***


### 7. Isolate configuration and constants: 


1. Move configuration and constant into a separate file or class from 
the business logic implementation.  
2. Import configuration details or constant from another module or class by request. 


***See example # 7***


### 8. Decompose functions:


1. Identify functions that have multiple responsibilities.  
2. Separate these responsibilities into different function.  
3. (If required) Create an orchestrating function to control execution flow of lower-level function.  


### 9. Modularize code: 


1. Separate code into modules based on responsibility.
Each module should focus on a specific task 
(e.g., `auth.py` for authentication, `report.py` for sending reports, etc.). 