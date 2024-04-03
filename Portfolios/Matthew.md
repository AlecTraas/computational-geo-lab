# Matthew's Portfolio
## Week 1 (1/31 - 2/7)
 
  During our first meeting on 1/31, we discussed methods and algorithms to find the 2D convex hull given a set of points. Throughout our discussion, we were able to land on the gift wrapping algorithm first. I found this algorithm to be the most intuitive to understand. Initially, my mindset was very focused on visual ways that a human could find a convex hull, such as visually shrinking a large circle like a rubber band to then fit over all points that would form the hull. As Lam mentioned though, what is easy for the human brain to do would be very hard for the computer to execute. Thus, I found the gift wrapping method to meet in the middle of this nice visual of what the algorithm was doing, while also being manageable to code and for the computer to execute. 
  
  As we wrapped up our discussion, we were also introduced to the quick hull method, where we can split our set of points into two and form convex hulls between smaller sets of points that can be rejoined back together to form the whole convex hull. Compared to the gift wrapping algorithm, I found this method unintuitive at first, but rationalizing this method as a divide and conquer sort of idea made it more familiar. Walking away from our meeting, I had an idea of wanting to implement something along the lines of the gift wrapping algorithm, or something that used the angular behavior between lines to actually formulate the convex hull.
  
  As I began to actually start coding, I found I was stumped on where to actually start formulating the algorithm to iterate through the set of points. It was difficult identifying what needed to be tracked during each iteration, and when it was okay to move on to testing the angle of another set of points. Initially, I wanted to use some sort of dot product function to track the angle between any three consecutive points that were being tested as a part of the convex hull (the "middle" point would act as an base of the vector while the other two points would be the head forming two different vectors). While I had coded this function, trying to implement it as a part of my algorithm didn't seem very fitting, as the dot product was not able to convey the greatest amount of information apart from the behavior of the angle, not whether it was directionally correct or not.


## Week 2 (2/7 - 2/14)


