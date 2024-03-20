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

![image 1](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/Screenshot%202024-02-28%20162324.png)
![image 2](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/Screenshot%202024-02-28%20162346.png)
![image 3](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/Screenshot%202024-02-28%20162405.png)
![image 4](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/Screenshot%202024-02-28%20162425.png)
![image 5](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/Screenshot%202024-02-28%20162440.png)
![image 6](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/Screenshot%202024-02-28%20162502.png)
![image 7](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/Screenshot%202024-02-28%20162518.png)
![image 8](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/Screenshot%202024-02-28%20162535.png)
![image 9](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/Screenshot%202024-02-28%20162553.png)
![image 10](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/Screenshot%202024-02-28%20162608.png)
![image 11](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/Screenshot%202024-02-28%20162622.png)
![image 12](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/Screenshot%202024-02-28%20162641.png)
![gif 1](https://drive.google.com/file/d/1mmrHI-DirlTQ_BmRftYvNL2fqQNk91zP/view?usp=sharing)

## Week 5

This week, since we had mostly completed our convex hull algorithms, we were tasked with selecting topics for a final project from our textbook Computational Geometry: Algorithms and Applications (accessible here: https://cimec.org.ar/foswiki/pub/Main/Cimec/GeometriaComputacional/DeBerg_-_Computational_Geometry_-_Algorithms_and_Applications_2e.pdf). 

The main topic that stood out to me was Orthogonal Range Searching in Chapter 5. I took an interest in it mainly because it seemed deceptively simple and was also related to topics I had experiences in like database querying and search trees.

The basis of the problem is incredibly easy to understand. At it's simplest level, you are given a set of points and want to find all points that have values in some range. 

A simple solution to this problem would be to simply iterate over every single point and check whether its value satisfies the requirement. This has Theta(n) time complexity and uses no additional space. While this does work, we can do better.

Another approach we can use is range searching and is reminiscent of using a binary search to efficiently search a data set. We create a binary search tree to represent the data where our leaf nodes are our data points. Our intermediary nodes are data points that we use to traverse and find valid points. If our data is sorted, we can do this in linear time based on the recursively splitting the list in two across the median. Note that the medians are still included as leaves so either the right or left sublist must continuously contain the median.

![1D tree](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week5/1dtree.png)

If we are given a parameter [x, x'] to search for values over, the 1D example works as follows. Traverse the tree and find the node where the paths to x and x' diverge. We can do this by traversing the tree while x and x' will travel the same direction and returning the first node where they do not or the leaf node if they converge.

![splitnode](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week5/splitnode.png)

If they converge to a leaf, we only have to check if this leaf is included. Otherwise, we first follow the path to x starting from the split node. Anytime the path traverses the left child in the tree, we add all the leaves that stem from the right child to our answers. This is based on the idea that the leaves to the right of the path from the split node to x will be between the paths of x and x'. A vizualiation of this can be seen below. Ultimately, the path will terminate at a leaf which we manually have to check.

![1d query](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week5/1dqueryvisual.png)

Likewise, we follow the path to x' from the split node. Anytime the path traverses the right child, we add all the leaves that stem from the left child. Check the leaf node we end at.

![diagram showing query works](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week5/1dalgo.png)

The time complexity of this algorithm is O(logn + k) where n is the number of points and k is the number of points that satisfy our interval. The worst case time is still the same as the simple method as you will always take O(n) time if you must return all points. However, the average case is significantly better as all points will usually not be returned.

If instead of one variable we had multiple, we can get around the added complexity by performing an additional range search on the next variable anytime we would have added those point(s) to our answer in the 1D example. 

![diagram showing 2d query works](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week5/2dqueryvisual.png)

The underlying structure of the range tree must be slightly altered so that each node is linked to a range tree of points the stemming from this node ordered on the next variable. The runtime of this algorithm is O((logn)^z + k) where n is the number of points, k is the number of points reported, and z is the number of dimensions.

![diagram showing 2d structure works](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week5/2dbuild.png)

My next step in implementing this algorithm will be first to interpret a 1D and 2D range tree creation and searching algorithm. The book provides pseudocode for these algorithms but they are not scaled to work for an n dimensional query. 

![diagram showing 2d build algo](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week5/2dtree.png)

![diagram showing 2d query algo](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week5/2dquery.png)

After that, I hope to implement and test an n dimensional range searching algorithm.

## Week 6