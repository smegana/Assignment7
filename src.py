import graph


def read_topo_sort_from_file(filename):
    """This reads the first line of the file. In a topological sort solution file,
    the first line holds the nodes in topological sort order on the first line,
    separated by whitespace."""
    with open(filename) as f:
        string = f.readline()
    return string


def parse_tps(tps_str):
    """ Gets a string of ordering of nodes for topological
    ordering and creates a list of integers from that. """
    return [int(x) for x in tps_str.split()]


def contains_sink_node(graph):
    """ Checks if there is a node without outgoing edge. """
    # empty collections are boolean false, so this asks if all
    # nodes have a non-empty set of neighbors (outgoing edges)
    return all(graph[i] for i in graph)


def check_TPS(graph, tps):
    """ Takes a out-edge graph dictionary and a list of integers for
    topological ordering and checks if that topological ordering is correct. """
    for i in reversed(range(len(tps))):
        for j in range(i):
            if tps[j] in graph[tps[i]]:
                print("Fault: There is a backward edge from ", tps[i], " to ", tps[j])
                return False
    if len(graph.keys()) != len(tps):
        return False
    return True


def write_tps_to_file(tps, filename):
    with open('output_' + filename, 'w') as file:
        for node in tps:
            file.write(node + ' ')


def compute_tps(filename):
    """ Write your implementation to create a topological sort here. 
    Store your answer in tps"""
    """ <filename> is the name of the input file containing graph information:
    you need to read it in and perform the topological sort, saving the results
    in tps, then use write_tps_to_file() to output it to a file called output_<filename>"""
    
    """ Read the file into a dictionary representation """
    g = graph.read_graph(filename)
    
    import time
    start_time = time.time()
 
    """ Find in degree for each node in the graph """
    in_deg = {a: 0 for a in g}
    for a in g:
        for b in g[a]:
            in_deg[b] += 1

    """ If a node in the graph has in degree of 0, add it to the queue """
    from collections import deque
    q = deque()
    for c in in_deg:
        if in_deg.get(c) == 0:
            q.appendleft(c)

    """ Add nodes that have 0 in degree to the tps """
    tps = []
    while q:
        node = q.pop()
        tps.append(str(node))
        """ For the nodes connected to the added node, subtract 1 from their in degree """
        for d in g[node]:
            in_deg[d] -= 1
            """ If in degree is now 0, add to the queue for processing """
            if in_deg.get(d) == 0:
                q.appendleft(d)

    end_time = time.time()

    write_tps_to_file(tps, filename)

    print("Ran in: {:.5f} secs".format(end_time - start_time))


if __name__ == '__main__':
    """ Write code here to run compute_tps for your testing purposes"""
    import sys
    filename = sys.argv[1]
    compute_tps(filename)
    f = "output_" + filename
    s = read_topo_sort_from_file(f)
    tps = map(int, s.split())
    g = graph.read_graph(filename)
    """ print(check_TPS(g, tps)) """
