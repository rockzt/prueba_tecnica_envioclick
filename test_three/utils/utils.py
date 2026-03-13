"""
    Utility functions.
"""

def _validate_position(self, row: int, col: int) -> None:
    """
    Validate if a given cell position exists.

    Raises:
        IndexError: If the position is outside the sheet.
    """
    if not (0 <= row < self.rows and 0 <= col < self.cols):
        raise IndexError("Cell position out of range")