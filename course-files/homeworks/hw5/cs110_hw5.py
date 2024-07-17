### IGNORE EVERYTHING THAT STARTS WITH A _
from random import randint
from math import sqrt, pi, radians, sin, cos

__docformat__ = "google"

_a_canvas = None

def rectangle(top_left=(0, 0), width=25, height=50, color="hotpink", outline="", tag="", **kwargs):
    """
    A reporter function that draws a rectangle.
    Args:
        top_left (`tuple`): A coordinate representing the top left-hand corner of the shape.
        width (`int`): How wide to draw the shape.
        height (`int`): How tall to draw the shape.
        color (`str`): What color to draw the shape.
        outline (`str`): What color should the border of the shape be.
        tag (`str`): The tag to assign to the shape.

    Returns:
         `Shape`: The rectangle that was created.
    """      
    point_0 = top_left
    point_1 = (top_left[0] + width, top_left[1])
    point_2 = (top_left[0] + width, top_left[1] + height)
    point_3 = (top_left[0], top_left[1] + height)
    return _a_canvas.create_polygon(
        point_0, point_1, point_2, point_3, fill=color, tags=tag, **kwargs
    )


def square(top_left=(0, 0), size=25, color="hotpink", outline="", tag="", **kwargs):
    """
    A reporter function that draws a square.
    Args:
        top_left (`tuple`): A coordinate representing the top left-hand corner of the shape.
        size (`int`): How big to draw the shape.
        color (`str`): What color to draw the shape.
        outline (`str`): What color should the border of the shape be.
        tag (`str`): The tag to assign to the shape.

    Returns:
         `Shape`: The square that was created.
    """
    return rectangle(top_left=top_left, width=size, height=size, color=color, tag=tag, **kwargs)

def cloud(center, color="white", tag=""):
    """
    Reporter function that draws a cloud to the screen.
    Args:
        enter (`tuple`): the point on which to center the cloud
        color (`str`): which determines the color of the cloud
        tag (`str`): to give the cloud a name

    Returns:
        `Shape`: The cloud that was created.   
    """
    for i in range(10):
        x_offset = randint(-40, 40)
        y_offset = randint(0, 20)
        circle(center=(center[0] + x_offset, center[1] + y_offset), 
               radius=randint(10, 50),
               color=color,
               tag=tag)
    return tag

def oval(center=(0, 0), radius_x=25, radius_y=50, color="hotpink", outline="", tag="", **kwargs):
    """
    A reporter function that draws an oval.
    Args:
        center (`tuple`): A coordinate representing the center of the shape.
        radius_x (`int`): Specifies the oval's radius on the x-axis.
        radius_y (`int`): Specifies the oval's radius on the y-axis.
        color (`str`): What color to draw the shape.
        outline (`str`): What color should the border of the shape be.
        tag (`str`): The tag to assign to the shape.

    Returns:
         `Shape`: The oval that was created.
    """
    x = center[0]
    y = center[1]
    x0, y0, x1, y1 = (x - radius_x, y - radius_y, x + radius_x, y + radius_y)
    steps = 100
    # major and minor axes
    a = (x1 - x0) / 2.0
    b = (y1 - y0) / 2.0
    # center
    xc = x0 + a
    yc = y0 + b
    point_list = []
    # create the oval as a list of points
    for i in range(steps):
        # Calculate the angle for this step
        theta = (pi * 2) * (float(i) / steps)
        x = a * cos(theta)
        y = b * sin(theta)
        point_list.append(round(x + xc))
        point_list.append(round(y + yc))

    return _a_canvas.create_polygon(point_list, fill=color, tags=tag, **kwargs)


def circle(center=(0, 0), radius=25, color="hotpink", outline="", tag="", **kwargs):
    """
    A reporter function that draws a circle.
    Args:
        center (`tuple`): A coordinate representing the center of the shape.
        radius (`int`): Specifies the circle's radius.
        color (`str`): What color to draw the shape.
        outline (`str`): What color should the border of the shape be.
        tag (`str`): The tag to assign to the shape.

    Returns:
         `Shape`: The circle that was created.
    """
    return oval(center=center, radius_x=radius, radius_y=radius, color=color, tag=tag, **kwargs)


