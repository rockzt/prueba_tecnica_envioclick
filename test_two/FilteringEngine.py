from typing import List, Dict, Tuple, Any
from utils.utils import field_exists

class FilterEngine:
    """
    Responsible for evaluating if an element matches the provided filters
    """

    def __init__(self, filters: List[Tuple[str, str, any]]):
        """
        Initialize the FilterEngine with a list of filters.
        Args:
            filters: A list of tuples, where each tuple contains:
                - field: The field name to filter on.
                - operator: The comparison operator (e.g., '=', '>', '<', '>=', '<=', '!=').
                - value: The value to compare against.
        """
        self.filters = filters

    def apply_filters(self, element: Dict[str, Any]) -> bool:
        """
        Apply the filters to the given element and determine if it matches all criteria.
        Args:
            element: A dictionary representing the element to be evaluated against the filters.
        Returns:
            True if the element matches all filters, False otherwise.
        """
        for field, operator, value in self.filters:
            field_found = field_exists(element, field)

            if not field_found:
                return False

            element_value = element[field]

            if operator == "=":
                if element_value != value:
                    return False

            elif operator == ">":
                if element_value <= value:
                    return False

            elif operator == "<":
                if element_value >= value:
                    return False

            elif operator == ">=":
                if element_value < value:
                    return False

            elif operator == "<=":
                if element_value > value:
                    return False

            elif operator == "!=":
                if element_value == value:
                    return False

            else:
                raise ValueError("Unsupported operator!")

        return True