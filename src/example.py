# SPDX-FileCopyrightText: 2026 zccrs
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Example Python module for testing SPDX checker.

This file demonstrates proper SPDX header formatting for Python files.
"""


def hello_world():
    """Print a greeting message."""
    print("Hello from SPDX checker test!")


def add_numbers(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b


if __name__ == "__main__":
    hello_world()
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
