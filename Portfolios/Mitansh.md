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

