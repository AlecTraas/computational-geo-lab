# Ridge's Portfolio
## Week 1 (1/31 - 2/7)

This week, our main goal was to theorize and implement an algorithm to solve convex hull problems. Given a set of points, the convex hull is the smallest set of points that encloses all other points in that set. My first intuition was to use ever growing circles from the origin to continously eliminate eges between points in the set until the remaining edges formed the hull. I quickly realized this was not practical because it would be hard to specify a termination case for the algorithm.

My next idea was to repeatedly eliminate points from the set for which there was another point in the set with a more extreme x and y value. Ultimately, you would be left with all the points on the hull. However, I found a few cases where this did not work and it was tough to define what the 'most extreme' was when points are not necessarily centered around the origin

Ultimately, we settled on a gift wrapping algorithm based off minimizing exterior angles from each line segment. We would first start off with a most extreme node, either x or y, because any most extreme node will automatically be included in the hull. From here, we would select the point that forms the smallest exterior angle with the previous line segment. We repeat this process until we get back to the initial node.

We also talked about a quickHull algorithm that chooses subsequent points by distance to a line segment. While this seems like a clever solution, I ultimately felt it would be very confusing and challenging to implement as a beginner project.

## Week 2

This week our primary goal was to finish a basic implementation of our algorithm. My first attempt involved taking the angle between the last point in the hull and some checked point in the set of points and comparing it to the last angle calculated in this process. I would iterate over the points to check and add the one with the least change in angle to the hull. I first found the leftmost point in set and used an initial angle of pi/2. This was first implemented recursively where the base case was choosing the root point as the point with the minimized angle. However, I ultimately realized that recursion was not necessary and increased overhead. 

I started to run into issues with this implementation because it would struggle to change direction. I think this was due to my use of arctan in finding angles. For example, my last two points may have a dx of -1 and a dy of -1. The next selecting point may have a dx of 1 and a dy of 0.9. Tangent treats these two vectors as having extremely similar angles, despite being opposite in direction. As a result, the algorithm had a hard time changing directions. I ultimately decided to change my implementation rather than try to solve this issue as I thought it could become complicated extremely quickly.

My next implementation used the dot product formula to calculate the angle between two vectors connecting points in the hull. I used the last vector in the hull and scanned all the possible new vectors to find the one that formed the maximum interior angle. Although this added a lot of extra computation, it was significantly more readable and easy to implement. I did run into an issue for choosing the third point in the hull where it would always choose the initial point because it calculated the angle between the vectors as pi. I fixed this by adding a conditional to my angle calculation method that returned 0 not pi whenever the two points were equal.

Ultimately, this method worked. I also decided I wanted to create an animation to visually represent the process. With online resources, I was able to come up with an elementary matplotlib animation that shows each subsequent point being selected. I would like to update this to show the algorithm scanning over points and choosing the one with maximum angle.

## Week 3

This week, I mainly focused on preparation for the upcoming team presentation next Tuesday. I did some research on easy way to explain convex hulls and algorithms that would be useful for conveying our projects. One analogy I found was a rubber band analogy. Think of your points as a set of pegs. Now, think of your hull as a rubber band being stretched around the pegs. As you let the rubber band go, it will snap around the pegs and form the convex hull. This is useful to give a common visual explanation for what a convex hull is and a real-world place you might see it.

Beyond this, we started on a slide deck. I wrote slides briefly explaining what a convex hull is by different definitions, and created graphics to show each step of the rubber band analogy. I also created slides explaining the basic pseudo-code of a gift wrapping algorithm and why it works. I included a Wikipedia gif of the algorithm executing as well as attached the animation that I made in matplotlib.

## Week 4

This week we finished up and practiced slides for our math club presentation on Tuesday, 2/27. I presented a brief overview of the gift wrapping algorithm along by taking a sample spread of points and walking through each step of the algorithm. I created visuals to show each subsequent step being processed.