# Mitansh's Portfolio
## Week 1 (1/31 - 2/7)
1/1/2024

This week, we talked extensively about possible approaches to algorithms to instruct a computer to spit out a convex hull when given an array of points. What was particularly interesting to me was the process we used, with the group brainstorming and coming up with ideas, followed by attempting to poke holes in the algorithm we had come up with and discussing edge cases where we might fail. 

A specifically intriguing idea was to construct a line parallel to the x-axis, passing through the top-most point and rotating it (or finding the least perpendicular distance of the other points to that line). This approach, while workable, was not the most efficient, with a high time-complexity (worst case O(n^2)). Another approach was to split the points into four quadrants, as on a graph, and find the border points in each of those quadrants, thus reducing the number of points required to be compared to the "chosen" points, and less computations required. However, this approach failed for certain edge cases, such as when a quadrant had one point which had no "extremal values", when compared to the other points. 

We also discussed universal edge cases, such as if all the points are collinear. In this case, the parallel line idea would be efficient, with a time complexity of O(n) and the convex hull would look like a line joining all the points. Another edge case was the case of an array of length 3, which would form a triangle in all cases. We decided the most efficient way to deal with this would be include an if statement to check if the length of an array was 3, then check if the points were collinear, and return either a line or a triangle. 

Before meeting next week, I will be looking at possible ways we could actually code the most efficient algorithm we discussed, Quick Hull, or at least write some pseudocode and research packages that could easier allow me to compute the shortest distance between a point and a line. Currently, I'm thinking defining a function that computes the shortest distance between points using vector dot products might be the best way to approach that particular problem. 

## Week 2 (2/8-2/14)
2/12/2024

This week, we explored the different algorithms we had each decided to explore to instruct a computer to spit out a convex hull when given an array of points. I chose a modified-gift wrapping algorithm. In essence, this algorithm starts at the leftmost point of the set, which has to be a part of the convex hull, separates all the other points into two sets, upper and lower, and finds the next hullpoint that is above it. We now find all points above this new hullpoint, and find the next point by finding the least angle between the vertical line passing through the original hullpoint and the vertical line passing through the point p. We repeat the procedure until we hit the topmost point, which must also be in the hullset. 

Then, we switch the procedure, now moving downward from the leftmost point, following the same procedure, until we hit the lowest point, which must also be in the hullset. 

We then switch over to the rightmost point, and go through the same loop, until we hit the bottom and top point again. At that point, our hullset is complete. This algorithm would be more efficient than normal gift-wrapping, since it essentially, on average, eliminates half the points needed to be analyzed every time we find a new hull point, even though it runs through four loops. 

I spent time this week getting familiar with numpy and pandas, since I have rarely used them before, and developing some pseudo and rough code, pictures of which I have attached at the bottom. Before meeting next week, I hope to continue to move toward a fully finished gift-wrapping 2.0 algorithm. 

![Screenshot (46)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/3f2e9c3f-27a6-413b-86fd-314bc986e0f2)
![Screenshot (45)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/b5be7180-f8d6-4536-be73-71cdacb718a8)
![Screenshot (44)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/5a974d33-3889-4223-8ba9-a1d6614235b3)

## Week 3 (2/15-2/22)
This week, the main focuse was on completing my GiftWrapping algorithm for a convex hull. I did have to take some inspiration from other GitHubs in order to get the syntax and flow order right, but the main idea was to right an algorithm from the GiftWrapping approach that can read a set of points and spit out a convex hull. The idea of a part of the algorithm was to also be interactive, prompting the user for the number of points n desired and generating a convex hull from n randomly generared points. Pictures of the code and the final output generated are below. I have included pictures of the convex hull for both n=200 and n=300.

I also read through some parts of the textbook chapter on Voronoi Diagrams. Given my interest in the applications of mathematics, I'm extremely intrigued as to the use of Voronoi diagrams in production processes, delivery optimization mechanisms, and I wonder if Voronoi diagrams could be used to analyze tactics and spaces in sports such as football or soccer. An idea I had related to that is for scouting potential players: using voronoi diagrams to map out the space a player is responsible for on the field, using voronoi diagrams to analyze a player's positioning and the spaces they most occupy/take responsibility for, and hence being able to find the best match. Some more research will be required, but I'm extremely interested in seeing where this could lead.

![Screenshot (50)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/ae7fde89-d5ca-4d33-9be1-faf81d5be025)
![Screenshot (51)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/32c4ab26-1e0b-4fc9-b6ea-86e47e50f5bb)
![Screenshot (52)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/fca18835-bfad-4e6b-8c0d-eab374937b95)
![Screenshot (53)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/6e931fee-b5d3-4133-8935-4583eb9fb97d)
![Screenshot (54)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/99d6a62c-8650-4bf6-99f2-44253c0e497e)
![Screenshot (55)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/3dcfaaff-57fa-4aa9-afda-c59951bc9249)

