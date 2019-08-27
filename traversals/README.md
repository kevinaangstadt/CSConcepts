# Traversal Exercises

## Overview

Traversals of graph data structures are a common operation in many algorithms.
The exercises in this directory are meant to help you gain practice with various
traversal (and implementation) strategies.

## Input Format

Graphs will be given to you in [adjacency
list](https://en.wikipedia.org/wiki/Adjacency_list) form.  Note that all edges
in this format are _directed_; undirected edges will appear in the list twice
(once for both directions).

Our chosen format is designed to be simple to parse:

1. The first line of the file is a single integer, which specifies the number of
nodes in the graph.
1. The remaining lines indicate the edges:
  * All integers on a line are seperated by a space
  * The first integer is the ID of the source node of an edge 
  * The remaining integers are all destinations of edges starting from the source
  * A line with a single integer represents a node with no outgoing edges
  * Integers must be in the range 0 <= i <= |nodes|

## Exercises

1. Print out the node IDs using a pre-order depth-first search
1. Print out the node IDs using a post-order depth-first search
1. Print out the node IDs using a breadth-first search

## Bonus Exercises

1. Perform the DFS exercises with and _without_ recursion
1. Perform the BFS exercise without using a queue
1. Implement these exercises in at least one compiled language and one
interpreted language

## Thought experiments

1. Why is there no in-order depth-first search for a graph? 