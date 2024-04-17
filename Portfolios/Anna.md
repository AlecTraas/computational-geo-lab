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
With Lam's assistance, I learned how to use the random function and completed my work on the convex hull. Here is the final graph.

![5681708531544_ pic](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/fbf2d042-e329-46b0-9490-62c7a901ce69)

The mentors introduced the concepts of Delaunay triangulations and Voronoi diagrams, and we decided that these would be our focus for the next period. Next Tuesday, we will have a group presentation in front of another geometry group, during which we will discuss our work. Essentially, we'll still focus on the 2D convex hull and the different algorithms we used in the presentation, including the animation.

### Progress 

I have read several materials to get a clue on how to start with Delaunay triangulation. A helpful resource I found is https://www.cs.princeton.edu/courses/archive/spring12/cos423/bib/vor.pdf. I have read through the different algorithms introduced here, and during spring week, I could possibly start working on the sweeping line algorithm. Also, Delaunay triangulation can finally produce a great graph like this:

![5691708533565_ pic](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/ed383de8-8647-4982-9ff9-0ec06a72f32e)

I believe this graph will be beneficial for future presentations and provide a basic understanding of computational geometry.

## Week 4 (2/21 - 2/28)
This week, we mainly focused on our presentation to the other geometry labs. I was tasked with presenting on the 2D quickhull algorithm.
I created some visualized pictures on google drawing to help understanding:
![graph1](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/e1f3dedf-dcc7-42df-9ee8-67275aea49b4)
![graph2](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/3bbb9a26-fa1f-4f2e-bcff-2bc177d20f72)
![graph3](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/888b94db-d4ba-4a04-b666-f97cc9f5dd5b)
![graph4](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/e7bb97f6-d418-4f6c-bafa-fc49c6cc5fbf)
![graph5](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/5dc8cf80-7db6-4099-b25c-f8964467a8f9)


## Week 5 (2/28 - 3/13)
During spring break, I was reading through materials about the line segment intersection problems. I have learned through the Plane Sweep Algorithm and learned the basic theory of the basic theory about the run time.
Balanced Binary Search Tree is included in this algorithm but I did not know much about it. Next week, I will focus more on the details of the algorithm, learn the balanced binary search tree, and see how i could visualize this.

<img width="681" alt="截屏2024-03-13 下午4 43 47" src="https://github.com/AlecTraas/computational-geo-lab/assets/97414774/73ce7dda-8706-4883-b988-094698a059a6">

## Week 6 (3/13 - 3/20)
This week, I was focusing on developing the foundational code for detecting line segment intersections, a crucial aspect of computational geometry. My approach was grounded in a comprehensive review of scholarly materials that laid the theoretical groundwork for this problem. I delved into various documents, including:
https://cs.gmu.edu/~jmlien/teaching/09_fall_cs633/uploads/Main/lecture02.pdf
https://ics.uci.edu/~goodrich/teach/geom/notes/LineSweep.pdf
https://www.cs.cmu.edu/~15451-f22/lectures/lec21-geometry.pdf

These resources provided a solid understanding of the algorithm's logic, which I aimed to translate into my coding efforts.

Segment Intersection Visualization - This illustration depicts the step-by-step process of my current implementation, highlighting how line segments are processed and intersections are identified or rejected.

The algorithm proceeds by processing the segments in a sequential manner, utilizing a binary tree structure to maintain and query the active line segments efficiently. Here's a brief overview of the process:

Upon processing the left endpoint of a segment, the algorithm checks for intersections with currently active segments, inserting the new segment into the tree.
Right endpoints trigger the deletion of their respective segments from the tree, with a final check for intersections amongst the remaining segments.
Through this iterative process, the algorithm successfully identifies intersections, such as those between segments 2 and 3.

Additionally, I explored practical implementations, such as a C++ code example on GeeksforGeeks, which offered valuable insights into translating theoretical concepts into executable code.

