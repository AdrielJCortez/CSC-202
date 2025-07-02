from sys import argv
from stack_array import *


class Vertex:
    def __init__(self, in_degree, adj_list):
        '''Add whatever parameters/attributes are needed'''
        self.in_degree = in_degree
        self.adj_list = adj_list

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * one vertex per line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    # for this code _out_ is the one leading to the next point, and _in_ is the one receiving
    dic = {}
    if len(vertices) == 0:
        raise ValueError("input contains no edges")
    if len(vertices) % 2 != 0:
        raise ValueError("input contains an odd number of tokens")
    else:
        for i in range(0, len(vertices), 2):
            j = i + 1
            if vertices[i] not in dic:  # check if _out_ is in the dictionary
                dic[vertices[i]] = Vertex(0, [vertices[i + 1]])  # set adj_list to _in_

            elif vertices[i] in dic:  # otherwise _out_ is in the dic already
                dic[vertices[i]].adj_list.append(vertices[j])  # update the adj lists

            if vertices[j] not in dic:  # if _in_ is not in the dic yet
                dic[vertices[j]] = Vertex(1, [])  # create a vertex with an in degree of 1

            elif vertices[j] in dic:  # otherwise _in_ is in the dict
                dic[vertices[j]].in_degree += 1  # update the in degree

    my_stack = Stack(len(vertices))
    for key in dic:
        if dic[key].in_degree == 0:  # get the value of the current item in the dictionary and if it is 0
            my_stack.push(key)

    ordering_list = []
    while not my_stack.is_empty():  # while the stack is not empty
        curr_top = my_stack.pop()  # pop the top vertex off (it is a string in this case)
        ordering_list.append(curr_top)  # then put it into our ordering_list
        adj = dic[curr_top].adj_list  # access the adj lists from the current vertex
        for vertex in adj:  # iterate over each vertex in the adjacent list
            dic[vertex].in_degree -= 1  # subtract one from each in degree for each adj
            if dic[vertex].in_degree == 0:  # if any in degrees equal 0 after taking away 1 push it onto the stack
                my_stack.push(vertex)

    if len(ordering_list) != len(dic):  # the reason why we check if the ordering list is the same length as the dic,
        # it means that every vertex got arranged correctly with no vertices not ever entering the stack.
        raise ValueError("input contains a cycle")

    ordering = "\n".join(ordering_list)  # join the ordering together
    return ordering


# 100% Code coverage NOT required
def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG.  Use this code 
       if you want to run tests on a file with a list of edges'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()

    vertices = []
    for line in f:
        vertices += line.split()

    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
