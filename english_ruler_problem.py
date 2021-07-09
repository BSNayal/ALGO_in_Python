''' The English ruler problem is a classic example of a recursion problem
    We are given a pattern that is getting repeated and we have to draw it.
    Ex:- 
    ----- 0
    -
    --
    -
    ---
    -
    ----
    -
    ---
    -
    --
    -
    ----- 1
'''

def draw_ruler(inches, majorticks):
    #We draw the initial line since before that there are no ticks
    draw_line(ticks=majorticks, label='0')
    #We run a loop to draw the ticks in between two major ticks
    # In the loop we print the next major tick also because last tick will
    # not having any ticks after it.
    for i in range(1, inches):
        draw_minorticks(ticks = majorticks - 1)
        draw_line(ticks=majorticks, label=str(i))

def draw_line(ticks, label=None):
    line= '-' * ticks
    if label is not None:
        line = line + ' ' + label
    print(line)

def draw_minorticks(ticks):
    if ticks > 0:
        draw_minorticks(ticks - 1)
        draw_line(ticks)
        draw_minorticks(ticks - 1)

draw_ruler(2,5)