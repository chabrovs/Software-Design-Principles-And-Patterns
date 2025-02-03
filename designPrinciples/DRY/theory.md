# DRY (Don't Repeat Yourself)


## Introduction


**DRY (Don't repeat yourself)** is a software development principle that suggests that 
__code should not have duplicated functionality__. The idea is to keep the codebase as 
simple as possible by eliminating redundancy and duplication. The goal is to reduce 
complexity and improve maintainability by ensuring that each piece of knowledge is expressed 
in a single, unambiguous way within the system.  

**The DRI applies to**: Code, Database schemas, configuration files, documentation and system 
design.  

The DRY is closely related to the SRP and the OCP, and aims to reduce the amount of duplicated 
code __by creating abstractions that can be reused across the system__.  



## Common Violations:


- **Code duplication**: Copy-pasting the same logic in multiple places.  
- **Hardcoded values**: Repeating constant values throughout the code instead of using variables 
and configurations.  
- **Repeated SQL queries**: Writing the same SQL queries in multiple places.  
- **Multiple data representations**: The same data represented in different forms.  


## How to adhere to the DRY in code:


1. Use functions to avoid repeated logic.  
2. Apply abstraction and encapsulation.  
3. Use data structures efficiently.  
4. Centralize constants and configurations.  
5. Remove redundant comments and documentation.  


## DRY beyond code: Applying DRY in software architecture.  

|Area|How to apply DRY|
|-|-|
|DB schema design|Normalize table to avoid data duplication (Use Normal Forms)|
|Configurations|Use `.env` or config files instead of hardcoding values.|
|APIs|Use a Shared Base Controller instead of duplication request handling logic.|
|Documentation|Avoid duplication logic in comments|



## Common PitFalls with DRY:


- **Over-Engineering**: avoid making code so reusable that it becomes hard to understand.  
- **Violating YAGNI Principle**.