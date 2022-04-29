from tkinter import Canvas

def make_circle(canvas:Canvas, center:tuple, radius:int, color:str='#FF4136', tag:str=None, stroke_width:int=1, outline:str=None):
    x, y = center
    canvas.create_oval(
        [ x - radius, y - radius, x + radius, y + radius ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )


w = None
r = "red"
b = "saddle brown"
t = "bisque3"
y = "bisque3"
g = "blue"


w, w, w, w, w, r, r, r, r, r, w, w, w, w, w, w
w, w, w, w, r, r, r, r, r, r, r, r, r, w, w, w
w, w, w, w, b, b, b, t, t, b, t, w, w, w, w, w
w, w, g, y, g, y, y, y, g, y, y, y, w, w, w, w
w, w, w, g, y, g, g, y, y, y, g, y, y, y, w, w
w, w, w, g, g, y, y, y, y, g, g, g, g, w, w, w
w, w, w, g, g, y, y, y, y, g, g, g, g, g, w, w
w, w, w, w, w, y, y, y, y, y, y, y, w, w, w, w
w, w, g, g, g, g, r, r, g, g, w, w, w, w, w, w
y, y, g, g, g, g, r, r, r, g, g, g, y, y, y, w
y, y, y, w, g, g, r, y, r, r, r, g, g, y, y, w
w, w, w, r, r, r, r, r, r, r, r, r, g, g, w, w
w, w, r, r, r, r, r, r, r, r, r, r, g, g, w, w,
w, g, g, r, r, r, w, w, w, r, r, r, g, g, w, w,
w, g, g, g, w, w, w, w, w, w, w, w, w, w, w, w,
w, w, g, g, g, w, w, w, w, w, w, w, w, w, w, w,


mario_1 = [
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 3, 3, 3, 4, 4, 4, 5, 4, 0, 0, 0, 0),
    (0, 3, 4, 3, 4, 4, 4, 4, 5, 4, 4, 4, 0, 0),
    (0, 3, 4, 3, 4, 4, 4, 4, 4, 5, 4, 4, 4, 0),
    (0, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 0),
    (0, 0, 1, 1, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0),
    (0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 0, 0, 0),
    (1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0),
    (4, 4, 1, 2, 6, 2, 2, 6, 2, 1, 4, 4, 0, 0),
    (4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0),
    (4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 0, 0),
    (0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0),
    (0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 0),
    (3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 0)
]
