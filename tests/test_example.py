# SPDX-FileCopyrightText: 2026 zccrs
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Test suite for example modules.

This file demonstrates proper SPDX header formatting for test files.
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from example import add_numbers, hello_world
    from legacy import LegacyClass, legacy_function
except ImportError as e:
    print(f"Import error: {e}")
    # Continue anyway for SPDX header testing purposes


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    print("test_add_numbers passed")


def test_legacy_class():
    """Test the LegacyClass."""
    obj = LegacyClass("test_object")
    info = obj.get_info()
    assert info["name"] == "test_object"
    assert info["created"] == 2023
    assert info["maintained_until"] == 2026
    print("test_legacy_class passed")


def test_legacy_function():
    """Test the legacy_function."""
    result = legacy_function()
    assert result is True
    print("test_legacy_function passed")


if __name__ == "__main__":
    print("Running tests...")
    test_add_numbers()
    test_legacy_class()
    test_legacy_function()
    print("All tests passed!")
