from typing import Any, Dict, List
from FilteringEngine import FilterEngine

class PrioritySorter:
    """
    Sort filtered elements by priority using insertion sort.
    """
    def __init__(self, order: str = 'ASC'):
        self.order = order.upper()

    def _should_swap(self, a: Dict[str, Any], b: dict) -> bool:
        if self.order == 'ASC':
            return a['priority'] < b['priority']
        else:
            return a['priority'] > b['priority']

    def _insertion_sort(self, elements: List[Dict[str, Any]]) -> List[Dict[str, Any]]:

        for index in range(1, len(elements)):

            key_record = elements[index]
            j = index - 1

            while j >= 0 and self._should_swap(elements[j], key_record):
                elements[j + 1] = elements[j]
                j -= 1

            elements[j + 1] = key_record

        return elements

    def sort(self,
             elements: List[Dict[str, Any]],
             filter_engine: FilterEngine
             ) -> List[Dict[str, Any]]:

        filtered_elements = []
        remaining_elements = []

        for element in elements:

            if filter_engine.apply_filters(element):
                filtered_elements.append(element)
            else:
                remaining_elements.append(element)

        sorted_filtered = self._insertion_sort(filtered_elements)

        result = []
        result.extend(sorted_filtered)
        result.extend(remaining_elements)

        return result