def triangle(
    bottom_center=(0, 0), width=25, top_shift=0, height=0, color="hotpink", outline="", tag="", **kwargs
):
    """
    A reporter function that draws a triangle.
    Args:
        bottom_center (`tuple`): A coordinate representing the bottom center of the shape.
        width (`int`): Specifies the width of the base of the triangle.
        top_shift (`int`): Specifies the how far to the left or right to shift the top of 
            the triangle from the bottom center.
        height (`int`): Specifies the triangle's height.
        color (`str`): What color to draw the shape.
        outline (`str`): What color should the border of the shape be.
        tag (`str`): The tag to assign to the shape.

    Returns:
         `Shape`: The triangle that was created.
    """
    if height == 0:
        height = width * sqrt(3) / 2
    point_0 = (bottom_center[0] - width / 2, bottom_center[1])
    point_1 = (bottom_center[0] + width / 2, bottom_center[1])
    point_2 = (bottom_center[0] + top_shift, bottom_center[1] - height)

    return _a_canvas.create_polygon(point_0, point_1, point_2, fill=color, tags=tag, **kwargs)


def line(points=[], curvy=False, color="hotpink", tag="", **kwargs):
    """
    A reporter function that draws a line given a list of points.
    Args:
        points (`list`): The points that define the line; this should be a list of tuples (coordinates).
        curvy (`bool`): Makes a curvy line instead.
        color (`str`): What color to make the shape.
        tag (`str`): The tag to assign to the shape.

    Returns:
        `Shape`: The line that was created.
    """
    return _a_canvas.create_line(points, fill=color, smooth=curvy, tags=tag, **kwargs)


def arc(points=[], width=5, color="hotpink", line_steps=15, tag="", **kwargs):
    """
    A reporter function that draws an arc ("curve") given a list of points.
    Args:
        points (`list`): The points outlining the curve; this should be a list of tuples (coordinates).
            Make sure to give it at least 3 (x,y) coordinates that aren't a straight line!
        color (`str`): What color to make the shape.
        tag (`str`): The tag to assign to the shape.

    Returns:
        `Shape`: The arc that was created.
    """
    return _a_canvas.create_line(
        points,  
        width=width,
        fill=color,
        splinesteps=line_steps,
        smooth=True,
        tags=tag,
        **kwargs
    )


def star(center=(0, 0), radius=50, color="hotpink", outer_radius=75, points=5, outline="", tag="", **kwargs):
    """
    A reporter function that draws a star.
    Args:
        center (`tuple`): A coordinate representing the center of the shape.
        radius (`int`): Specifies the radius of the inside part of the star.
        color (`str`): Specifies the color of the star.
        outer_radius (`int`): Specifies the radius of the outside part of the star.
        points (`int`): Specifies the number of points for the star.
        outline (`str`): What color should the border of the shape be.
        tag (`str`): The tag to assign to the shape.

    Returns:
         `Shape`: The star that was created.
    """
    arc_segment = 360 / points
    vertices = []
    for i in range(points):
        inner_point = (
            radius * cos(radians(arc_segment * i)) + center[0],
            -1 * radius * sin(radians(arc_segment * i)) + center[1],
        )
        vertices.append(inner_point)
        outer_point = (
            outer_radius * cos(radians(arc_segment * i + arc_segment / 2)) + center[0],
            -1 * outer_radius * sin(radians(arc_segment * i + arc_segment / 2))
            + center[1],
        )
        vertices.append(outer_point)
    return polygon(vertices, color=color, tag=tag, **kwargs)

def polygon(points=[], color="hotpink", outline="", tag="", **kwargs):
    """
    A reporter function that draws a polygon given a list of points.
    Args:
        points (`list`): The points outlining the polygon; this should be a list of tuples (coordinates).
            defaults to an empty list.
        outline (`str`): What color should the border of the shape be.
        color (`str`): What color to make the shape.
        tag (`str`): The tag to assign to the shape.

    Returns:
        `Shape`: The polygon that was created.
   """
    return _a_canvas.create_polygon(points, fill=color, tags=tag, **kwargs)

def _polar_to_cartesian(r, theta):
    return int(r*cos(theta)), int(r*sin(theta))

