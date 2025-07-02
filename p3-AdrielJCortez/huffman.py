from ordered_list import *
from huffman_bit_writer import *
from huffman_bit_reader import *


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # stored as an integer - the ASCII character code value
        self.freq = freq  # the freqency associated with the node
        self.left = None  # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        return type(self) is type(other) and self.char == other.char and self.freq == other.freq

    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if self.freq == other.freq:
            return other.char > self.char
        else:
            return other.freq > self.freq


def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file'''
    list_of_freq = [0] * 256

    with open(filename, "r") as current_file:
        for word in current_file:
            for char in word:
                curr_ord = ord(char)  # This is the index of where we are adding 1 to
                list_of_freq[curr_ord] += 1  # This actually adds the one to that current index

    return list_of_freq


def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''
    ordered_huff_list = OrderedList()  # Lines 40-44 put all the new huffs in an ordered list
    current_idx = 0
    for freq in char_freq:
        if freq != 0:
            create_huff_node = HuffmanNode(current_idx, freq)
            ordered_huff_list.add(create_huff_node)
        current_idx += 1
    while ordered_huff_list.size() > 1:  # create a while loop while the list of huff nodes is not 1
        # merges two branches into one huff.

        branch1 = ordered_huff_list.pop(0)  # the reason why these are both 0 is that after popping the first element
        # the 2nd becomes index 0
        branch2 = ordered_huff_list.pop(0)
        if branch2.char < branch1.char:  # branch two has a lower ask key, so it's the top representing
            new_huff = HuffmanNode(branch2.char, (branch1.freq + branch2.freq))
            new_huff.left = branch1  # one will always be the lower freq
            new_huff.right = branch2  # two will always be greater in freq bc of tiebreaker
            ordered_huff_list.add(new_huff)
        elif branch2.char > branch1.char:  # branch one has a lower ask key
            new_huff = HuffmanNode(branch1.char, (branch1.freq + branch2.freq))
            new_huff.left = branch1
            new_huff.right = branch2
            ordered_huff_list.add(new_huff)

    return ordered_huff_list.pop(0)


def create_code_h(node, code_list, code=""):
    if node.left is None and node.right is None:
        code_list[node.char] = code  # Assign code to the ASCII character index
    else:
        # Traverse the left node with '0' appended to the code
        if node.left is not None:
            create_code_h(node.left, code_list, code + "0")
        # Traverse the right node with '1' appended to the code
        if node.right is not None:
            create_code_h(node.right, code_list, code + "1")


def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the array, with the resulting Huffman code for that character stored at that location'''
    code_list = [""] * 256
    create_code_h(node, code_list)
    return code_list


def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    index = 0
    header = ""
    for freq in freqs:
        if freq != 0:
            header += str(index) + " " + str(freq) + " "
        index += 1
    return header.strip(" ")


def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''

    # This first part is the huffman process that we have to do on the input file
    try:
        in_f = open(in_file, "r")
    except FileNotFoundError:
        raise FileNotFoundError

    text = in_f.read()

    if not text:
        # Handle case where the file is empty
        freq = [0] * 256  # Empty file, so all frequencies are 0
        tree = None  # No tree to create for an empty file
        code_for_chars = [""] * 256  # No characters to encode
        header = ""  # No header needed for an empty file
    else:
        # Handle case where the file is not empty
        freq = cnt_freq(in_file)
        tree = create_huff_tree(freq)
        code_for_chars = create_code(tree)
        header = create_header(freq)

    # Open the output to add 1's and 0's to the bigger compressed file and add the header
    output = open(out_file, "w")
    if text:
        output.write(f"{header}\n")

    # Change outputs name to the correct compressed and add the header
    out_file = out_file[:-4] + "_compressed.txt"
    huff_compress = HuffmanBitWriter(out_file)
    if text:
        huff_compress.write_str(f"{header}\n")

    # In this for loop add to the bigger (0's and 1's) and write the actual bitcode for the actual compressed
    if text:
        for word in text:
            for char in word:
                output.write(code_for_chars[ord(char)])
                huff_compress.write_code(code_for_chars[ord(char)])

    huff_compress.close()
    in_f.close()
    output.close()


def parse_header(header_string):
    freqs = [0] * 256
    list_of_head = header_string.split()  # for example this will be ["32", "3", "97", "4", "99", "2", "100", "1"]

    idx_of_idx_in_freqs = 0  # the list above this will be "32"

    idx_of_freqs = 1  # the list above this will be three

    while idx_of_freqs != (len(list_of_head) - 1):  # checks if idx_of_freqs is len(list) -  1 which would be the last
        # idx in the list
        freqs.insert(int(list_of_head[idx_of_idx_in_freqs]), int(list_of_head[idx_of_freqs]))
        idx_of_idx_in_freqs += 2
        idx_of_freqs += 2

    freqs.insert(int(list_of_head[idx_of_idx_in_freqs]), int(list_of_head[idx_of_freqs]))  # the while loop case there
    # is still going to be one more to insert into the list of freqs

    return freqs


def huffman_decode(encoded_file, decode_file):

    try:
        compressed_file = HuffmanBitReader(encoded_file)
    except FileNotFoundError:
        raise FileNotFoundError

    header = compressed_file.read_str()  # reads the header
    list_of_head = header.split()  # list of the head for edge cases

    if len(list_of_head) == 2:
        decode = open(decode_file, "w")
        for i in range(int(list_of_head[1])):
            decode.write(chr(int(list_of_head[0])))
        decode.close()
        compressed_file.close()

    elif len(list_of_head) == 0:
        decode_file = open(decode_file, "w")
        decode_file.close()
        compressed_file.close()

    else:
        list_of_freqs = parse_header(header)  # creates the list of frequencies

        huff_tree = create_huff_tree(list_of_freqs)  # creates the huffman tree
        decode = open(decode_file, "w")  # open a new file
        current_node = huff_tree  # keep track of the current node to traverse the tree to find the character need
        # to write

        amt_chars = 0  # this finds the amount of characters
        for num in list_of_freqs:
            if num != 0:
                amt_chars += num

        chars_in_decode = 0  # the current amount of characters in the output decoded file
        while chars_in_decode != amt_chars:  # checks if the amount of chars is equal to the expected chars
            # if so then stop adding chars down the tree
            bit = compressed_file.read_bit()
            if bit:
                current_node = current_node.right  # if its true it means a 1 and go the right of the tree
            else:
                current_node = current_node.left  # if it is false it means it's a 0 go to the left

            if current_node.left is None and current_node.right is None:  # checks if we are at a leaf
                character = chr(current_node.char)  # turns the ASCII to an actual char
                decode.write(character)  # adds the character to the file
                current_node = huff_tree  # resets the current node back to the root of the tree
                chars_in_decode += 1  # add one to the amount of chars in the file

        decode.close()
        compressed_file.close()
