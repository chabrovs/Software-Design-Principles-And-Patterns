# The "HollyWood Principle"


## Introduction


The **HollyWood Principle** is a software design principle that encourages Inversion Of Control (IoC) 
by delegating responsibilities of managing the control flow to higher-level components 
(e.g., Frameworks, Orchestrion modules or layers).  

Its motto: "*Don't call us, we'll call you.*", embodies the idea of designing systems where 
lower-level components do not control the flow of execution but instead rely on higher-level components to manage them.  

This principle is frequently employed by frameworks, event-driven systems, dependency injections, and various design patterns 
like Template method and Observer. By adhering the HollyWood principle, developers can create systems that are modular,
 flexible and easier to maintain.  


## Definition


The **HollyWood Principle** advocates for: 
- Lower-level components should not directly call or depend on higher-level components.  
- Instead, higher-level components should control the flow of execution by calling lower-level components as needed.  


### Relation to Inversion-Of-Control (IoC).

The **HollyWood Principle** is an implementation of Inversion-Of-Control (IoC), where control over program control flow
is inverted from the traditional approach. IoC decouples components, delegating responsibility for 
orchestrating actions to a framework or higher-level logic.  


## How it works


- **Traditional control flow:** components call each other components directly, managing the flow of execution themselves.  
Example: a class explicitly invoking other class's methods.  

- **HolloWood control flow:** The flow of execution is managed by an external components 
(e.g., framework, orchestrating layer (i.e. application layer is a layered architecture or control module in MVC architecture)).  
Lower-layer components wait to be invoked by the orchestrating layer.  


## Pros and Possible Pitfall


### Pros:


1. **Promotes decoupling**: Components are loosely coupled, making system more modular and extensive.  
2. **Improves reusability**: Lower-level components can be reused in different context 
because they are not tightly bounded to specific implementations.  
3. **Supports framework development**.  
4. **Isolates control flow logic of a program**.  


### Pitfalls:

1. **Over-Reliance on frameworks**: Blind reliance of frameworks can lead to complexity or reduced understanding of 
underlying mechanisms.    
2. **Event Spaghetti**: In event-driven systems excessive event chaining can make the flow hard to follow.  
3. **Steep Learning Curve**: Understanding how framework or other flow controllers change the execution flow may be complex.   
4. **Debugging complexity**: Debugging code managed by a framework of IoC container can be challenging due to hidden flows.  


## Where this principle is applied


- **Frameworks**: In frameworks like Django, Spring, React, developers implement specific methods or handlers, and 
the framework decides when to invoke them.  
Example: Django's view functions are called by the framework based on incoming HTTP request.  
- **Event-Driven Systems**: Components register for events, and when an event occurs, 
the event manager calls the appropriate handler.  
- **Dependency Injection**: The control over dependency creation and injection is inverted, 
with the container managing dependencies.
- **Design Patterns**: 
    - **Template method**: ...  
    - **Observer pattern**: observers register themselves and called when the observable's state changes.  


## Examples:


### 1. Example 1


- *withoutHollywood.py*: Show the example without adhering the **Hollywood Principle**. 
- *withHollywood.py*: Shows the example that adheres to the **Hollywood Principle**.  

### 2. Example 2

- *eventDrivenProgramming.py*: Shows that event driven programming adheres the Hollywood principle by default.  


### 3. Example 3.

In Example we will show way the **Hollywood Principle** can be achieved.  

- *abstractClassAndPolymorphism.py*: Concrete classes implement the interfaces (abstract classes) but do not control the 
program execution flow. The program execution control flow is delegated to a higher-level component (the Framework class). 

- *dependencyInjection.py*: Dependency injection (DI), a higher-level component (like framework or orchestrator) provides 
dependencies to lower-level components. This ensures that the lower-level component are not in control of 
their dependencies or the flow.  
 
- *callbacks.py*: A callback is a function that is passed to another (a high order) function or component to be invoked 
later. This achieves the **Hollywood Principle** because the control of when the callback is actually executed 
resides with the higher-level component.  

- *observationPattern.py*: The **Observer Pattern** is a design pattern where an object (subject or observable) maintains 
a list of dependents (observers) and notifies them of any state changes.  
This naturally implement the **Hollywood Principle** because the subject (observable) calls the observers when necessary.  
The **Observation Pattern** is common for Event-driven systems and Reactive programming paradigm.  

- *framework.py*: Frameworks often implement the **Hollywood Principle** by calling user-defined methods 
(e.g., handlers or callbacks) at the appropriate time. This is common for web frameworks, GUI frameworks, 
and Job schedulers.  

The Flask framework manages the HTTP request/response flow and calls the home function only when a request is made to the root URL.   

- *templateMethodPattern.py*: The **Template pattern** defines the structure of an algorithm in a base class and lets subclasses 
implement specific steps. The higher-level logic controls the flow of execution, while lower-level classes provide 
specific behavior.

- *eventDrivenProgramming.py*: Event-driven systems naturally implement the **Hollywood Principle**. Components register for events, 
and the system manages the flow of when and how these components are invoked.  

- *dependencyInjectionFrameworks.py*: ...