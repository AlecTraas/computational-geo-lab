import math
import random

import drawsvg as draw
from drawsvg import Drawing
from hyperbolic import euclid, util
from hyperbolic.poincare import *

# For some reason, the imaginary components of Line.from_points(r1,i1,r2,i2) are negative. That is, up is actually down.
# Also, weirdly enough, the geodesic rendering is kind of wonky. Look at the example of the red and blue geodesics.
# They meet at the same point, but I suppose because they aren't really rendered faithfully to the poincare disc,
# they don't appear to approach the same point along the unit circle. Very janky...

#initialize canvas
d = Drawing(2.1, 2.1, origin='center')

#line 1
l_1 = Line.from_points(-0.5,1,1,0,True)
d.draw(l_1,fill='none', stroke_width=0.005, stroke='red')

#line 2
l_2 = Line.from_points(0,-1,-0.5,1,True)
d.draw(l_2,fill='none', stroke_width=0.005, stroke='blue')

#line 3
l_3 = Line.from_points(0,-1,1,0)
d.draw(l_3,fill='none', stroke_width=0.005, stroke='green')

#initialize unit circle
d.draw(euclid.Circle(0, 0, 1), fill='none', stroke_width=0.01, stroke='black')

d.set_render_size(w=800)

#output
d.save_svg('images/out.svg')