def spiral(center=(0, 0), width=100, roughness=0.01, start=0, spirals=5, line_width=1, tag="", **kwargs):
    """
    A reporter function that draws a spiral.
    Args:
        center (`tuple`): A coordinate representing the center of the shape.
        width (`int`): Specifies the total width of the spiral.
        roughness (`float`): Controls how spiral-y the shape is (lower is less spiral-y)
        start (`int`): Where on the spiral to start drawing.
        spirals (`int`): How many loops to draw.
        line_width (`int`): How wide for the line to be drawn.
        tag (`str`): The tag to assign to the shape.

    Returns:
         `Shape`: The spiral that was created.
    """
    theta = 0.0
    r = start
    all_points = []
    prev_pos = _polar_to_cartesian(r, theta)
    distance = width / 4 / pi / spirals 
    all_points.append((prev_pos[0] + center[0], prev_pos[1] + center[1]))
    while theta < 2 * spirals * pi:
        theta += roughness
        r = start + distance*theta
        pos = _polar_to_cartesian(r, theta)
        all_points.append((pos[0] + center[0], pos[1] + center[1]))

    return arc(points=all_points, width=line_width, **kwargs)

def move(tag, x=0, y=0):
    """
    Purpose: Move the x and y position of all shapes that have been tagged
    with the tag argument
    Args:
        tag (`str`): the shape (or shapes) to move
        x (`int`; optional): amount to move in the x direction
        y (`int`; optional): amount to move in the y direction
    """
    shape_ids = _a_canvas.find_withtag(tag)
    for id in shape_ids:
        _a_canvas.move(id,
                        x,
                        y)

def put_in_front(tag):
    """
    A function that "raises" a shape to the "top" of the screen."

    Args:
        tag (`str`): The tag to raise.
    """
    _a_canvas.tag_raise(tag)

def put_in_back(tag):
    """
    A function that "lowers" a shape to the "bottom" of the screen."

    Args:
        tag (`str`): The tag to raise.
    """
    _a_canvas.tag_lower(tag)

def overlay(shape1, shape2, offset_x=0, offset_y=0):
    """
    A reporter function that overlays shape1 onto shape2. It does this by moving shape 1's center
    to shape 2's center, and then applying any specified offset.
    Args:
        shape1 (`Shape` or Tag): The first shape to use.
        shape2 (`Shape` or Tag): The second shape to use.
        offset_x (`int`): How much to shift shape 2 in the x-direction after centering it.
        offset_y (`int`): How much to shift shape 2 in the x-direction after centering it.
        tag (`str`): The tag to assign to the shape.

    Returns:
        `Shape`: The modified shape1.
   """
    center1 = get_center(shape1)
    center2 = get_center(shape2)
    _a_canvas.move(
        shape1,
        (center2[0] - center1[0]) + offset_x,
        (center2[1] - center1[1]) + offset_y,
    )
    _a_canvas.tag_raise(shape1, shape2)
    return shape1


def underlay(shape1, shape2, offset_x=0, offset_y=0):
    """
    A reporter function that underlays shape1 beneath shape2. It does this by moving shape 1's center
    to shape 2's center, and then applying any specified offset.
    Args:
        shape1 (`Shape` or Tag): The first shape to use.
        shape2 (`Shape` or Tag): The second shape to use.
        offset_x (`int`): How much to shift shape 2 in the x-direction after centering it.
        offset_y (`int`): How much to shift shape 2 in the x-direction after centering it.

    Returns:
        `Shape`: The modified shape1.
   """
    center1 = get_center(shape1)
    center2 = get_center(shape2)
    _a_canvas.move(
        shape1,
        (center2[0] - center1[0]) + offset_x,
        (center2[1] - center1[1]) + offset_y,
    )
    _a_canvas.tag_lower(shape1, shape2)
    return shape1


def above(shape1, shape2, offset_x=0, offset_y=0):
    """
    A reporter function that places shape1 above shape2 (vertically). It does this by moving shape 1's center
    to shape 2's center, moving shape 1 in the y-direction the exact height of shape 2, and then applying any
    specified offset.

    Args:
        shape1 (`Shape` or Tag): The first shape to use.
        shape2 (`Shape` or Tag): The second shape to use.
        offset_x (`int`): How much to shift shape 2 in the x-direction after moving it.
        offset_y (`int`): How much to shift shape 2 in the x-direction after moving it.

    Returns:
        `Shape`: The modified shape1.  
    """
    overlay(shape1, shape2)
    _a_canvas.move(
        shape1,
        0 + offset_x,
        -1 * (get_height(shape2) + get_height(shape1)) / 2 + offset_y,
    )
    return shape1


