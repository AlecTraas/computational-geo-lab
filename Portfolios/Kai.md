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

## Week 2 (2/7 - 2/14)
helpful papers for high-dimensional convex hull algorithms:

[The Quickhull algorithm for Convex Hulls](https://dpd.cs.princeton.edu/Papers/BarberDobkinHuhdanpaa.pdf)

[Visualizing High-Dimensional Data: Advances in the Past Decade](https://www.sci.utah.edu/~beiwang/publications/Vis_HD_STAR_BeiWang_2015.pdf)
