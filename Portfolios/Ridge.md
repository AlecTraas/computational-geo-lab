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

![diagram showing 2d structure works](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week5/2dtree.png)

My next step in implementing this algorithm will be first to interpret a 1D and 2D range tree creation and searching algorithm. The book provides pseudocode for these algorithms but they are not scaled to work for an n dimensional query. 

![diagram showing 2d build algo](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week5/2dbuild.png)

![diagram showing 2d query algo](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week5/2dquery.png)

After that, I hope to implement and test an n dimensional range searching algorithm.

## Week 6

This week I focused on getting working implementations of my 1D, 2D, and nD range query algorithms. I first started by creating a node class used to create and traverse the tree.

![node1](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/node1.png)
![node2](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/node2.png)

The class is fairly simple, consisting mostly of getters and setters and a display method. It has a left and right child, the left should have a value less than and the right a value greater than or equal to. It has a "canonical tree" which is the search tree of the spanned points ordered on the next variable (if there is one). This is useful for all cases greater than the 1D case where you need trees for the next variable. It also has a "subtree" which is the points it spans. This is useful for the 1D or any case where you are on the last searched variable.

I first created the findsplit node method. I slightly altered it from the textbook to make it easier to generalize. I included a dimension parameter so that it could be used regardless what variable you were searching on. I also change it so that the right subchild included the median node whereas the book had it included in the left. It was just slightly easier to code and avoid index out of bounds errors when creating the method to create the tree.

![findsplit](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/find_split_node.png)

I next created the 1D range query method. This is extremely close to the algorithm stated in the book. I also created the check_leaf method to simplify and not reuse code. I changed the algorithm to account for the right subchild including the median by checking >= rather than > if I were to traverse right in the tree. Once the path to start traversed left or the path to end traversed right, I added all points spanned by the opposite child to a field "answer" which stores my output.

![1D range query](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/1dqueryalgo.png)

![check leaf](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/checkleaf.png)

The next algorithm I completed was the create 2D range tree algorithm. This has some slight discrepencies from the book algorithm so that it was easier to generalize. If I am not on the last variable, I set the next canonical subtree. Else, I set the subtree span. This is because I will only need the span on the last variable and the canonical tree everywhere else. The function returns the root of the tree. You also have to be sure to sort the values on the next variable so that the tree can be constructed based on median values.

![2d range tree](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/create_2d_range_tree.png)

I then moved on to the 2D query algorithm, again accounting for the median placement discrepancy. This was overall very similar to the book's algorithm. Instead of adding points to my answer whenever a path to start goes left or end goes right, I call my 1D query on the canonical tree of that point with the given next parameter. 

![2d query](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/2dqueryalgo.png)

Ultimately, I decided to make a second version for my nD solution so that I could clean up and generalize my code. The node classes has some slight differences from before as I renamed subtrees to span as it made more logical sense to call it this. I also renamed canonical subtrees to just subtrees to simplify.

![new node class](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/ndnode1.png)
![new node class](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/ndnode2.png)

I consolidated the methods pertaining to range tree creation into a range_tree class since it is a data structure and makes sense to be interpreted as a class. I also added a display function that prints the range tree ordering on the first variable. Besides slight renaming, the creation functions remain largely unchanged. 

![new range tree class](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/ndcreatetree.png)

Lastly, I consolidated all querying related methods into a range search query class. This should help with modularity if I hope to implemented other querying algorithms. Most functions remain unchanged except for the recursive query function. Instead of having one function for 1D, and another for 2+D, I consolidated both into a nD function. It now takes in a parameter for the number of variables in the range tree and the current variable number being searched over. Every time the function finds a possible subtree of points, it recursively calls itself with the new subtree on the next variable. This happens until we have reached the maximum depth at the number of dimensions in the tree.

![new range searching class](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/ndquery1.png)

![new range searching class](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/ndquery2.png)

I also tested my nD algorithm on various 1D, 2D, and 3D queries.

![1d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/1dtests.png)

![2d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/2dtests.png)

![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week6/3dtests.png)

My next goal is to ensure the algorithm works on points that share variable values. Currently, the sorting order of points if they have the same value for the current variable is undefined. This leads to problems when these points span across the median. One or more points will be to the left of the median with equal value. However, we should always include points that are greater than or equal to in the right subtree.

To fix this, I am defining an ordering for nodes through a compareTo method. Instead of just comparing based on the current variable value, it will compare on current variable value, then the next if they are equal, then the next, etc. This ensures that points will be placed on the side of the median we expect them to, unless there are multiple points with all the same variable values. However, in a database, points have a unique "id" identifier so all variables of separate points can never be equal.

Furthermore, I would like to look into optimizations for this strategy, like fractional cascading, and what methods could be used for range queries that are not orthogonal. I also want to look into how to a efficiently add points to a range tree. 

## Week 7

This week we prepared for a presentation for the UVA Math Club about our current progress. We tried to focus on hands-on activities to more intuitively explain our algorithms. For our convex hull algorithms, we did this using thumbtacks, string, rubber bands, and a bulletin board. We first showed an intuitive visual of what a convex hull is by expanding a rubber band around a collection of thumbtacks, representing our points. The polygon formed by the band represents a 2D convex hull.

