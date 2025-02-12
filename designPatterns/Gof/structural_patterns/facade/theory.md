# Structural pattern: Facade


## Introduction


The **Facade Pattern** is a structural patterns that provides a simplified, high-level interface 
to a complex systems. Instead of exposing a complicated set of subsystems, it offers a single 
entry points that make the system easier to use.   


### Problems it solves


- When a system has too many independent classes, making it difficult for clients to use.  
- When a system exposes too much low-level complexity.  
- When there is a need to provide a unified API to multiple systems.  


### Solution


- Introduce a facade class that wraps the complex subsystems and exposes a single API.  
- The client interacts with the Facade, instead of dealing with individual subsystems.  


### Schema


```
+--------------------+
|     Client         |  (Calls Facade)
+--------------------+
        │
        ▼
+--------------------+
|      Facade        |  (Simplifies Access)
|--------------------|
| + simple_method()  |
+--------------------+
        │
        ▼
+--------------------+    +--------------------+
| Subsystem A        |    | Subsystem B        |  (Complex Subsystems)
+--------------------+    +--------------------+
| + complex_method() |    | + complex_method() |
+--------------------+    +--------------------+
```


## Use cases


- Working with complex subsystems and there is a need to simplify interactions.  
- Integrating legacy code that exposes complicated APIs.  
- Designing modular systems, making them easier to use and test.  
- Providing different interfaces for different user types (e.g., Admin vs. Regular User).  


## Components of the Facade Pattern


1. **Facade**: The main class that provides the simplified interface to the client. It knows 
which class in the subsystem are responsible for fulfilling the request and delegates the 
request to the appropriate objects.  
2. **Subsystem classes**: The **Facade** interacts with these classes to handle with client's 
requests. The client, however, does not directly interact with these classes.  


### Key Relationships and How it Works


- The client interacts only with the Facade.  
- The Facade receives the client's request.  
- The Facade then interacts with the appropriate subsystem classes to fulfill the request.  
- The Facade return the result to the client.  


## Examples 


### 1. Example 1


- *without_facade.py*: A module that does not implement the Facade pattern.
- *with_facade.py*: A module that implement the Facade pattern that facilitates the client 
interactions with the complex module.  


## Anti-Patterns


### 1. Unnecessary Facade


**Anti-Pattern**: Implementing the **Facade** when there is no need to simplify a complicated API.


### 2. Monolithic Facade


**Anti-Pattern**: The **Facade** becomes too big, grouping unrelated components together.  

**Example**:

```
class MegaFacade:
    def __init__(self):
        self.payment = PaymentProcessor()
        self.user_manager = UserManager()
        self.inventory = InventorySystem()
        self.logging = LoggingService()
        self.notifications = NotificationService()

    def process_order(self, user, amount):
        self.payment.process_payment(amount)
        self.user_manager.update_user(user)
        self.inventory.check_stock()
        self.logging.log_transaction(user, amount)
        self.notifications.send_notification(user, "Order confirmed!")

```

**Problem**:

- The Facade controls too many unrelated things.  
- High coupling makes it hard to maintain and modify.  


**Solution**:

```
class OrderFacade:
    def __init__(self):
        self.payment = PaymentProcessor()
        self.inventory = InventorySystem()

    def process_order(self, amount):
        self.payment.process_payment(amount)
        self.inventory.check_stock()

class NotificationFacade:
    def __init__(self):
        self.notifications = NotificationService()

    def send_order_notification(self, user):
        self.notifications.send_notification(user, "Order confirmed!")

# ✅ Usage
order_facade = OrderFacade()
notification_facade = NotificationFacade()

order_facade.process_order(100)
notification_facade.send_order_notification("User")
```