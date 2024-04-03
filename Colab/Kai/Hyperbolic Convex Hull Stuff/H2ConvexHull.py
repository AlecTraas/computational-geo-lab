import math
import random

import drawsvg as draw
from drawsvg import Drawing
from hyperbolic import euclid, util
from hyperbolic.poincare import *

#initialize canvas
d = Drawing(2.1, 2.1, origin='center')

#initialize unit circle
d.draw(euclid.Circle(0, 0, 1), fill='none', stroke_width=0.006, stroke='black')

#line 1
l_1 = Line.from_points(-1,0,1,-0.5)
d.draw(l_1,fill='none', stroke_width=0.006, stroke='red')

#line 2
l_2 = Line.from_points(0,-1,-0.5,1)
d.draw(l_2,fill='none', stroke_width=0.006, stroke='blue')

#line 3
l_3 = Line.from_points(1,1,0,0)
d.draw(l_3,fill='none', stroke_width=0.006, stroke='green')

d.set_render_size(w=800)
d.save_svg('images/out.svg')