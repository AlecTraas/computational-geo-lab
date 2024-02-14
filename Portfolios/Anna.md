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
<img width="1470" alt="截屏2024-02-14 下午2 00 53" src="https://github.com/AlecTraas/computational-geo-lab/assets/97414774/a70b92a0-c895-44f8-b359-3cb2be27b840">


### Progress 

### Reflection and Planning 




