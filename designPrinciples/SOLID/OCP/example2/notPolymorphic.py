def calculate_discount(customer_type: str, amount: float) -> float:
    if customer_type == "regular":
        return round(amount * 0.1, 2) 
    elif customer_type == "premium":
        return round(amount * 0.2, 2)
    
    return 0.0
    

if __name__ == "__main__":
    print(calculate_discount("regular", 110.2))
    print(calculate_discount("premium", 110.2))


# Problem:
# In order to add a new customer type and the discount fot this type \ 
# you need to change code in the existing function 'calculate_discount' \
# This violates the OCP. 
# See 'example2/polymorphic.py' on how to fix this problem.  