def beside(shape1, shape2, offset_x=0, offset_y=0):
    """
    A reporter function that places shape1 beside shape2 (horizontally). It does this by moving shape 1's center
    to shape 2's center, moving shape 1 in the x-direction the exact width of shape 2, and then applying any
    specified offset.

    Args:
        shape1 (`Shape` or Tag): The first shape to use.
        shape2 (`Shape` or Tag): The second shape to use.
        offset_x (`int`): How much to shift shape 2 in the x-direction after moving it.
        offset_y (`int`): How much to shift shape 2 in the x-direction after moving it.

    Returns:
        `Shape`: The modified shape1.  
    """
    overlay(shape1, shape2)
    _a_canvas.move(
        shape1,
        (get_width(shape2) + get_width(shape1)) / 2 + offset_x,
        0 + offset_y,
    )
    return shape1


def below(shape1, shape2, offset_x=0, offset_y=0):
    """
    A reporter function that places shape1 below shape2 (vertically). It does this by moving shape 1's center
    to shape 2's center, moving shape 1 in the y-direction the exact height of shape 2, and then applying any
    specified offset.

    Args:
        shape1 (`Shape` or Tag): The first shape to use.
        shape2 (`Shape` or Tag): The second shape to use.
        offset_x (`int`): How much to shift shape 2 in the x-direction after moving it.
        offset_y (`int`): How much to shift shape 2 in the x-direction after moving it.

    Returns:
        `Shape`: The modified shape1.  
    """
    overlay(shape1, shape2)
    _a_canvas.move(
        shape1,
        0 + offset_x,
        (get_height(shape2) + get_height(shape1)) / 2 + offset_y,
    )
    return shape1

def delete(shape):
    """
    A function that deletes a shape from our screen.

    Args:
        shape (`Shape` or Tag): The shape to delete.
    """
    _a_canvas.delete(shape)

def duplicate(shape, color=None):
    """
    A reporter function that perfectly copies a shape and returns that copy.

    Args:
        shape (`Shape` or Tag): The shape to duplicate.
        color (`str`): A new color to use with the duplicated shape.

    Returns:
        `Shape`: The new duplicated shape.  
    """
    shape_type = _a_canvas.type(shape)
    shape_config = _a_canvas.itemconfig(shape)
    shape_coords = _a_canvas.coords(shape)
    the_copy = None
    if shape_type == "polygon":
        new_config = {key: shape_config[key][-1] for key in shape_config.keys()}
        if color != None:
            new_config["fill"] = color
        the_copy = _a_canvas.create_polygon(shape_coords, **new_config)
        return the_copy

def mirror(shape):
    """
    A reporter function that takes a shape and flips it across its vertical
    axis, returning the tag or ID of the modified shape.
        
    Args:
        shape (`Shape` or Tag): The shape in question.

    Returns:
        The modified shape.
    """
    center = get_center(shape)[0]
    shape_ids = _a_canvas.find_withtag(shape)
    for shape_id in shape_ids:
        flipped_coordinates = []
        shape_coords = _a_canvas.coords(shape_id)
        counter = 0
        for num in shape_coords:
            if counter % 2 == 0:
                if num < center:
                    flipped_coordinates.append(num + 2 * (center - num))
                elif num > center:
                    flipped_coordinates.append(num - 2 * (num - center))
                else:
                    flipped_coordinates.append(num)
            else:
                flipped_coordinates.append(num)
            counter += 1
        _a_canvas.coords(shape_id, flipped_coordinates)

