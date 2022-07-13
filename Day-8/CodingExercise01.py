#Paint Can Required

import math
def paint_calc(height, width, cover):
  can_required = (height * width)/cover
  print(f"You'll need {math.ceil(can_required)} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)