"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
        Machine to create unique incrementing serial numbers.  It is instantiated with a path to a file on disk that contains words, one word per line

        it reads that file, and makes an attribute of a list of those words
        it prints out “[num-of-words-read] words read”
        
        it provides a method, random(), which returns a random word from that list of words

        Note: the random method should not re-read the list of words each time; it should work with the already-read-in list of words.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.read_file()

    def read_file(self):
        f = open(self.file_path, 'r')
        self.file_lines = f.readlines()

    def random(self):
        l = len(self.file_lines)
        return self.file_lines[random.randint(0, l)].replace('\n', '')

class SpecialWordFinder(WordFinder):
    def __init__(self, file_path):
        super().__init__(file_path)

    def read_file(self):
        super().read_file()

    def random(self):
        return super().random() + " but I am Special"

wf = WordFinder("words.txt")
print(wf.random())

wf_special = SpecialWordFinder("words.txt")
print(wf_special.random())