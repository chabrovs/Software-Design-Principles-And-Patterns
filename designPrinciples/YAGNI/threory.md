# YANGI (You ain't gonna need it)


## Introduction


The **YANGI (You ain't gonna need it)** principle in software development helps developers avoid 
over-engineering.  

> "Don't implement a feature until it actually needed".  


### Facts:

- A part of: Agile & extreme programming (XP)
- Closely related to: KISS, DRY.  
- Goal: avoid wasting time and effort on unnecessary functionality that may never be used.  



## Violations of YANGI


Signs that YANGI principle is being violated:  
- Writing code for "potential future use" instead of actual needs.  
- Adding configuration options that are not required.  
- Implementing unnecessary abstraction layers until it actually needed.  
- Creating database tables for features that are "planned" but not confirmed.  
- Over-engineering APIs with unused methods "just in case".  


## How to apply YANGI in code: 


1. Implement features only when required.  
2. Avoid premature abstractions. 
3. Keep codebase lean and focused.  
4. Prioritize real requirements (agile development).  


## Common Pitfalls:


- Confusing YANGI with laziness: YAGNI does not mean ignoring valid features needs.  
- Ignoring scalability needs: if scaling is an immediate concert, go for it.  
- Refactoring too late: waiting too long to refactor may increase tech debt.  