from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("test_words.txt")
    3 words read
    >>> wf.words
    ['cat', 'dog', 'porcupine']
    """

    def __init__(self, filepath):
        """Create Word Finder by reading in words from filepath"""

        self.words = self._read_file(filepath)
        print(f"{len(self.words)} words read")

    def _read_file(self, filepath):
        """Reads a file and returns list of the file lines"""

        words = []
        file = open(filepath, "r")
        for line in file:
            if self._is_valid(line):
                words.append(line.strip())
        file.close()
        return words

    def _is_valid(self, line):
        """Determines if line should be included. Always returns True."""

        return True

    def random(self):
        """Returns random word"""

        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """SpecialWordFinder: WordFinder that excludes special cases.

    >>> wf = SpecialWordFinder("special_words.txt")
    4 words read
    >>> wf.words
    ['kale', 'parsnips', 'apple', 'mango']
    """

    def _is_valid(self, line):
        """Returns False for lines that start with '#' or blank lines"""

        return not (line.startswith("#") or line == "\n")
