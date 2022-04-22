def make_oval(canvas, center: tuple, width: int, height: int, fill_color: str='hotpink'):
    top_left = (center[0] - width, center[1] - height)
    bottom_right = (center[0] + width, center[1] + height)
    canvas.create_oval([top_left, bottom_right], fill=fill_color)

def make_circle(canvas, center: tuple, radius: int, fill_color: str='hotpink'):
    make_oval(canvas, center, radius, radius, fill_color=fill_color)


## You can add any other shape functions you write here. For instance, you might consider
## grabing the make_square function from Tutorial 2.


def make_creature(canvas):
    ## TODO: delete all of this function and create *your* creature!
    ## This is just a hard-coded example

    # face:
    make_circle(canvas, (250, 150), 100, fill_color='yellow')

    # left eye:
    make_oval(canvas, (225, 130), 10, 18, fill_color='black')

    # right eye:
    make_oval(canvas, (275, 130), 10, 18, fill_color='black')
