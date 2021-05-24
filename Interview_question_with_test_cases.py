# -*- coding: utf-8 -*-
"""
Author: Nia Chang 
Date: 20 May 2021 

Comments:
The function get_max_association_groups() takes a group of associated items as an input and returns the largest associated item groups:

- The input associated items doesn't have to be pairs (i.e. it can [itemA, itemB, itemC]) (see test case 3 below)
- If there are multiple largest associated item groups with the same size, all of them will be returned (see test case 4 below)
- Breadth_First_Search method is applied. We can consider the association relationships as a undirected graph. 
  Each item is considered as a vertex and the association relations are considered as edges. Therefore, this questions is actually 
  looking for the largest connected component in the graph.
- The output will be in lexicographically order. It is achieved with the bubble_sort() function. 
  It can be done with the built-in sorted() function as well.
- There 5 test cases being provided in this script, if you want to define your own test case, please define it 
  in section # define your own test case
"""

import itertools


def BFS_Graph(graph_dict,start, visited):
    cc = []
    queue = [] 
    queue.append(start)

    while (len(queue)> 0):
        v = queue.pop(0)
        adj_v = graph_dict[v]
        
        for w in adj_v:
            if w not in visited:
                queue.append(w)
                visited.add(w)
        cc.append(v)
    return visited, cc


# Bubble sort could be replaced with the built in function sorted()
def bubble_sort (items,order):
    if order not in ('a', 'd'):
        print('Please select a valid order and re-try')
        return None

    else:
        sorted_list = []
        
        while items != []:
            # start with assume the first element is the min one
            min_i = items[0]

            for i in range(1,len(items)):
                curr_i = items[i]  
                if curr_i < min_i:
                    min_i = curr_i
                    
            # get the item and remove from the list     
            index = items.index(min_i)
            sorted_item = items.pop(index)
            sorted_list.append(sorted_item)
        if order == 'a':
            #print(sorted_list)
            return sorted_list
        
        else:
            #reverse the list if descent
            rev_list = sorted_list[::-1]
            #print(rev_list)
            return rev_list
     
    
def get_max_association_groups(item_groups):
    
    # Step 1: Create graph 
    # Consider each item as a node in the graph and the association connection as an edge that connect the nodes
    # Can handle the associated groups that is not a pair as well

    # Initialization: create nodes
    all_items = list(set([item for group in item_groups for item in group]))
    item_dict = {item:[] for item in all_items}
    all_components = []

    # Add edges
    for group in item_groups:
        combos = list(itertools.combinations(group, 2))
        for combo in combos:
            n = combo[0]
            m = combo[1]
            if m not in item_dict[n]:
                item_dict[n].append(m)
            if n not in item_dict[m]:
                item_dict[m].append(n)

    # Step 2: Looking for connected component
    # start with random item
    # each vertex is unique
    visited = set()
    while len(all_items) > 0:

        start = all_items.pop(0)
        visited.add(start)
        visited, connected_component = BFS_Graph(item_dict, start, visited)
        # Bubble sort could be replaced with the built in function sorted()
        all_components.append(bubble_sort(connected_component,'a'))
        for item in visited:
            if item in all_items:
                all_items.remove(item)
                
    # Step 3: return max group  
    max_size = max(len(component) for component in all_components)
    results = [component for component in all_components if len(component) == max_size]
    for cc in results:
        print(cc)
    return(results)

if __name__ == '__main__':
    # test case 1
    item_groups = [
               #['Mazda 3', 'Toyota Yaris'],
               ['Toyota Corolla', 'Toyota Camry'], 
               #['Mazda Cx9', 'Toyota Klugar'], 
               ['Toyota Prius', 'Toyota Yaris'],
               #['Mazda Cx3', 'Mazda Cx5'],
               ['Toyota Ascent', 'Toyota Yaris']
               #['Toyota Asce','Toyota Yaris'],
               #['Mazda Cx3', 'Mazda 3']
              ]
    print('Test case 1')
    print('Input:', item_groups)
    print('Output:')
    max_associate_groups = get_max_association_groups(item_groups)
    
    # test case 2
    item_groups = [
                   ['Mazda 3', 'Toyota Yaris'],
                   ['Toyota Corolla', 'Toyota Camry'], 
                   ['Mazda Cx9', 'Toyota Klugar'], 
                   ['Toyota Prius', 'Toyota Yaris'],
                   ['Mazda Cx3', 'Mazda Cx5'],
                   ['Toyota Ascent', 'Toyota Yaris'],
                   ['Toyota Asce','Toyota Yaris'],
                   ['Mazda Cx3', 'Mazda 3']
                  ]
    print('Test case 2')
    print('Input:', item_groups)
    print('Output:')
    max_associate_groups = get_max_association_groups(item_groups)
    
    # test case 3
    item_groups = [
                   ['Toyota Corolla', 'Toyota Camry'], 
                   ['Mazda Cx9', 'Toyota Klugar'], 
                   ['Toyota Prius', 'Toyota Yaris'],
                   ['Mazda Cx3', 'Mazda Cx5','Mazda 3'],
                   ['Toyota Ascent', 'Toyota Yaris','Toyota Corolla']]
    print('Test case 3')
    print('Input:', item_groups)
    print('Output:')
    max_associate_groups = get_max_association_groups(item_groups)
    
    # test case 4
    item_groups = [
                   ['Toyota Corolla', 'Toyota Camry'], 
                   ['Mazda Cx9', 'Toyota Klugar'], 
                   ['Toyota Prius', 'Toyota Yaris'],
                   ['Mazda Cx3', 'Mazda Cx5'],
                   ['Toyota Ascent', 'Toyota Yaris'],
                   ['Mazda Cx3', 'Mazda 3']
                  ]
    print('Test case 4')
    print('Input:', item_groups)
    print('Output:')
    max_associate_groups = get_max_association_groups(item_groups)
    
    # test case 5
    item_groups = [
                   ['Toyota Corolla', 'Toyota Camry'], 
                   ['Mazda Cx9', 'Toyota Klugar'], 
                   ['Toyota Prius', 'Toyota Yaris'],
                   ['Mazda Cx3', 'Mazda Cx5','Mazda 3'],
                   ['Toyota Ascent', 'Toyota Yaris','Toyota Corolla'],
                   ['Toyota Prius', 'Nissan Juke']
                  ]
    print('Test case 5')
    print('Input:', item_groups)
    print('Output:')
    max_associate_groups = get_max_association_groups(item_groups)

    # define your own test case:
    '''
    my_test_case = []
    print('My own test case:')
    print('Input:', my_test_case)
    print('Output')
    max_associate_groups = get_max_association_groups(my_test_case)
    '''
