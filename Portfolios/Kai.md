# Kai's Portfolio
## Week 1 (1/31 - 2/7)
During our January 31st meeting, our group brainstormed and discussed various methods for computing the [Convex Hull](https://en.wikipedia.org/wiki/Convex_hull) for a set of 2d vectors. We discovered methods for computing the convex hull that fall under two general categories: angles-based and distance-based. My contribution was an angles-based one similar in format to the [Gift Wrapping Algorithm](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm), though with the help of my group members and mentors we managed to approach the [Quickhull](https://en.wikipedia.org/wiki/Quickhull) algorithm, which is significantly more clever and has cheap `O(n log(n))` time complexity. I am particularly interested in how the quickhull algorithm abstracts into higher dimensions and I'll research how others achieved this in the past. This week I aim to complete an implementation of both the 2d and 3d quickhull algorithms, with my developing an understanding of Python's graphics libraries an ancillary objective.

Today is 2/3, and I've completed my lightly-debugged, unoptimized first draft of the 2d quickhull code. I have found challenges in two main areas: dealing with Stack Overflow and dealing with Python. From my research I knew generally what form my code should take, but for the `aboveLine` and `furthestP` functions I opted to take strip formulas from Stack Overflow instead of creating them by myself. This, however, turned out to be a mistake, as one of my biggest challenges was trying to debug the `furthestP` function. The bigger challenge actually ended up being dealing with the Python interpreter. I constantly kept getting `TypeError`s and `IndexError`s, and I blame this on [Dynamic Typing](https://stackoverflow.com/a/1517670). That is, if I had to assign the intended variable types and array sizes myself (like I would in C++, Java, or Rust), errors with types and indecies likely wouldn't get past me so easily. That said, I have found myself rather liking the simplicity and abstraction (maybe over-abstraction?) of Python's syntax.

Today is 2/6, and I have fully completed an unoptimized, rather messy implementation of the 2d quickhull algorithm. Yesterday I was able to get my code into an error-free state, though the output was always incorrect. Here are a couple output sets I got in the form of `X|Y` tables:

x|y|*and*|x|y
-|-|-|-|-
inf|inf|-|0|0
inf|inf|-|0|0
5.8942|2.2572|-|None|None
None|None|-|None|None
1.2945|4.8593|-|0|0

Clearly, these are not the types of results I was looking for. I scowered my code and found few issues, essentially hitting a brick wall in my progress. Today, I thought I would turn to graphing values myself, and walking through the algorithm in a test scenario. I set up a test case for the section of the code which determines if a point is within a triangle, and I used [Desmos](https://www.desmos.com/calculator) to visually graph the results. What I found is that I was incorrectly determining which points lie outside the triangle formed by `A`,`B`,and `P`:

<img src="https://i2.paste.pics/ea2bf739d8c7f4ecdb1245eb1436e815.png?trs=dd494636c42af34438770bca22294014fd61ebd0cb110405d73f174c77ec4014&rand=ZBPwnrNO5A"  width="40%" height="20%">

With my newly corrected convex hull-generating program completed, I wondered if, by computing the convex hull for a large number of sets at varying point quantities, I could computationally approach the answer to the following question:
> What is the probability, for a set of 2d points, that a randomly-selected point lies on the convex hull of the aforementioned set?
I, therefore, mocked up a quick test:
```
def check_and_increment_counter(hull_set, points):
    for point in hull_set:
        if np.array_equal(point, points[rnd.randint(0, len(points)-1)]):
            return 1
    return 0

counter = 0.0
for i in range(1,100000):
  hull_set, points = runProgram(10)
  counter += check_and_increment_counter(hull_set, points)
print(counter/100000)
```
This returned $0.4632$, or roughly $46\\%$. How interesting! I took the results for a few other sets of  points as well (at a smaller sample size of $50,000$), and plotted the results on Desmos:

<img src="https://i2.paste.pics/6391d66525fe358ced7a0672402470db.png?trs=dd494636c42af34438770bca22294014fd61ebd0cb110405d73f174c77ec4014&rand=cLR3G1H7r0"  width="80%" height="60%">

Though there is a fair bit of deviance from the true, expected values one would achieve by hand, I believe this plot makes a decent amount of sense. As the number of points grows to infinity, we can expect 
$$\lim_{x\to\infty} \frac{a}{x^b} \to 0$$
Essentially, the size of the convex hull doesn't grow fast enough to keep up pace with the set of points it is derived from.

## Week 2 (2/7 - 2/14)
During our last meeting, we worked on fixing our 2d convex hull code and we discussed the algorithm we would use for 3d quickhull and, eventually, arbitrary-dimension quickhull. As I understand it, the algorithm is as follows:
```
// For a d-dimensional set of points:

1. Generate a polygon with d-1 points and facets
2. Remove points within the polygon
3. Assign each point to the facet it is above
4. For each facet that has points above it:
    4.1. Find the furthest point above the facet
    4.2. Find the horizon ridges for that point
    4.3. Connect the point to its horizon
    4.4. Remove the now internal facets and points

// Repeat 4 until no facet has points above
```
This week I have attempted to implement this algorithm for the 3d case. I began by researching classes in Python, as I thought an [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming) approach would suit this algorithm best because of how many interlinked arrays and lists need to be created and stored. Most of the time I spent working on the program this week was spent building out and debugging the `define_tetrahedron()` function:

##### Preliminary Pseudocode
In order to effectively and cleanly write the function, I started with a [pseudocode](https://en.wikipedia.org/wiki/Pseudocode) description. I decided to forgo a conventional, code-adjacent style of pseudocode, instead opting for a more plain language, bullet-pointed syntax.
##### Basic Functionality
Following my completion of pseudocode, I wrote the function in Python, taking little time to check the correctness of my code. Thankfully, it was entirely functional besides one persistant bug in my code.
##### Coding Headache
I consistantly faced one issue in my programming of the `define_tetrahedron()` function: duplicate point selection. Patricularly in low point-count cases, my function would often select the same point as its pick for two of the tetrahedron's vertices. This obviously caused issues, as in such cases a triangle or nothing at all would be outputted as opposed to a complete tetrahedron. In the end, my solution was as follows: 

I went from this
```
i = [self.points[:,0].argmin(),
    self.points[:,1].argmin(),
    self.points[:,2].argmin(),
    self.points[:,1].argmax()]
```
to this
```
temp = np.array(self.points)

i = []
k = temp[:,0].argmin()
i.append(k)
temp[k] = np.inf
k = temp[:,1].argmin()
i.append(k)
temp[k] = np.inf
k = temp[:,2].argmin()
i.append(k)
temp[temp == np.inf] = -np.inf
temp[k] = -np.inf
k = temp[:,1].argmax()
i.append(k)
```

The bug, simply put, stemmed from having no duplicate regulation whatsoever. By allowing for a second temporary array that can be edited, we maintain correct indices in the `i` array. Similarly, the act of setting the points in temp to `np.inf` or `-np.inf` after selection allows us to ignore the selected points without changing the indecies of the rest of the points.
##### Belated Completion

Though I didn't seem to get much work done on the program this week, I hope that in the next I may complete it once and for all.

## Week 3 (2/14 - 2/21)
In this week's group meeting, we discussed the future of our subgroup, and what direction we will go in with future projects. As a natural successor to the convex hull, we began conversation about [Voronoi Diagrams](https://en.wikipedia.org/wiki/Voronoi_diagram) and [Delaunay Triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation), with Lam presenting resources for us to futher research these on our own. As we spoke about capstone projects to begin after Spring break, the idea of computing the convex hull in [Hyperbolic space](https://en.wikipedia.org/wiki/Hyperbolic_space) particularly caught my attention, as I've been trying to find an excuse to program a non-euclidean renderer for quite some time. That said, I have to admit that the convex hull intimidates me, as I'm already finding it relatively challenging to program the 3d Quickhull algorithm.

As far as my progress on the 3d Quickhull program goes, I feel it's going quite smoothly. I've had a couple issues with my rusty linear algebra skills, but I feel myself rapidly regaining my intuition as I work to solve all the interesting little components of the algorithm. The most fun I've had this week working on my project is with the `clear_internal_points()` function. It has taken an estimated 3 hours of banging my head against a wall and contacting our mentors for me to get it functional, but I can proudly say that it is definitely the most clever or satisfying bit of code thus far. I will explain it below, as I'm sure you could derive a similar joy from the brilliance of the function.

```
def clear_internal_points(self):
  hull_centroid = np.sum(self.hull_points, axis=0) / len(self.hull_points)
  queue = []
  for p in self.points:
    for fc in self.facet_centroids():
      if np.dot(fc - hull_centroid, p - fc) > 0:
        queue.append(p)
  seen = set()
  queue = [x for x in queue if tuple(x) not in seen and not seen.add(tuple(x))]
  self.points = queue
```

The whole idea of the algorithm is as follows:
- find the centroid of the hull $h_c$ by averaging the points together
- for each point $p$:
- for each facet centroid $f_c$:
- if the dot product between the vector formed by $f_c-h_c$ and $p-f_c$ is negative, then the point if within the polyhedron

## Week 5-6 (2/28 - 3/13)
Foreword: This is the third time I am rewriting my portfolio. I have accidentally left the page without committing **Twice**. It's very frustrating that I've written 6 full paragraphs, but now I have to restart again. I will be committing every five minutes from now on so that I'm not doomed to relive Week 5 for eternity.

Last week we presented to the wider Geometry Lab, and got to see what the other subgroups are working on. It went pretty well, but we had to halt work on our projects to prepare. This week we determined what projects we will work on next, with Alec and Lam giving me an introduction to the various $\mathbb{H}^2$ to $\mathbb{R}^2$ projection methods. We mainly discussed the [Poincaré Disk model](https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model), in which the infinite hyperbolic plane is crammed into a Euclidean unit circle. This model is most useful for its preservation of angles and for not extending to infinity. 

<img src="https://raw.githubusercontent.com/AlecTraas/computational-geo-lab/main/portfolio-images/poincare.png"  width="40%">

I also proposed my own model, which projects orthogonally and therefore occupies the entire Euclidean plane (this would preserve curvature, but not much else). This, apparently, has already been proposed by David Gans. *My* model is, thereby, actually called the [Gans model](https://en.wikipedia.org/wiki/Hyperbolic_geometry?scrlybrkr=58c7a161#:~:text=the%20models%20(below)-,The%20Gans%20model,-%5Bedit%5D).

As for my work on the 3d Quickhull program, I have completed all aspects of the program besides the whole remeshing-to-connect-to-the-horizon deal. Today, however, I worked out the first step of that process instead of paying attention to my teacher:

<img src="https://raw.githubusercontent.com/AlecTraas/computational-geo-lab/main/portfolio-images/blackboard.jpg"  width="70%">

What this is meant to detail is the algorithm by which I can determine which faces are seen and which ridges are on the horizon. I thought about the convex polyhedron as a simple sphere, and I deduced that the seen facets can be found by simply taking the dot product between the normal of each facet and the "eye" point. The horizon, therefore, would be the set of edges only contained by one facet. 

<img src="https://raw.githubusercontent.com/AlecTraas/computational-geo-lab/31e5eec9d2fb97d6c409aa3198b8aafc7623ffa0/portfolio-images/oops.svg"  width="50%">
As I write this, I realize there is a major flaw in my method. As you can see in the image, unless the "eye" point is infinitely far away, There will always be the chance for a band of facets just outside the visible range to be marked as visible. I need to account for this one way or another.

I have finished the first draft of my code, and I am currently working to debug the program. Unfortunately, I have found I substantial number of issues like the one I just described.

As for progress on the $\mathbb{H}^2$ Convex Hull Program, I have been researching libraries to help with hyperbolic geometry display and abstract away some of the code I'd have to write myself. One nice-looking library I've found is the [geometry-tools](https://public.websites.umich.edu/~tjwei/geometry_tools/geometry_tools.html) API by Theodore Weisman. I will investigate it further, but it seems very promising.

## Week 7 (3/13 - 3/20)
In this week's meeting, Alec and Lam helped us get started on our capstone projects, with Lam attempting to get Weisman's API working in Colab. Unfortunately, it posed too many challenges, and we agreed it would be best for me to stick to a different IDE on this one. I also spent some time discussing point-geodesic distance formulae with Alec, and I plan to do work this week to figure out exactly how I will implement one in Python.

Today, Saturday 3/16, I have been struggling to clear up an issue that has gone under the radar in my code for quite some time. A while ago, I identified that there exist indexing issues within my program stemming from the resizing of the global `points` array. In [testing](https://colab.research.google.com/drive/1dS4k5Yes62GSvN-7cx40jfRff217FLMT?usp=sharing) my solution, I discovered a fatal flaw with the `clear_internal_points()` function. For a few uniquely-situated points, their position relative to the polyhedron is incorrectly identified. That is, some points which are inside are marked as outside, and vice versa. I just now, 5 or so hours later, figured out what has been going wrong with my code. Where I should have been evaluating $f_n\cdot(p-f_c)$, I was mistakenly calculating $(f_c-h_c)\cdot(p-f_c)$ (where $f_n=$ facet normal, $f_c=$ facet centroid, $h_c=$ hull centroid, and $p=$ point). After fixing that and a few other small tweaks, `clear_internal_points()` is, as far as I can tell, complete.

## Week 8 (3/20 - 3/27)
The main event of this week was our meeting with the UVA Math Club, where we demonstrated what algorithms we've been working on in Geometry Lab. I particularly liked Matthew's demonstration of pagerank, as I found it to be quite engaging and interesting in subject matter. Unfortunately, our demonstrations of the 2d convex hull algorithms seemed to have fallen through, for the most part due to structural issues with the thumbtacks.

As for my work on convex hulls, I have spent this week largely focused on trying to get Weisman's API working on my machine and coming up with my own formula for the angle between intersecting geodesics. I have been unable to get `geometry-tools` working on my computer due to my poor understanding of relative paths. I have, however, been relatively successful in creating a method for finding the angle between geodesic segments, as I noted in [this](https://www.desmos.com/calculator/pow2ovw2tw) Desmos workspace. There is probably a cleaner or cleverer method (using inverse hyperbolic trig functions, I presume), that I missed in my Euclidean blindness. This is something I would really like to discuss in this afternoon's group meeting.

In my research of the upper half plane model, I found this [cool demo](https://www.geogebra.org/m/Z4SWyEnC) I couldn't help but share.
