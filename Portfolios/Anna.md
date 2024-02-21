# Anna's Portfolio
## Week 1 (1/31 - 2/7)
### Meeting Recap
On January 31, we explored the convex hull problem, aiming to find the smallest convex polygon enclosing a set of points, guided by mentors who introduced us to the gift wrapping algorithm as our initial solution approach. This algorithm iteratively selects the most counterclockwise points to construct the hull, detailed further on Wikipedia's Graham Scan Algorithm page.
Briefly speaking, the gift wrapping method can be concluded as:
1. **Find the point with the lowest y-coordinate.**:  If there's a tie, pick the one with the lowest x-coordinate. Call this point P. This is a quick step, taking O(n) time for n points.
2. **Sort the remaining points by the angle they make with P**: Use a simple sorting method (like heapsort, O(n log n)) and a function related to the angle. If two points have the same angle, keep the one that's farther from P.
3. **Go through the sorted points**: Go through the sorted points one by one, checking if can make a left or right turn from the last point. If it's a right turn, the point before isn't on the hull. Keep checking and removing points that lead to right turns. Use basic math to check turns without needing angles.
4. **Continue until loop back to P**:  Now, with the points that make up the hull in counterclockwise order, this step sorts out which points are on the outer edge (convex hull) and leaves out the ones inside.

Additionally, our mentors introduced the QuickHull algorithm, a method that calculates the convex hull of a point set by recursively finding and removing points within the boundaries created by extreme points. It begins with the points of minimum and maximum x-coordinates, segments the set, identifies the farthest point from each segment to establish new boundaries, and continues this process to discard points not on the hull. This divide-and-conquer strategy effectively isolates the outermost points that define the convex polygon enclosing the entire set.


### Progress 
Over past week, I had a thorough review of the literature pertaining to the two algorithms previously discussed, ultimately electing to concentrate my efforts on the QuickHull algorithm.

The methodology employed in my implementation of the QuickHull algorithm can be summarized as follows:

1. **Initialization**: Start with an empty set for the convex hull.
2. **Identifying Extremal Points**: Find and add the leftmost and rightmost points (A and B) to the convex hull.
3. **Partitioning the Point Set**: Divide the remaining points into two subsets based on their location relative to the line AB.
4. **Recursive Hull Construction**: Use the `FindHull` function to recursively find and add the farthest point from each subset to the convex hull, effectively identifying all points that form the outer boundary.

### Problems
1. In my initial attempt using the notebook test_anna01.ipynb, only the plots of selected points were visible, while those that were eliminated didn't appear on the graph.
2. The points it identified seem correct to me. However, the way the lines were drawn appeared weird.
3. I attempted to execute the code from the following URL: https://github.com/zifanw/ConvexHull2D/blob/master/ConvexHull.py, aiming to replicate the code and verify its functionality. I have documented the code in notebook test_anna02.ipynb. Unfortunately, there are some errors from execution.
   

## Week 2 (2/7 - 2/14)
### Meeting Recap
In Wednesday's meeting, I have the graph look like this during the meeting.
![image1](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/810c3465-e5f9-4c79-87e5-4479f919504e)
During the discussion, we explored ways to enhance the functionality of the graph. Two main ideas were suggested. The first suggestion involved adding additional code after the original algorithm to sort the convex hull points. This would involve connecting the leftmost and rightmost points and using this line to divide the set of points. Points on the upper side would be connected from left to right, and those on the lower side from right to left. The alternative method proposed embedding the sorting process directly into the original code. Given that sorting and dividing are integral to the QuickHull method, integrating graphing functionalities at this stage seemed feasible.

### Progress 
From the start, I tried to code the connections for the upper and lower sides. In the process, I digged deeper into the syntax and functionalities of Matplotlib and learned more about slicing techniques. However, the outcomes were not as satisfactory as I had hoped.
![image2](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/48d08a1f-9621-4122-9c3f-05d08cd2c9e2)

I realized I wanted the convex hull to be depicted in a single color, along with the inclusion of the original input points on the graph. After further learning of Matplotlib, I had the following graph:
![image3](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/0c07d2f0-e10c-484b-a3e5-09f7cd063a8c)

This graph contains all the points I had put, and generates the smallest convex set in two dimensions.

### Reflection and Planning 

Incorporating random points as input could enhance the testing of the algorithm's characteristics. However, my familiarity with the use of random functions and their generation is limited. Thus, I decided to maintain the current code and graphical output for the time being.

In the upcoming week, I will explore whether it's feasible to incorporate randomness into the dataset to create a more diverse set of input points. Alternatively, I may discuss with my group the possibility of shifting our focus from a two-dimensional to a three-dimensional approach.



## Week 3 (2/14 - 2/21)
### Meeting Recap
With Lam's help, I learned how to use the random function and wrapped up my work in convexhull.
Here is the final graph.

### Progress 
From the start, I tried to code the connections for the upper and lower sides. In the process, I digged deeper into the syntax and functionalities of Matplotlib and learned more about slicing techniques. However, the outcomes were not as satisfactory as I had hoped.
![image2](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/48d08a1f-9621-4122-9c3f-05d08cd2c9e2)

I realized I wanted the convex hull to be depicted in a single color, along with the inclusion of the original input points on the graph. After further learning of Matplotlib, I had the following graph:
![image3](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/0c07d2f0-e10c-484b-a3e5-09f7cd063a8c)

This graph contains all the points I had put, and generates the smallest convex set in two dimensions.

### Reflection and Planning 

Incorporating random points as input could enhance the testing of the algorithm's characteristics. However, my familiarity with the use of random functions and their generation is limited. Thus, I decided to maintain the current code and graphical output for the time being.

In the upcoming week, I will explore whether it's feasible to incorporate randomness into the dataset to create a more diverse set of input points. Alternatively, I may discuss with my group the possibility of shifting our focus from a two-dimensional to a three-dimensional approach.







