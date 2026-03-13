from Cleaner import Cleaner

class Finder:
    """
    Class to find the number of occurrences of a target word in the cleaned data.
    """

    def __init__(self, text : str):
        """
       Initialize the Finder with the input text and create a Cleaner instance to process it.

       Args:
              text: The input text to be cleaned and searched.
       """
        self.data = Cleaner(text)

    def find(self, target: str) -> str:
        """
        Find the number of occurrences of the target word in the cleaned data.
        Args:
            target: The word to search for.
        Returns:
            A string indicating the number of occurrences found.
        """
        target = target.lower()
        cleaned_data = self.data.clean()
        count = 0

        for item in cleaned_data:
            if item == target:
                count = count + 1

        return f'{count} ocurrencias encontradas'
