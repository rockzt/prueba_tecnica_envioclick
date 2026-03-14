from typing import List, Dict, Tuple, Any

from FilteringEngine import FilterEngine
from PrioritySorter import PrioritySorter


class DataProcessor:
    """
    Coordinates filtering and sorting of a dataset based on
    dynamic filters and priority ordering.
    """

    def __init__(self, filters: List[Tuple[str, str, Any]], order: str) -> None:
        """
        Initialize the processor.

        Args:
            filters: List of filter conditions.
            order: Sorting order ('ASC' or 'DESC').
        """
        self.filter_engine = FilterEngine(filters)
        self.sorter = PrioritySorter(order)

    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Apply filtering and sorting to the dataset.

        Args:
            data: List of dictionary records.

        Returns:
            List of processed records.
        """
        return self.sorter.sort(data, self.filter_engine)