While this is a good visualization for people, it's not practical for computers. This led us into our giftwrapping algorithm. We started with the leftmost point which is guarantted to be on the hull and tacked the string to the board. We then continued wrapping the string around the tack that had the minimum angle to the previous segment until we ended back up at our original point.

We next displayed the graham scan algorithm. We started with the string at the bottom most point and scanned through the points in order of polar angle to this base point. We kept doing this, making sure we were always forming a convex, counter clockwise turn. Otherwise, we would backtrack to fix our hull such that every connection fit these constraints. We did this until reaching the point with the maximum angle.

Lastly, we displayed the quickhull algorithm using rubber bands. We started with the rubber band connecting the lowest and highest y value tacks. We then split the problem in two. For each subhalf, we added the point furthest from the line to the hull to form a polygon. For each side, we found the furthest point away that was not yet enclosed by the polygon and added it. We repeated this process until all points were enclosed.

As for my personal project this week, I focused on allowing for repeated values for points. I did this by defining a custom comparator and sorting method to implement it. The new comparator compares the current index being compared first. If and only if this is equal, it compares on the next index values. If the subsequent values are the same, then it compares on the next, and so on. As a result, the points are only considered equal if all of their values are the same. If the points have different values at the index, it works the same as a regular integer compare method.

Implementing this allows me to search for values even if multiple have the same index value. In previous iterations, this was not the case. Consider if we make a tree on index i and the median value of i is shared by three points. Theoretically, these points can span both sides of the median. However, when traversing the tree, we would expect all points with value greater than or equal to the median be in the right subtree.

In the new iteration, we compare the other values in addition to the value at i. If the previous case still occurs, the new sorting algorithm will make sure that whatever is left of the median has a lesser comparison value than the median. This way, if we are looking for a point, we will always know which subtree it will be in regardless of whether or not it shares a value.

My next goals for the project are to explore added efficiency from fractional cascading. Additionally, I want to determine if there are efficient ways to add points to the range tree while keeping its structure so that we do not need to recalculate it every time the list of points changes. I also would like to explore changing the sorting comparator to allow the algorithm to work for non-orthogonal queries. As of now, I am unsure whether or not this is possible. However, I feel that we may be able to compare each i value to an expected or boundary value which may allow us to search the tree.\

## Week 8

This week, I did not make as much progressas in past weeks on the project. I mainly spent my time deciding in what direction I want to take it next. The topic that I have been exploring is dynamic range trees, which is a way to add or delete items from the elements you search over while still maintaining the structure of the tree instead of creating a new one. Past implementations of my project have used static trees, where the elements searched were assumed not to change. While this is more simple, it does not make sense in most applications, like databases, to make this assumption. I have previous experience implementing dynamic binary trees like balance factor based binary trees or red black trees. However, nd range trees will be significantly more complex because of their recursive structure. Not only do you have to rebalance the initial tree, you must also update which elements are included in subsequent trees and rebalance them as needed.

I found a few research papers regarding this topic. The literature on the subject seems very open and has not reached a set of 'ideal' algorithms. Thus, I am looking more so to create any working dynamic search rather than one that is more optimized. 

## Week 9

This week, I focused on create a simple but maybe not optimized strategy to update the range trees. While my strategy is not fully complete, it is very similar to self balancing AVL trees, but with slight discrepancies. First off, when an item is added to the sorted list, keep track of what index it is added at and what item was previously at this index (if it is added at the end of the sorted list, disregard). Based on the index, follow the new element down until you reach a leaf. For each node you traverse (including the root) recursively call this function to add this element to the canonical subtree for that node. Eventually, you will reach a leaf node. Since our tree is always full, compare the index of this node to the index of the leaf. If the index is less, make the new element the left child and itself the right child. Else, swap the value of the leaf with the value of the new element. Make the existing element the left child and the new element the right child. It is also important to consider that you have to update lesser depth medians as well. I am not yet exactly sure how to achieve this without recalculating, but I believe it has something to do with switching out median occurrences of the element that was previously at the index with the new element. I am not sure if there are edge cases where this does/doesn't work. 

Once you have added the new element as a leaf and potentially updated the medians, your tree may now be unbalanced which would decrease search efficiency. The tree could grow wildly to one side or another which means we can no longer efficiently binary search. As a result, I will use a balance factor calculation typically used to balance binary trees. A balance factor is calculated by the maximum amount of edges needed to reach a leaf in a subtree. For every non leaf node, the balance of the left and right subtrees should not differ by more than one. From the position we added the new element as a leaf, we must recurse back up the tree, calculating the balance factor each time. If we find a case for a root of a subtree where its right subtree has a greater balance factor by 2 or more, we will perform a "left rotation." This works by making the right child the new root, replacing the left child of the new root with the old root, and making the old left child of the new root the right child of the old root/new left child. It is important to keep track of the canonical subtrees during this process. The new root has the subtree of the old root. The old root now has the subtree of its left child plus the old left child of the new root. 

The same operation but reflected happens when the left subtree is 2 or more greater than the right subtree. Below are some visuals to better describe rotations.

