from typing import List, Dict, Tuple, Any
from utils.utils import field_exists

class FilterEngine:
    """
    Responsible for evaluating if an element matches the provided filters
    """

    def __init__(self, filters: List[Tuple[str, str, any]]):
        self.filters = filters

    def apply_filters(self, element: Dict[str, Any]) -> bool:
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