![SegmentIntersect-1](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/9bce4403-1bf9-402b-be03-06b4428a37f9)

Currently, my implementation can determine the existence of line segments but falls short in accurately identifying and exporting intersections. The next phase of development will focus on refining this capability, with an emphasis on outputting identified intersections efficiently.

## Week 7 (3/20 - 3/27)
This week, we focus on the second presentation to the AWM and the Math Club. We use the situation similar to poster session in this time.  I introduced the Sweep Line algorithm, emphasizing its significance in solving real-world problems through the detection of line intersections. This session not only illuminated the practical applications of theoretical concepts but also marked the beginning of the next phase of my research.

![image](https://github.com/AlecTraas/computational-geo-lab/assets/97414774/3f470c82-3d50-46fb-9c06-0f3d8620cdf4)

I recently discovered a video that introduces the real-life applications of the line segment intersection problem. One compelling example detailed in the video is how this problem can be utilized to determine the intersections between a river and a planned road. By identifying these intersection points, we can strategically determine the optimal locations for bridge construction, thereby efficiently planning the number and placement of bridges needed to facilitate transportation without disrupting natural waterways.

Furthermore, for the code part, I've identified the necessity for refinement to ensure its applicability in more generalized scenarios. The focus ahead is on enhancing the algorithm's ability to precisely determine intersection points across a broader range of cases. This step is critical for moving from theoretical exploration to practical application, setting the stage for future developments aimed at refining the algorithm's accuracy and utility.

## Week 8 (3/27 - 4/3)

During this week's group meeting, I addressed a critical issue where my code was previously only identifying a single intersection point. I've now refined the algorithm, enabling it to accurately detect and output all intersections of the given segment.

Furthermore, to enhance the visualization aspect, I've implemented a strategy for labeling each line segment with a unique number, facilitating easier verification of the code's accuracy. Following Lam's advice, I experimented with the matplotlib.pyplot.text function. After several iterations and adjustments, I successfully integrated a mechanism to automatically label every line in the generated graph. 


<img width="622" alt="截屏2024-03-30 下午11 17 33" src="https://github.com/AlecTraas/computational-geo-lab/assets/97414774/ab4ea8f0-3d98-4299-8033-1585fca73723">

In the next phase of the project, I plan to focus on precisely determining the position of each intersection point. It will significantly enhance the accuracy and utility of the project. Additionally, I aim to explore potential applications of line intersection analysis, such as map overlay.

## Week 9 (4/3 - 4/10)

During last week's group meeting, Lam gave me advice on the command code for solving linear equations. Inspired by this, I focused on adjusting the code to output the position of the intersection points as the final product. This week, I worked on adjusting some definitions within the code and revisited the numpy command book to find appropriate commands to apply. Furthermore, I made slight adjustments to the graph output code in order to enhance clarity and readability. 

<img width="929" alt="截屏2024-04-10 下午4 28 27" src="https://github.com/AlecTraas/computational-geo-lab/assets/97414774/99b97f93-607f-4e6e-9888-b1f7319fdf12">


<img width="859" alt="截屏2024-04-10 下午4 27 49" src="https://github.com/AlecTraas/computational-geo-lab/assets/97414774/9b130607-9489-4cad-bae8-2cd2caa37415">


## Week 10 (4/10 - 4/17)

Throughout this week, I focused on adjusting various definitions within the code and revisited the numpy command documentation to identify and apply appropriate commands. Furthermore, I made minor enhancements to the graph output code segment to randomize the segment positio. The culmination of these efforts has resulted in asolution capable of accurately determining and displaying the intersection points, complemented by a polished graphical output that prioritizes clarity and interpretability.

<img width="834" alt="截屏2024-04-17 下午4 27 34" src="https://github.com/AlecTraas/computational-geo-lab/assets/97414774/7cfb886d-d5c5-451f-a8f5-5cf114fbdd59">