Trivial Right Shift
![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week8/rightshift1.png)

Larger Right shift
![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week8/rshift.png)

These images were taken from Professor Brianna Morrisson's Data Structures and Algorithms 2023 Spring Slide Deck.

## Week 10

This week we pivoted into implementing shortest-path algorithms as a team. The main or most popular shortest path algorithm is Dijkstra's algorithm, which is a greedy breadth first search algorithm that works by traversing to the nearest unexplored node to the start and seeing if there are any paths to a node that are shorter than a previous one we have found. 

Dijkstra's is performed on a graph, a collection of points, called vertices, where connections between points have a specified "weight." The shortest path between points is the one that minimizes the total weight of the edges it uses. We define one "start" node. We initially assume all vertices are an infinite distance from the start. The start is a distance of 0 from itself. From here, we visit the node that we have not visited yet that has the least distance from the start. We look at all the edges coming out of this node, and, of the edges that connect to a node we haven't visited, see if taking this route is faster than the shortest previous route (the distance to the current node + weight of edge < current shortest route). If so, update our distance from the start node value for that vertex. An example of how this works can be seen below:

Remove the node with the shortest distance (initially the start node):
![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week10/dfirst.png)

Update the distance of the top node to the new lowest distance:
![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week10/dfirstfirst.png)

Update the distance of the top node to the new lowest distance:
![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week10/dsecond.png)

Explore the node with the shortest distance:
![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week10/dthird.png)

Reapeat this process:
![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week10/dfourth.png)

End when all nodes have been visited:
![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week10/dfifth.png)

These images were taken from Professor Robbie Hott's Data Structures and Algorithms 2 2024 Spring Slide Deck

One common way to implement Dijkstra's algorithm is with a priority queue or minheap. Store all of the nodes in the collection based on their distance from the start, initially infinite. If you find a shorter path to a node, update its distance in the collection. When need to explore the next closest node, pop() the collection in O(logn) time.

## Week 11

This week we focused on making an efficient implementation of dijkstra's algorithm. To represent graphs, I used NetworkX, a common graph library in python. One of the inefficiencies of dijkstra's algorithm is decreasing the value of a node's distance in the collection. Because priority queues and minheaps only ensure that the first or root element is the minimum, we do not know where in our collection each element is stored. Thus, if we want to update its value, we must find it first, taking O(n) time. However, we can improve on this by storing pointers to the elements rather than the elementes themselves in the queue. This allows us to update the underlying value in constant time. We still must rebalance the heap after, taking O(logn) time.

A python library that allows me to do this is dictheap. Dictheap allows for easy access to and change of the value of an item in the heap. Each key can be though of a pointer to its value. Additionally, dictheap automatically rebalances the heap after a value is changed.

One other efficiency I added is that the main loop of dijkstra's runs only until the ending node removed from the heap. Because dijkstra's is greedy, we assume that once it is removed from the minheap, we will not find a shorter path to it. This is because the node removed is currently the one closest to the start. Any other unexplored paths must pass through a node that is further from the. Since we assume all edge weights are positive, any subsequent path to the removed node cannot be shorter than the previously found shortest path. In short, once we remove a node from the heap, it means we've found its shortest path already. Thus, we don't have do any more calculations. 

In order to track the actual path of the node, we assign each node a "parent" in a dictionary representing the next to last node in the shortest path to this node. In my implementation, this is originally null. When we find a new shortest distance from a node, in addition to updating the distance, we will set this node's parent to whichever node the edge came from. One dijkstra's main loop runs to completion, we can iterate up through the parents from the end node to find the path.

If you were to do this to a normal list, the run time would be O(n^2). This is because we must add the parent to the head of the list, which takes O(n) instead of O(1). The reason is that when adding to the head of an index-based list, we must update the index of all other things in the list whereas when we add to the tail, we don't need to update any other indices. We add to the head at most n times if every node is taken to get from the start to the end. 

In order to circumvent this, I used a stack. A stack is a LIFO data structure where the last thing you added to the list is the first thing that comes out when you remove. The add or "put" function of the stack is O(1), The remove or "pop" function of the stack is O(1). We call each up to n times if all n nodes are included in the path. Thus, we can add the parents to the stack as we bubble up and then remove them all in reverse order in O(n) time. 

Lastly, the end node must be added to the end of the reversed list. A picture of my code is shown below:

![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week10/dijk-code.png)

In addition to this, I tested my code against NetworkX's built-in shortest path function and graphed the graph using matplotlib to make sure this made logical sense. I ran 1000 tests at a time and used python's "assert" keyword to determine that the lists contents were equal.

![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week10/matplotlib-screenshot.png)

![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week10/dgraph2.png)

I also tested the runtime of my code against the built in function to determine how efficient. Over a series of 1000 run tests, my implementation is approximately 3.5 times slower than the NetworkX one. This may be due to inefficiencies in the libraries I used, missed optimizations, and python inefficiencies if NetworkX uses a different underlying language.

![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week10/dtimetest.png)

![3d tests](https://github.com/AlecTraas/computational-geo-lab/blob/main/Colab/Ridge/pictures/week10/time2.png)