## Week 4 & Spring Break (2/23-3/13)
This week, the main focus was on completing my slides and preparing for the upcoming presentation to the rest of the Geometry Lab group. We decided on the split of slides (who is presenting what). I presented on the introduction and applications of Convex Hulls, and then about the GiftWrapping Algorithm, and in which scenarios it is more efficient to use the "four quadrant" variation of the GiftWrapping approach. 
Over Spring Break, I worked my way through sections of the textbook on Voronoi Diagrams and watched a few YouTube tutorials to fully understand the algorithm used to produce it. In essence, this Fortune's Algorithm involves a downward flowing horizontal line, and a beach line recording the Voronoi Diagram, and utilizes a binary search tree and priority queue. Every time the line comes across an event, there are two options: that it comes across a new site that must be added to the Diagram, or two neighboring cells are completely surrounded by a third cell, and must then be adjusted to reflect the correct Voronoi. As the horizontal line flows down it comes across all sites and the beach line reflects the shape of a parabola with the focus at the site and the directrix being the horizontal line. 
I also spent some time thinking about the Least Cost Path problem, considering cases where you can "jump" from one path to another and when you cannot. One of my ideas is to set a benchmark, or some upper limit so that the path may not be the most efficient, but it is "efficient enough" and if so, then for the second case we can use a moving average of the upper limit that increases as we pass through each node. Another idea I had with regards was to model each sequential node as a normal distribution with N follows (n*u/N, (u/N)^2) where n is the nth node, u is the upper limit, and N is the total number of nodes. We eliminate paths that exceed 1.5 standard deviations, thus ending with a suitable path without having to check and follow the sum of each and every node. This method does assume that no such node exists that completely overpowers the other nodes. 

## Week 5 (3/13-3/20)
This week, I worked on preparing myself to write code for Fortune's Algorithm. I spent some time getting a high level overview of binary search trees and priority queues. A binary search tree is a structure where we sort an array such that there exists one "parent" node which has a left and a right branch and that satisfies the following two conditions: 
1) the "daughter" nodes also each have two "daughter" nodes of their own
2) the left node is always less than the parent node, and the right node is always greater than the parent node.
As so:
![Screenshot (59)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/37c26943-dcd2-4ef4-9814-62297a6ee504)
The binary search tree helps in adding sites that the sweep line encounters and maintaining and updating the voronoi arcs correctly, including the insertion and "expansion" of arcs, as well as the removal of arcs when a circle event occurs.
I also explored Dijkstra's Algorithm to compute the shortest path connecting all sites. It basically iterates through all the possible paths before choosing the path of least cost from the source to the destination, and then does the same again from the new source, the original destination. It also picks destinations via the same method of evaluating all possible nodes and identifying the least cost path.

## Week 6 (3/21-3/27)
This week, I spent some time learning about NetworkX, the most popular python library for graphs. NetworkX will be quite useful when attempting my application of Voronoi Diagrams to soccer formations, since the initial positions of players can be represented in terms of graphs. After playing a little bit with the basic syntax and code structure, I generated an image for a basic 1-4-3-3 formation in soccer, one of the most popular formations in use today. 

![image](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/2c3e36b5-1dc3-437a-a153-0a6dc8f10883)


I then worked on a mini-manual Voronoi Diagram for the same, currently taking into account only the nodes 1,2,3,4,5. In soccer, this is the defensive line and the goalkeeper, and, arguably where positioning and hence Voronoi Diagrams to come up with strategies are most useful. In the future, the goal is to construct a Voronoi Diagram for the full 11 players (either through my in-progress algorithm if possible, or through manual implementation of the sweep line method). This was the product (where the edges represent the boundaries of the Voronoi Diagram for these 5 nodes only):

![Screenshot (62)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/4d239f24-4e52-43c1-9cfe-5c2494ac7727)

I also spent some time thinking about my presentation at the Math Club/AWM meeting. In soccer, "heat maps" are visuals that represent the average position of a player, with the darker colors representing higher density. 

![image](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/0cb11eb6-c66b-4ed0-89f6-4f8c6bac234f)

This is the heatmap for Virgil Van Dijk, from his debut for Liverpool. As can be seen, his heatmap from that game, if overlayed on the Voronoi Diagram above almost perfectly overlaps for the defensive aspects. At the time, Liverpool used a 1-4-3-3 system, so we can see why Virgil Van Dijk was a great addition, since his positioning almost perfectly captures what was required of him positionally in that system according to the Voronoi Diagram generated

## Week 7 (3/28-4/3)

This week, I spent some time familiarizing myself with priority queues and heapq, a library that creates a heap and is primarily used to create priority queues. A priority queue is a type of binary search tree where the parent node is less than each of its children nodes. Hence, the source (super-parent) node is the least, and the tree goes from there. 

![Screenshot (65)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/ee03a0fe-42f1-455f-b7e9-9c8f43c98d23)

I also spent some time beginning to code my Voronoi Diagram:

![Screenshot (66)](https://github.com/AlecTraas/computational-geo-lab/assets/158364293/4cb4975c-e460-4caa-ba71-c2025e93b38e)

The parabola function returns the y-coordinate of a parabola given its focus, directrix, x-coordinate and width as parameters, and the intersection function determines the intersection of these parabolas with focus points p1,p2 and the directrix (the sweep line)