def rotate(shape, degrees=5, origin=None):
    """
    A reporter function that takes a shape and rotates it by a specified amount around a specified point.
    It does this by interpolating a polygon around the shape and calculating the shifts of individual
    points on the edge of the polygon.

    Args:
        shape (`Shape` or Tag): The shape to rotate.
        degrees (`int`): The number of degrees to rotate the shape.
        origin (`tuple`): An `(x,y)` coordinate about which to perform the rotation. Defaults to the center
            of the given shape.

    Returns:
        `Shape`: The modified shape.  
    """
    if origin is None:
        origin = get_center(shape)

    theta = radians(degrees)
    ox, oy = origin

    all_shapes = _a_canvas.find_withtag(shape)

    for a_shape in all_shapes:
        coords = _a_canvas.coords(a_shape)
        # update coordinates:
        for i in range(0, len(coords), 2):
            px, py = coords[i], coords[i + 1]
            qx = cos(theta) * (px - ox) - sin(theta) * (py - oy) + ox
            qy = sin(theta) * (px - ox) + cos(theta) * (py - oy) + oy
            coords[i] = qx
            coords[i + 1] = qy
        # set the coordinates:
        _a_canvas.coords(a_shape, coords)

    return shape 

def distance(point1, point2):
    """
    A reporter function calculates the distance between two `(x, y)` coordinates.
          
    Args:
        point1 (`tuple`): The first `(x, y)` coordinate.
        point2 (`tuple`): The second `(x, y)` coordinate.

    Returns:
         A `float` representing the distance between the two points.
    """
    return sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))

def update_color(tag, color):
    '''
    Change the fill color of a tagged object.

    Args:
        tag (`str`): The tag of the object to re-fill.
        color (`str`): A color name or hex code to re-fill with.
    '''
    ids = _a_canvas.find_withtag(tag)
    for id in ids:
        _a_canvas.itemconfig(id, fill=color)