During our meeting on the 7th, we discussed further about our algorithms to find the convex hull given a set of points. Rather than focusing on the conceptual formation of our algorithms, we dove more into the nitty gritty coding side of our algorithms. Prior to the meeting, I was searching online for other possible convex hull algorithms I could implement that were also efficient at the same time. This led me down the rabbit hole to finding the graham scan algorithm, which uses the orientation [(link)](https://www.geeksforgeeks.org/orientation-3-ordered-points/) of an ordered set of 3 points to determine if a point is on the hull or not. I found this idea of orientation also much easier to apply in the context of our problem as a test for points on our hull as well, as this characteristic only required two other points to make a relative measuring. 

When implementing the graham scan algorithm, I found the process of iterating through points to be pretty straightforward. First, I had to start with the point with the lowest y-value (the anchor point), and then measure the polar angle made between all other points and the anchor point. I then sort the points by this polar angle from smallest angle to greatest for the algorithm to then iterate through to test orientability. Here, it is important to understand in terms of orientation, we want any 3 consecutive points on our convex hull to have counterclockwise orientation. That way, when iterating through points, the convex hull is able to form lines between hull points in counterclockwise order moving through the points sorted from smallest angle to greatest. The algorithm would then iterate through each point and check if the orientation of the next point formed a counterclockwise turn, thus slowly wrapping around the entire convex hull.

I found my generated plots of this also turned out pretty well using a set of 100 randomly generated points:

![image](https://github.com/AlecTraas/computational-geo-lab/assets/158364295/bc68f009-f845-4b78-890a-7b67f03e1d55)

While this seems to work as a general solution, I am unsure of how edge cases would hold up in the algorithm I've coded. In the future, I hope to dive more in depth into edge cases that dive into collinearity between points.

## Week 3 (2/14 - 2/21)
During our meeting on the 14th, we pivoted away from our previous discussion on convex hulls to focus on the topics of Delaunay triangulations and Voronoi diagrams. In particular we discussed the definition of both and their intriguing relationship. Given a set of points on a plane, a Voronoi diagram seeks to partition the plane in such a way that each point is contained within its own cell. These cells are formed in such a way that any point within the cell is closest to the given point that defines a cell. The boundaries of each of these cells is given by the perpendicular bisector of the line between any two points. When diving deeper into the textbook outside of our discussion, the ideas around Voronoi diagrams and how they were assembled seemed rather intuitive. However, I'm currently struggling to see how to even go about thinking algorithmically with the formation of these diagrams. 

During our meeting on the 20th, we began to develop our presentation for the group meeting on the 27th. We decided we were going to mainly focus on our work surrounding the convex hull. As for the structure and content of the presentation, we decided on including an introduction to the concept of a convex hull, the algorithms each of us worked on and a high level look at how each algorithm works, as well as applications of the convex hull. For our presentation, we want to focus on visual aids and diagrams to hopefully make our work intuitive and easy to understand for our audience. Overall, I found this meeting to be really productive in setting up the overall structure and establishing what each group member was going to focus on and work on to finalize for the 27th.

## Week 4 (2/21 - 2/28)

This week, we mainly focused on preparing our presentation for 2/27. As I was tasked with presenting on the Graham Scan algorithm, and after listening to feedback from my group members, I created an animation of a very basic run through of the Graham scan algorithm. Our thought with this basic animation was to show the "always turning left" method this algorithm relies on. Then for the cases where we end up turning right, we "pop out" the middle point of the three most recent points that we have iterated through.

![5d61acda-4c43-4e89-89d6-a22da253afa3](https://github.com/AlecTraas/computational-geo-lab/assets/158364295/7c5c4e1b-03ae-4811-9438-b6d1a8295ca4)

## Week 5

Over the course of spring break and the past couple of days, I have spent most of my time familarizing myself with the networkX library. This library basically acts as the one-stop-shop for anything related to graphs. After reading the documentation and walking through a couple of tutorials, I coded a couple of graphs of different types.
![image](https://github.com/AlecTraas/computational-geo-lab/assets/158364295/12b39a8c-55de-479d-ac1a-450c630ba3bc)

I also looked more into possible algorithms I could start to work through now that I have a foundational understanding of the library. One that caught my eye was PageRank, mainly due to its applications in web browsing. In terms of websites, this algorithm determines the "importance" of a website by looking at the websites are directed amongst each other. Websites that are being linked to from other websites are then denoted as "more important". Connecting this back to the idea of graphs, each website could be considered its own node, whereas the links would be looked at as directed edges. 

## Week 6

After our meeting on 3/13, I finalized my capstone idea of exploring the page rank algorithm for directed graphs. For this week, my action plan focused on completing the easier portions of the algorithm. So far, I have worked through creating a function that will update the page rank of a single node. After executing this function for each node, all nodes will have been updated with new page ranks and thus the algorithm can restart a new iteration. But, I am running into a bit of a road block trying to find a way to approximate convergence of the final page ranks without the algorithm iterating a crazy amount of times. One idea I had was recursively checking the past iteration's page ranks with the current iteration's page ranks and if they are close enough (i.e something like every node's previous and current page rank is within one thousandth of one another), then I can end the algorithm and use the current page ranks for each node as the output. But, this approach most likely runs into a similar problem of taking an immense amount of iterations to execute, making this not as feasible with run time most likely being long. Looking forward, I am going to do a little more research on convergence techniques I could possibly look at to optimize this portion of the algorithm.

## Week 7

For this week, I mainly focused on preparing materials to demonstrate the PageRank algorithm for the Math Club meeting yesterday. To demonstrate the PageRank algorithm, I drew out a scaled down network that I could run through a couple iterations of pagerank to showcase the algorithm's general idea and purpose. In order to showcase the shifting pageranks of each node, I used Cheerios to represent the weight / pagerank of each node during each iteration. Thus after each iteration, I would rearrange the Cheerios across the nodes to showcase the pagerank of each node changing. In addition to this physical visual, I also created a couple of slides to showcase the formula used to find the pageranks, as well as listing out pagerank values of this graph as we continue to iterate this algorithm. [Link to slides](https://docs.google.com/presentation/d/1tQokZxLaw0Vm2p3h4fergDCG6TZ40C4z1ovSASbx-jE/edit?usp=sharing)

![430E367E-E338-40CD-BC51-A4A5207C71C3_1_105_c](https://github.com/AlecTraas/computational-geo-lab/assets/158364295/cd2b1e69-c7f3-4c25-a327-682c048342fa)

<sub>Weighted digraph visual I used as a basis to showcase the PageRank algorithm, representing the weights / pageranks as the amount of Cheerios on a specific node</sub>


I have also finished the bulk of my simplified pagerank algorithm, and am troubleshooting the algorithm to completely finalize it. While my algorithm currently ends by checking the difference between the previous iteration pageranks and current iteration pageranks is small enough, I would like to try implementing this algorithm as a stochastic process using linear algebra. This way, rather than relying on doing some large amount of pagerank iterations to eventually reach the final pageranks, we could instead try to find a steady state probability vector that corresponds to the final pageranks. 

I would also like to try implementing a more complex version of the pagerank algorithm through the addition of a damping factor. This damping factor allows for a little more randomness within the network, as in the context of web browsing, the addition of a damping factor simulates web surfers randomly jumping to different websites, even if the two websites are not linked. I feel this would be a great next step to take in scaling up my simplified version of the pagerank algorithm.

## Week 8

For this week, I wrapped up troubleshooting my basic PageRank algorithm. I found most of the issues I was running into were Python-oriented rather than logical problems, which made the trouble shooting process much more difficult than I originally anticipated. For example, when updating my pagerank distributions for the next iteration of the algorithm, I was running into an issue where the correct values were not being outputted. This turned out to be an issue in the setting the updated pageranks as the current pageranks for the next iteration. Instead, I had to recast the updated pageranks as a numpy array again and then set these values as the current pageranks for this code to execute. I thought this was kind of strange, but it works :)

#### Ex:
```python

current_page_ranks = updated_page_ranks
# This would not work, even though both are casted as numpy arrays

current_page_ranks = np.array(updated_page_ranks)
# Recasting the updated_page_ranks again as a numpy array again would output correct values
```


After finishing this troubleshooting, I went ahead and added the damping factor throughout the algorithm. This was actually a pretty easy change to execute without the need for a lot of troubleshooting, as it only required an additional input of the damping factor, d, when calculating the individual page ranks for each iteration from one node to the next.


#### New pagerank formula with damping factor
![image](https://github.com/AlecTraas/computational-geo-lab/assets/158364295/84047edf-4a63-4b67-9e2d-3438695718a8)

<sub> For each individual pagerank, I implemented this formula where d is the damping factor, and N is the total number of pages / nodes <sub>


Moving forward, I feel like I want to build up one more graph algorithm before the end of the semester. Right now, I am thinking of building a shortest path algorithm (like Dijkstra's algorithm) or finding a way of determining if a graph contains a eulerian path or circuit within a given graph.
