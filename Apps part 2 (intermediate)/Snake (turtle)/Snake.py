
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)




# In the range function here, the left number is the number it will start on,
    # the middle number is the number it will stop on,
    # and the right number is the step.
    # (like either 1 or -1 depending on if you want it to step up or step down)
    # So it would look like this if we could include keyword arguments:
    # for seg_num in range(start=2, stop=0, step=-1):
    # in this case, instead of starting on 2, in the future we may add more starting segments,
    # so we will use len(segments) instead of 2.
    for seg_num in range((len(segments) - 1), 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)