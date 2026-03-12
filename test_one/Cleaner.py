class Cleaner:
    """
        Class to clean the input data, removing punctuation and converting to lowercase.
    """
    def __init__(self, input_data : str):
        self.input_data = input_data.split()

    def clean(self) -> list[str]:

        cleaned_data = [item.strip('.').strip(',').lower() for item in self.input_data]

        return cleaned_data