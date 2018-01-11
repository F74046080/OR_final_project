# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:50:53 2018

@author: Chau
"""

import csv
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

# Callback of distance
class CreateDistanceCallback(object):
  # Calculate distances between points.
  def __init__(self):
    # Array of the distances of point to all the other point
    # Open the .csv
    dis_list = []
    with open('distance_all.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            dis_list.append(row)
    for i in dis_list:
        i.pop() # pop the last empty element
    self.matrix = dis_list
    '''self.matrix = [
    [    0, 3894, 1816, 2515, 2910],
    [ 3748,    0, 2585, 1780, 2446],
    [ 1984, 2556,    0,  776, 1154],
    [ 2628, 1780,  804,    0,  808],
    [ 3256, 2223, 1161,  814,    0]]
    '''
  def Distance(self, from_node, to_node):
    return int(self.matrix[from_node][to_node])
def main():
  
  # use numbers to replace the name of post
  # the 0 means the start & end point
  post_names = []
  for i in range(0, 41):
      post_names.append(str(i))
  # post_names = ["a","b","c","d","e"]		# the test data
  tsp_size = len(post_names)
  num_routes = 1    
  depot = 0        # The starting point

  # Create the path model
  if tsp_size > 0:
    routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
    # Do the callback and return the distance between the points
    dist_between_nodes = CreateDistanceCallback()
    dist_callback = dist_between_nodes.Distance
    routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:
      # the total distance about the solution
      print ("Total distance: " + str(assignment.ObjectiveValue()) + " m\n")
      route_number = 0
      index = routing.Start(route_number)
      route = ''
      while not routing.IsEnd(index):
        route += str(post_names[routing.IndexToNode(index)]) + ' -> '
        index = assignment.Value(routing.NextVar(index))
      route += str(post_names[routing.IndexToNode(index)])
      print ("Route:\n\n" + route)
    else:
      print ('No solution found.')
  else:
    print ('Specify an instance greater than 0.')

if __name__ == '__main__':
  main()
