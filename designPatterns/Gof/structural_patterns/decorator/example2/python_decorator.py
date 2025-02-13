"""
Python has a built-in support for decorator which emphasizes \
working with them. 
"""


from functools import wraps
from typing import Callable


def decorator(original_func: Callable) -> Callable:
    # Transfer Metadata from the original func to the wrapper func.
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        # Add behavior before delegating the call to the original function.
        # HERE: ...

        ...  # Ellipses mean that no actual behavior is added.

        # Delegate the call to the original function, \
        # and save the return data if necessary.
        # HERE:...
        result = original_func(*args, **kwargs)

        # Add behavior after the original function was called.
        # HERE: ...

        ...  # Ellipses mean that no actual behavior is added.

        return result  # Return the result of the original function.

    return wrapper  # Return the 'decorated' object.


def foo(*args, **kwargs):
    """This is the original function."""

    return f"Some result... ARGS={args}, KWARGS={kwargs}"


# Client code
if __name__ == "__main__":
    # Wrap the original function into the decorator.
    decorated_function = decorator(foo)

    # Call the decorate function. \
    # Actually the wrapper is called (see line: 14).

    print(decorated_function(1, name="chabrovs.tech"))
    # STDOUT: Some result... ARGS=(1,), KWARGS={'name': 'chabrovs.tech'}