def interpolate_colors(color1, color2, frac):
    """
    A reporter function that generates a new color between two given colors.
    Args:
        color1 (`str`): The path of the file to wrap
        color2 (`str`): The path of the file to wrap
        frac (`float`): What fraction of each color to take. An input of 0 returns
            color1, an input of 1 returns color2, an input of 0.5 returns a color
            perfectly between the two.

    Returns:
         A color (as a hex `str`) to be used elsewhere
   """
    if "#" not in color1:
        color1 = tuple((c // 256 for c in _a_canvas.winfo_rgb(color1)))
    else:
        color1 = _tupelize_color(color1)
    if "#" not in color2:
        color2 = tuple((c // 256 for c in _a_canvas.winfo_rgb(color2)))
    else:
        color2 = _tupelize_color(color2)
    return _interpolate_tuple(color1, color2, frac)

def get_center(shape):
    """
    A reporter function calculates the a coordinate at the center of some shape.
        
    Args:
        shape (`Shape` or Tag): The shape in question.

    Returns:
         A `tuple` representing center of the given shape.
    """
    bbox = _safe_bbox(shape)

    if bbox is None:
        raise Exception(f"We couldn't find the shape with id/tag {shape}. Make sure it exists!")

    return (((bbox[2] + bbox[0]) / 2), ((bbox[1] + bbox[3]) / 2))


def get_top(shape):
    """
    A reporter function calculates the **minimum** y-value of a given shape (since the y-axis is flipped).

    Args:
        shape (`Shape` or Tag): The shape in question.

    Returns:
         A `int` representing the minimum y-coordinate of the shape.
    """
    bbox = _safe_bbox(shape)
    return bbox[1]


def get_bottom(shape):
    """
    A reporter function calculates the **maximum** y-value of a given shape (since the y-axis is flipped).
    
    Args:
        shape (`Shape` or Tag): The shape in question.

    Returns:
         A `int` representing the maximum y-coordinate of the shape.
    """
    bbox = _safe_bbox(shape)
    return bbox[3]


def get_left(shape):
    """
    A reporter function calculates the **minimum** x-value of a given shape.
        
    Args:
        shape (`Shape` or Tag): The shape in question.

    Returns:
         A `int` representing the minimum x-coordinate of the shape.
    """
    bbox = _safe_bbox(shape)
    return bbox[0]


def get_right(shape):
    """
    A reporter function calculates the **maximum** x-value of a given shape.
        
    Args:
        shape (`Shape` or Tag): The shape in question.

    Returns:
         A `int` representing the maximum x-coordinate of the shape.
    """ 
    bbox = _safe_bbox(shape)
    return bbox[2]


def get_height(shape):
    """
    A reporter function calculates the height of some given shape.
        
    Args:
        shape (`Shape` or Tag): The shape in question.

    Returns:
         A `int` representing the height of the shape.
    """
    bbox = _safe_bbox(shape)
    return bbox[3] - bbox[1] - 1


def get_width(shape):
    """
    A reporter function calculates the width of some given shape.
        
    Args:
        shape (`Shape` or Tag): The shape in question.

    Returns:
         An `int` representing width of the shape.
    """
    bbox = _safe_bbox(shape)
    return bbox[2] - bbox[0] - 1

def make_grid(c, w, h):
    """
    Draws a grid on a screen with intervals of 100.

    Args:
        w (`int`): The width of the grid to draw
        h (`int`): The height of the grid to draw
    """
    interval = 100
    # Creates all vertical lines at intervals of 100
    for i in range(0, w, interval):
        _a_canvas.create_line(i, 0, i, h, tag="grid_line")
    # Creates all horizontal lines at intervals of 100
    for i in range(0, h, interval):
        _a_canvas.create_line(0, i, w, i, tag="grid_line")
    # Creates axis labels
    offset = 2
    for y in range(0, h, interval):
        for x in range(0, w, interval):
            _a_canvas.create_oval(
                x - offset, y - offset, x + offset, y + offset, fill="black"
            )
            _a_canvas.create_text(
                x + offset,
                y + offset,
                text="({0}, {1})".format(x, y),
                anchor="nw",
                font=("Purisa", 8),
            )

def _safe_bbox(shape):
    try:
        bbox = _a_canvas.bbox(shape)
        if bbox is None:
            Exception(f"We couldn't find the shape with tag/id: {shape}. Make sure this shape exists!") 
        return bbox
    except:
        raise Exception(f"We couldn't find the shape with tag/id: {shape}. Make sure this shape exists!") 

def _tupelize_color(color):
    R = int(color[1:3], 16)
    G = int(color[3:5], 16)
    B = int(color[5:7], 16)
    return R, G, B


def _interpolate_tuple(startcolor, goalcolor, frac):
    R = startcolor[0]
    G = startcolor[1]
    B = startcolor[2]

    targetR = goalcolor[0]
    targetG = goalcolor[1]
    targetB = goalcolor[2]

    DiffR = targetR - R
    DiffG = targetG - G
    DiffB = targetB - B

    iR = int(R + (DiffR * frac))
    iG = int(G + (DiffG * frac))
    iB = int(B + (DiffB * frac))

    hR = hex(iR).replace("0x", "")
    hG = hex(iG).replace("0x", "")
    hB = hex(iB).replace("0x", "")

    if len(hR) == 1:
        hR = "0" + hR
    if len(hB) == 1:
        hB = "0" + hB
    if len(hG) == 1:
        hG = "0" + hG

    color = ("#" + hR + hG + hB).upper()

    return color

def does_tag_exist(tag):
    '''
    Returns `True` if a given tag exists otherwise returns `False`.

    Args:
        `tag` (`str`): [Required] The tag of the object to lookup.

    '''
    result = _a_canvas.find_withtag(tag)

    if result:
        return True
    else:
        return False

def random_color():
    '''
    Returns a random color as a `string` to be used with `tkinter`.
    It does not accept any inputs.
    '''
    r = lambda: randint(0,255)
    return '#%02X%02X%02X' % (r(), r(), r())

from tkinter import Tk, Canvas

def setup_shapes(title, background="white", width=600, height=600, grid=False):
    """
    A static function that sets up the pop-up window. **DO NOT ADD CALLS TO THIS FUNCTION**.
    
    Args:
        `title` (`str`): The title of the window to create.
        `background` (`str`): Color to set the background.
        `width` (`int`): How wide to make the pop-up window.
        `height` (`int`): How tall to make the pop-up window.
        `grid` (`bool`): Whether or not to draw the axes / grid.
        
    """
    global _a_canvas
    gui = Tk()
    gui.title(title)
    _a_canvas = Canvas(gui, background=background, width=width, height=height)
    _a_canvas.pack()
    if grid:
        make_grid(_a_canvas, width, height)
    return _a_canvas