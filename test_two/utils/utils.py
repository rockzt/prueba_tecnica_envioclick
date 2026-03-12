"""
    Utility module for common helper functions.
"""

from typing import Dict, Any

def field_exists(element: Dict[str, Any], field: str) -> bool:
    """
    Check if a field exists in the given element.
    Args:
        element: The dictionary to check for the field.
        field: The field name to look for.
    Returns:
        True if the field exists in the element, False otherwise.
    """
    for key in element:
        if key == field:
            return True

    return False