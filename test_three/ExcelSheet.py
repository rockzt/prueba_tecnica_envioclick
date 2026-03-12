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