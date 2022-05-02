from random import randint

def make_rectangle(canvas, top_left, width, height, fill_color="#3D9970", tag=None):
    x, y = top_left
    return canvas.create_rectangle(
        [(x, y), (x + width, y + height)],
        fill=fill_color,
        width=0,
        tags=tag
    )

def make_circle(canvas, center, radius, fill_color='white', tag=None, stroke_width=2, outline="white"):
    make_oval(
        canvas, center, radius, radius, color=fill_color, tag=tag,
        stroke_width=stroke_width, outline=outline
    )

def make_oval(canvas, center, radius_x, radius_y, color='#FF4136', tag=None, stroke_width=1, outline=None):
    x, y = center
    return canvas.create_oval(
        [ x - radius_x, y - radius_y, x + radius_x, y + radius_y ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )

############ More Advanced Shapes!

def make_car(canvas, top_left=(0, 0), color="#3D9970", tag=None):
    '''
    demo function that show you how to draw a car, given the convenience
    functions that are available in this module
    '''
    x, y = top_left
    make_rectangle(canvas, (x + 50, y), 100, 40, fill_color=color, tag=tag)
    make_rectangle(canvas, (x, y + 30), 200, 45, fill_color=color, tag=tag)
    make_circle(canvas, (x + 50, y + 80), 20, fill_color='black', tag=tag)
    make_circle(canvas, (x + 150, y + 80), 20, fill_color='black', tag=tag)


def make_cloud(canvas, center, tag=None):
    for i in range(randint(0,10)):
        x_offset = randint(-40,40)
        y_offset = randint(0,20)
        make_circle(canvas, (center[0] + x_offset, center[1] + y_offset), randint(10,50))

def make_star(canvas, center, diameter, tag=None):
    '''
    demo function that show you how to draw a star, given the convenience
    functions that are available in this module
    '''
    make_circle(
        canvas,
        center,
        diameter / 2,
        stroke_width=0,
        outline='white',
        color='white',
        tag=tag
    )

def make_bubble(canvas, center, diameter, tag=None):
    '''
    demo function that show you how to draw a bubble, given the convenience
    functions that are available in this module
    '''
    make_circle(
        canvas,
        center,
        diameter / 2,
        stroke_width=1,
        outline='white',
        color=None,
        tag=tag
    )
