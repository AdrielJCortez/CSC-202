from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key):
        '''Add other Attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.visited = False
        self.color = None


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        # This method should call add_vertex and add_edge!!!
        self.graph_contents = {}
        with open(filename) as file:
            text = file.read()
            vertices = text.split()
            for i in range(0, len(vertices), 2):
                j = i + 1
                v1 = vertices[i]
                v2 = vertices[j]
                self.add_vertex(v1)
                self.add_vertex(v2)
                self.add_edge(v1, v2)

    def add_vertex(self, key):
        # Should be called by init
        '''Add vertex to graph only if the vertex is not already in the graph.'''
        if key not in self.graph_contents:
            self.graph_contents[key] = Vertex(key)

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex ID's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.graph_contents[v1].adjacent_to.append(v2)
        self.graph_contents[v2].adjacent_to.append(v1)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''
        if key in self.graph_contents:
            return self.graph_contents[key]
        return None

    def get_vertices(self):
        '''Returns a list of ID's representing the vertices in the graph, in ascending order'''
        vertices = list(self.graph_contents.keys())
        return sorted(vertices)

    def conn_components(self):
        '''Return a Python list of lists.  For example: if there are three connected components
           then you will return a list of three lists.  Each sub list will contain the
           vertices (in ascending alphabetical order) in the connected component represented by that list.
           The overall list will also be in ascending alphabetical order based on the first item in each sublist.'''
        # This method MUST use Depth First Search logic!
        current_num_items = 0
        list_of_lists = []
        while current_num_items != len(self.get_vertices()):  # the reason for this is because that means we haven't gone through every subgraph
            dfs = self.dfs(self.get_vertices())
            list_of_lists.append(sorted(dfs[0]))  # dfs returns a tuple so [0] is a list
            current_num_items += dfs[1]  # [1] is a number
        self.reset_vertex(self.get_vertices())  # this resets all my visited
        return sorted(list_of_lists)

    def dfs(self, list_of_ver):
        output_of_graph = []
        my_stack = Stack(len(list_of_ver))  # create a stack
        curr_idx = 0
        for ver in list_of_ver:  # the reason for this for loop is to find the min point in a graph
            # (since there can be multiple subgraphs)
            if self.get_vertex(ver).visited is False:
                break
            curr_idx += 1
        my_stack.push(list_of_ver[curr_idx])  # push small onto the stack
        self.get_vertex(list_of_ver[curr_idx]).visited = True  # set its visited to true
        output_of_graph.append(list_of_ver[curr_idx])  # put it into our output
        num = 0
        while not my_stack.is_empty():  # while the stack is not empty
            curr_key = my_stack.peek()
            curr_ver = self.get_vertex(curr_key)  # access the curr_vertex
            if self.dead_end(curr_ver.adjacent_to):  # checks if the curr_vertex is at a dead end
                my_stack.pop()  # pop until we are not at a dead end
                num += 1
            else:  # otherwise it is not at a dead end
                sorted_adj_list = sorted(curr_ver.adjacent_to)
                i = 0
                while True:
                    if self.get_vertex(sorted_adj_list[i]).visited is False:  # checks if smallest was visited
                        my_stack.push(sorted_adj_list[i])
                        self.get_vertex(sorted_adj_list[i]).visited = True
                        output_of_graph.append(sorted_adj_list[i])
                        break
                    i += 1
        return output_of_graph, num

    def dead_end(self, adj_list):
        for v in adj_list:
            if self.graph_contents[v].visited is False:
                return False
        return True

    def is_bipartite(self):
        '''Return True if the graph is bipartite, False otherwise.'''
        # This method MUST use Breadth First Search logic!
        current_num_items = 0
        while current_num_items != len(self.get_vertices()):  # while the points we have gone too is not equal to all the points
            y = self.bfs_color(self.get_vertices())  # color function to see if it is bipartite
            current_num_items += y[0]  # y bfs color is returning a tuple so this is the number
            if y[1] is False:  # this is a boolean
                return False
        self.reset_vertex(self.get_vertices())
        return True

    def bfs_color(self, list_of_verts):
        queue = Queue(len(list_of_verts))
        current_idx = 0 # this is to find the starting point in the graph
        for ver in list_of_verts:  # find the start of the graph
            if self.get_vertex(ver).color is None:
                break
            current_idx += 1
        queue.enqueue(list_of_verts[current_idx])
        if self.graph_contents[list_of_verts[current_idx - 1]].color is not None:  # if the previous node is already colored
            if self.graph_contents[list_of_verts[current_idx - 1]].color == "P":  # change the starting color so code doesn't return false
                self.graph_contents[list_of_verts[current_idx]].color = "R"
            else:
                self.graph_contents[list_of_verts[current_idx]].color = "P"
        else:  # otherwise if its none color the first one purple
            self.graph_contents[list_of_verts[current_idx]].color = "P"
        num = 0
        while not queue.is_empty():
            curr_ver = queue.dequeue()
            num += 1
            lists_of_adj = self.graph_contents[curr_ver].adjacent_to
            if self.graph_contents[curr_ver].color == "P":  # if the color is purple
                for ver in lists_of_adj:
                    if self.graph_contents[ver].color is None:  # Only if it is not colored already enqueue and color
                        queue.enqueue(ver)
                        self.graph_contents[ver].color = "R"
                    elif self.graph_contents[ver].color is not None and self.graph_contents[ver].color == self.graph_contents[curr_ver].color:
                        # is not bipartite and exits the function
                        self.reset_vertex(self.get_vertices())
                        return num, False
            elif self.graph_contents[curr_ver].color == "R":  # if the color is red
                for ver in lists_of_adj:
                    if self.graph_contents[ver].color is None:
                        queue.enqueue(ver)
                        self.graph_contents[ver].color = "P"
                    elif self.graph_contents[ver].color is not None and self.graph_contents[ver].color == self.graph_contents[curr_ver].color:
                        # is not bipartite and exits the function
                        self.reset_vertex(self.get_vertices())
                        return num, False

        return num, True  # the num is in order to keep track if we need to find another subgraph meaning we aren't done

    def reset_vertex(self, list_of_verts):
        for ver in list_of_verts:
            self.graph_contents[ver].visited = False
            self.graph_contents[ver].color = None