# Carsales Interview Question
## Find the largest assocation group

Author: Nia Chang

Date: 20th May 2021

### Question
Carsales has built an engine to provide recommendations to users regarding vehicles they might be interested in to personalize user experience. Based on historical searches and views by a user, a vehicle type association is defined as - If vehicle type A is viewed by a user, then vehicle type B is also likely to be viewed by the same user. All vehicles onsite that are linked together by a vehicle type association can be considered to be in the same group. A vehicle type without any association to any other vehicle can be considered to be in its own item association group.

Given a list of vehicle type association relationships(i.e. group of vehicles type likely to be viewed together), write a python program that outputs the largest vehicle type association.

#### Input

The input to the function/method consists of an argument - vehicleAssociation, a list containing pairs of string representing the vehicles that are viewed together.

#### Output

Return a list of strings representing the largest association group sorted lexicographically.

#### Example

Input:

itemAssociation: [[Toyota Corolla, Toyota Camry],[Toyota Prius, Toyota Yaris],[Toyota Yaris, Toyota Ascent]]

Output:

[Toyota Ascent,Toyota Prius, Toyota Yaris]


### Answer

#### get_max_association_groups()
The function get_max_association_groups() takes a group of associated items as an input and returns the largest associated item groups:

- The input associated items doesn't have to be pairs (i.e. it can [itemA, itemB, itemC]) (see test case 3)
- If there are multiple largest associated item groups with the same size, all of them will be returned (see test case 4)
- Breadth First Search method is applied. We can consider the association relationships as a undirected graph. 
  Each item is considered as a vertex and the association relations are considered as edges. Therefore, this questions is actually 
  looking for the largest connected component in the graph.
- The output will be returned in lexicographically order. It is achieved with the bubble_sort() function. 
  It can be done with the built-in sorted() function as well.
- There are 5 test cases being provided in the script, if you want to define your own test case, please define it 
  in section # define your own test case
