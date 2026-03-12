from Cleaner import Cleaner

class Finder:
    """
    Class to find the number of occurrences of a target word in the cleaned data.
    """

    def __init__(self, text : str):
        self.data = Cleaner(text)

    def find(self, target: str) -> str:

        cleaned_data = self.data.clean()
        count = 0

        for item in cleaned_data:

            if item == target:
                count = count + 1

        return f'{count} ocurrencias encontradas'
