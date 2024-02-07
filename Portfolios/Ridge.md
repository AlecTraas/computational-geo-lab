# Ridge's Portfolio
## Week 1 (1/31 - 2/7)

This week, our main goal was to theorize and implement an algorithm to solve convex hull problems. Given a set of points, the convex hull is the smallest set of points that encloses all other points in that set. My first intuition was to use ever growing circles from the origin to continously eliminate eges between points in the set until the remaining edges formed the hull. I quickly realized this was not practical because it would be hard to specify a termination case for the algorithm.

My next idea was to repeatedly eliminate points from the set for which there was another point in the set with a more extreme x and y value. Ultimately, you would be left with all the points on the hull. However, I found a few cases where this did not work and it was tough to define what the 'most extreme' was when points are not necessarily centered around the origin

Ultimately, we settled on a gift wrapping algorithm based off minimizing exterior angles from each line segment. We would first start off with a most extreme node, either x or y, because any most extreme node will automatically be included in the hull. From here, we would select the point that forms the smallest exterior angle with the previous line segment. We repeat this process until we get back to the initial node.

We also talked about a quickHull algorithm that chooses subsequent points by distance to a line segment. While this seems like a clever solution, I ultimately felt it would be very confusing and challenging to implement as a beginner project.


