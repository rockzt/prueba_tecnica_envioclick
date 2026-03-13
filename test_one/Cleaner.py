class Cleaner:
    """
        Class to clean the input data, removing punctuation and converting to lowercase.
    """
    def __init__(self, input_data : str):
        """
        Initialize the Cleaner with the input data and split it into a list of words.
        Args:
            input_data: The raw input string to be cleaned.
        """
        self.input_data = input_data.split()

    def clean(self) -> list[str]:
        """
        Clean the input data by removing punctuation and converting to lowercase.
        Returns:
            A list of cleaned words.
        """
        cleaned_data = [item.strip('.').strip(',').lower() for item in self.input_data]

        return cleaned_data