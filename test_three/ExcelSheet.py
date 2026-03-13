from typing import Any, List


class ExcelSheet:
    """
    Basic representation of an Excel-like sheet using rows and columns.
    """

    def __init__(self, rows: int, cols: int) -> None:
        """
        Initialize the sheet with empty cells.

        Args:
            rows: Number of rows.
            cols: Number of columns.
        """
        self.rows = rows
        self.cols = cols
        self.sheet: List[List[Any]] = [[None for _ in range(cols)] for _ in range(rows)]


    def _validate_position(self, row: int, col: int) -> None:
        """
        Validate if a given cell position exists.

        Raises:
            IndexError: If the position is outside the sheet.
        """
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Cell position out of range")

    def insert(self, row: int, col: int, value: float) -> None:
        """
        Insert information into a cell.

        Args:
            row: Row index.
            col: Column index.
            value: Value to store.
        """
        self._validate_position(row, col)

        if self.sheet[row][col] is not None:
            raise ValueError("Cell already contains data. Use update instead.")

        self.sheet[row][col] = value

    def update(self, row: int, col: int, value: float) -> None:
        """
        Update information in a cell.

        Args:
            row: Row index.
            col: Column index.
            value: New value.
        """
        self._validate_position(row, col)
        self.sheet[row][col] = value

    def has_value(self, row: int, col: int) -> bool:
        """
        Validate if a cell contains information.

        Args:
            row: Row index.
            col: Column index.

        Returns:
            True if the cell has data, otherwise False.
        """
        self._validate_position(row, col)
        return self.sheet[row][col] is not None

    def preview(self) -> None:
        """
        Print a preview of the sheet.
        """

        header = "    "
        for col in range(self.cols):
            header += f"{col}     "
        print(header)

        for row_index, row in enumerate(self.sheet):
            line = f"{row_index} | "

            for value in row:
                cell = "" if value is None else value
                line += f"{cell}    "

            print(line)

    def sum_row(self, row: int) -> None:
        """
        Retrieve all elements in a row and print the sum of numeric values.

        Args:
            row: Row index.

        Returns:
            Sum of numeric values.
        """
        if not(0 <= row < self.rows):
            raise IndexError("Row index out of range")

        total = sum(value for value in self.sheet[row] if isinstance(value, float))
        return total


    def sum_column(self, col: int) -> None:
        """
        Retrieve all elements in a column and print the sum of numeric values.

        Args:
            col: Column index.

        Returns:
            Sum of numeric values.
        """
        if not (0 <= col < self.cols):
            raise IndexError("Column out of range")

        total = sum(
            row[col] for row in self.sheet if isinstance(row[col], float)
        )

        return total