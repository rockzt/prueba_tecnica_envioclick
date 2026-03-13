from typing import Any, Dict, List
from FilteringEngine import FilterEngine

class PrioritySorter:
    """
    Sort filtered elements by priority using insertion sort.
    """
    def __init__(self, order: str = 'ASC'):
        """
        Initialize the PrioritySorter with the specified sorting order.
        Args:
            order: A string indicating the sorting order. It can be 'ASC' for ascending or 'DESC' for descending. Default is 'ASC'.
        """
        self.order = order.upper()

    def _should_swap(self, a: Dict[str, Any], b: dict) -> bool:
        """
        Determine if two elements should be swapped based on their priority and the specified sorting order.
        Args:
            a: The first element to compare, represented as a dictionary.
            b: The second element to compare, represented as a dictionary.
        Returns:
            True if the elements should be swapped, False otherwise.
        """

        if self.order == 'DESC':
            return a['priority'] < b['priority']
        else:
            return a['priority'] > b['priority']

    def _insertion_sort(self, elements: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Sort a list of elements using the insertion sort algorithm based on their priority.
        Args:
            elements: A list of dictionaries, where each dictionary represents an element with a 'priority' key.
        Returns:
            A new list of dictionaries sorted by priority according to the specified order.
        """

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
        """
        Sort the provided elements based on their priority after filtering them using the given FilterEngine.
        Args:
            elements: A list of dictionaries, where each dictionary represents an element with a 'priority' key.
            filter_engine: An instance of FilterEngine used to filter the elements before sorting.
        Returns:
            A new list of dictionaries where the filtered elements are sorted by priority according to the specified order
        """

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