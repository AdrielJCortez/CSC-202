from hash_quad import *
import string


class Concordance:

    def __init__(self):
        self.stop_table = None  # hash table for stop words
        self.concordance_table = None  # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        try:
            with open(filename, "r") as file:
                stop_words = file.read().split()
            for word in stop_words:
                self.stop_table.insert(word)
        except FileNotFoundError:
            raise FileNotFoundError

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table,
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        (The stop words hash table could possibly be None.)
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.concordance_table = HashTable(191)
        try:
            curr_line = 1
            with open(filename, "r") as file:
                for line in file:
                    # remove apostrophe characters
                    line = line.lower()
                    line = line.replace("'", "")

                    # replace punctuation with spaces
                    for char in string.punctuation:
                        line = line.replace(char, " ")

                    words = line.split()

                    for word in words:
                        if word.isalpha() and not self.stop_table.in_table(word):
                            if not self.concordance_table.in_table(word):  # if word is not in the table
                                self.concordance_table.insert(word, [str(curr_line)])
                            else:  # if word is in the concordance table
                                occurrences = self.concordance_table.get_value(word)
                                if str(curr_line) != occurrences[-1]:  # otherwise check if we have to update lines
                                    occurrences.append(str(curr_line))
                    curr_line += 1  # Increment the line counter after processing each line

        except FileNotFoundError:
            raise FileNotFoundError

    def write_concordance(self, filename):
        """Write the concordance entries to the output file(filename).
        See sample output files for format."""
        words_to_write = self.concordance_table.get_all_keys()

        # sort the words alphabetically
        words_to_write.sort()

        # write the words and their values to the output file
        with open(filename, "w") as file:
            for word in words_to_write:
                value = " ".join(self.concordance_table.get_value(word))
                file.write(word + ":" + " " + value + "\n")
