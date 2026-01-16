# SPDX-FileCopyrightText: 2026 zccrs
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Legacy Python module for testing SPDX checker with year ranges.

This file demonstrates proper SPDX header formatting with a year range,
simulating a file that has been maintained over multiple years.
"""


class LegacyClass:
    """A legacy class that has been around since 2023."""
    
    def __init__(self, name):
        """
        Initialize the legacy class.
        
        Args:
            name: Name identifier
        """
        self.name = name
        self.created_year = 2023
    
    def get_info(self):
        """
        Get information about this legacy object.
        
        Returns:
            Dictionary with object information
        """
        return {
            "name": self.name,
            "created": self.created_year,
            "maintained_until": 2026
        }


def legacy_function():
    """A function that has been maintained since 2023."""
    print("This is a legacy function from 2023")
    return True


if __name__ == "__main__":
    obj = LegacyClass("test")
    print(obj.get_info())
    legacy_function()
