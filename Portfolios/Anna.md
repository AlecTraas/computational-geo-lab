# Anna's Portfolio
## Week 1 (1/31 - 2/7)
On 1.31 meeting, we discussed about the convexhull problem. The mentors introduced the problem of finding the smallest convex set by the points given(or random points). With the help of mentors, we brainstormed the first method, the gift wrapping algorithm. In general, it means 
More detailed explaination can be found on the website here:https://en.wikipedia.org/wiki/Graham_scan
Briefly speaking, the method can be concluded:
1. Find the point with the lowest y-coordinate. If there's a tie, pick the one with the lowest x-coordinate. Call this point P. This is a quick step, taking O(n) time for n points.
2. Sort the remaining points by the angle they make with P, without actually calculating the angle. Use a simple sorting method (like heapsort, O(n log n)) and a function related to the angle. If two points have the same angle, keep the one that's farther from P.
3. Go through the sorted points one by one, checking if you're making a left or right turn from the last point. If it's a right turn, the point before isn't on the hull. Keep checking and removing points that lead to right turns. Use basic math to check turns without needing angles.
4. Continue until you loop back to P. Now, you have the points that make up the hull in counterclockwise order. This step sorts out which points are on the outer edge (convex hull) and leaves out the ones inside.





The problem I faced now:


https://github.com/zifanw/ConvexHull2D/blob/master/ConvexHull.py
