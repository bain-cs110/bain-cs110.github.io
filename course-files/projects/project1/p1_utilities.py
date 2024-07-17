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
        point_0, point_1, point_2, point_3, fill=color, tags=tag, outline=outline, **kwargs
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
    return rectangle(top_left=top_left, width=size, height=size, color=color, tag=tag, outline=outline, **kwargs)


def diamond(center=(0, 0), width=25, height=50, color="hotpink", outline="", tag="", **kwargs):
    """
    A reporter function that draws a rectangle.
    Args:
        center (`tuple`): A coordinate representing the center of the shape.
        width (`int`): How wide to draw the shape.
        height (`int`): How tall to draw the shape.
        color (`str`): What color to draw the shape.
        outline (`str`): What color should the border of the shape be.
        tag (`str`): The tag to assign to the shape.

    Returns:
         `Shape`: The shape that was created.
    """      
    point_0 = (center[0] - width / 2, center[1])
    point_1 = (center[0], center[1] - height / 2)
    point_2 = (center[0] + width / 2, center[1])
    point_3 = (center[0], center[1] + height / 2)
    return _a_canvas.create_polygon(
        point_0, point_1, point_2, point_3, fill=color, tags=tag, outline=outline, **kwargs
    )

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
        
    return _a_canvas.create_polygon(point_list, fill=color, tags=tag, outline=outline, **kwargs)


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
    return oval(center=center, radius_x=radius, radius_y=radius, color=color, tag=tag, outline=outline, **kwargs)


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

    return _a_canvas.create_polygon(point_0, point_1, point_2, fill=color, tags=tag, outline=outline, **kwargs)


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
    return polygon(vertices, color=color, tag=tag, outline=outline, **kwargs)

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
    return _a_canvas.create_polygon(points, fill=color, tags=tag, outline=outline, **kwargs)

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

    return arc(points=all_points, width=line_width, tag=tag, **kwargs)

def text(top_left=(0,0), text="", font=("Purisa", 32), color="black", tag="", **kwargs):
    """
    A reporter function that draws text to the screen
    Args:
        top_left (`tuple`): coordinate pair to specify the location.
        text (`str`): What text to draw.
        font (`tuple`): A tuple where the first element is a string for the font name and the second is an
           int with the font size.
        color (`str`): What color should the text be.
        tag (`str`): The name to tag this thing with.

    Returns:
        `Shape`: The text that was created.
    """
    return _a_canvas.create_text(top_left,
                                  text=text, 
                                  font=font,
                                  fill=color,
                                  tags=tag, **kwargs)

def move(tag, x=0, y=0):
    """
    Shift the given tagged item by the specified amounts.
    
    Args:
        tag (Shape or `str`): the shape (or shapes) to move
        x (`int`): amount to move in the x direction
        y (`int`): amount to move in the y direction
    """
    shape_ids = _a_canvas.find_withtag(tag)
    for id in shape_ids:
        _a_canvas.move(id,
                        x,
                        y)
        
def move_to(tag, to, anchor="center"):
    """
    Move the given tagged item to a particular `point` maintaining some `anchor`.
    Note: this is NOT the same as the `move` function which moves an object by a specific amount.
    
    Args:
        tag (Shape or `str`): the shape (or shapes) to move
        to (`tuple`): the `(x, y)` coordinate to which you wish to move the tagged object
        anchor (`str`): which point on the shape do you want to move toward the given tuple. You can
            use either `"center"` (default), `"top_left"`, `"top_right"`, `"bottom_left"`, or `"bottom_right"`.
    """
    anchor_options = ["center", "top_left", "top_right", "bottom_left", "bottom_right"]
    if anchor not in anchor_options:
        raise ValueError("The anchor input must be one of " + str(anchor_options) + " but instead we found " + str(anchor))

    outline = _get_outline(tag)
    delta_x = 0
    delta_y = 0
    
    if anchor == "top_left":
        delta_x = to[0] - outline['left']
        delta_y = to[1] - outline['top'] 
    elif anchor == "top_right":
        delta_x = to[0] - outline['right']
        delta_y = to[1] - outline['top']
    elif anchor == "bottom_right":
        delta_x = to[0] - outline['right']
        delta_y = to[1] - outline['bottom']
    elif anchor == "bottom_left":
        delta_x = to[0] - outline['left']
        delta_y = to[1] - outline['bottom']
    elif anchor == "center":
        delta_x = to[0] - outline['center'][0]
        delta_y = to[1] - outline['center'][1]
    
    _a_canvas.move(tag, delta_x, delta_y)


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
    
    
def _get_outline(shape):
    """
    A reporter function that takes in a shape and calls the various helper functions to generate
    a sort of "summary" of that particular shape and returns it in the form of a dictionary.

    Args:
        shape (Shape or Tag): what shape to look up
        
    Returns:
        a `Dictionary` with the various properties of the shape
    """
    
    return {
        "center": get_center(shape),
        "left": get_left(shape),
        "right": get_right(shape),
        "top": get_top(shape),
        "bottom": get_bottom(shape)
    }
    

def align(shape1, shape2, via="middle", offset_x = 0, offset_y = 0):
    """
    A reporter function that aligns `shape1` with `shape2`. It does this by moving `shape1` to align with
    whatever property of `shape2` is selected with the `via` input.
    
    Args:
        shape1 (`Shape` or Tag): The first shape to use.
        shape2 (`Shape` or Tag): The second shape to use.
        via (`str`): Has to be one of, the following options: `"center"` (horizontal center), 
            `"middle"` (vertical center), `"top"`, `"bottom"`, `"left"`, or `"right"`
        offset_x (`int`): How much to shift in the x-axis after alignment
        offset_y (`int`): How much to shift in the y-axis after alignment

    Returns:
        `Shape`: The modified shape1.
    """
    via_options = ["center", "middle", "top", "bottom", "left", "right"]
    if via not in via_options:
        raise ValueError("The via input must be one of " + str(via_options) + " but instead we found " + str(via))

    outline1 = _get_outline(shape1)
    outline2 = _get_outline(shape2)
    
    if via == "center":
        _a_canvas.move(
            shape1,
            (outline2['center'][0] - outline1['center'][0]) + offset_x, offset_y)
        
    elif via == "middle":
        _a_canvas.move(
            shape1,
            offset_x, (outline2['center'][1] - outline1['center'][1]) + offset_y)
        
    elif via == "top":
        _a_canvas.move(
            shape1,
            offset_x, (outline2['top'] - outline1['top']) + offset_y)
        
    elif via == "bottom":
        _a_canvas.move(
            shape1,
            offset_x, (outline2['bottom'] - outline1['bottom']) + offset_y)
        
    elif via == "left":
        _a_canvas.move(
            shape1,
            (outline2['left'] - outline1['left']) + offset_x, offset_y)
        
    elif via == "right":
        _a_canvas.move(
            shape1,
            (outline2['right'] - outline1['right']) + offset_x, offset_y)
        
    return shape1   


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
    A reporter function that generates a new color between two given colors. Can be used to make
    gradients!
    
    Args:
        color1 (`str`): The "start" color
        color2 (`str`): The "end" color
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

def get_colors(tag_or_tags):
    """
    A reporter function that returns all the colors associated with a tag or list of tags.

    Args:
        tag_or_tags (`str` or `List`): the tag or list of tags you'd like to find the colors of
        
    Returns:
        A `List` containing all **unique** colors associated with that tag(s)
    """
    all_shapes = []
    if not isinstance(tag_or_tags, list):
        tag_or_tags = [tag_or_tags]
    for tag in tag_or_tags:
        all_shapes += _a_canvas.find_withtag(tag)
        
    all_colors = []
    for shape in all_shapes:
        color = _a_canvas.itemcget(shape, 'fill')
        if color not in all_colors:
            all_colors.append(color) 

    return all_colors

def get_center(shape):
    """
    A reporter function calculates the center **coordinate** at the center of some shape.
    Note that this is different from the other get functions as it returns a `tuple` instead of an `int`.
        
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
    Returns `True` if a given tag exists on the screen otherwise returns `False`.

    Args:
        `tag` (`str`): The tag of the object to lookup.

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

def make_car(top_left=(0, 0), size=100, color="#3D9970", tag=""):
    '''
    Draws a cool car.

    Args:
        top_left (`tuple`): A coordinate at which to draw the car.
        fill_color (`str`): Color name or hex code to fill the object with.
        tag (`str`): The tag to assign to the shape.

    '''
    x, y = top_left
    rectangle((x + 5*size/10, y), size, size / 10 * 4, color=color, tag=tag)
    rectangle((x, y + size - 7*size/10), size, size / 10 * 4.5, color=color, tag=tag)
    circle((x + 5*size/10, y + size - size/5), size / 5, color='black', tag=tag)
    circle((x + 15*size/10, y + size - size/5), size / 5, color='black', tag=tag)

_cache = []

def make_image(image_path, position=(200, 200), rotation=None,
        scale=None, tag="", **kwargs):
    '''
    Draws a given image on the screen. NOTE: Requires the `pillow` package to be installed - contact 
    Prof. Bain or post on edSTEM if you'd like more details!

    Args:
        image_path (`str`): Location of the image file on your computer.
        position (`tuple`): A coordinate at which to render the image.
        rotation (`int`): A number of degrees to rotate the given image.
        scale (`int`): A scaling factor to multiply the image size by.
        tag (`str`): A string representing the "name" fo this shape.
    '''
    # import PIL libraries
    from PIL import Image, ImageTk
    anchor='nw'

    import os
    # 1. create PIL image and apply any image transformations:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(dir_path, image_path)
    pil_image = Image.open(image_path)
    if scale:
        size = (
            round(pil_image.size[0] * scale),
            round(pil_image.size[1] * scale)
        )
        pil_image = pil_image.resize(size)
    if rotation:
        pil_image = pil_image.rotate(rotation)  # note: returns a copy

    # 2. convert to tkinter-compatible image format:
    tkinter_image = ImageTk.PhotoImage(pil_image)
    _cache.append(tkinter_image)  # workaround for known tkinter bug: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm

    # 3. draw image on canvas:
    _a_canvas.create_image(*position, image=tkinter_image, anchor=anchor, tags=tag, **kwargs)

def get_tag_from_event(event, precision=25):
    '''
    Tries to return a tag of an object at a given mouse-event.

    Args:
        event (`Event`): Must be a mouse event otherwise we'll give back an error.
        precision (`int`): How precise in number of pixels does a user have to be to "select" an object
    '''
    try:
        x = event.x
        y = event.y
        shape_id = _a_canvas.find_closest(x, y) # get the top shape
        if shape_id and distance(get_center(shape_id), (x,y)) < precision:
            tags = _a_canvas.gettags(shape_id)
            if len(tags) > 0:
                return tags[0]
        return ""
    
    except:
        raise Exception("No tag found! Maybe you passed us an event that isn't a mouse event?")

def random_color():
    '''
    Returns a random color as a `string` to be used with `tkinter`.
    It does not accept any inputs.
    '''
    r = lambda: randint(0,255)
    return '#%02X%02X%02X' % (r(), r(), r())

def setup_listener(event, handler_function):
    '''
    Sets up a listener for a given event on our window.
    
    Args:
        event (`str`): The magic string that represents this event (determined by Python)
        handler_function (`func`): The name (not a string though) of the function you want called when the event his heard.
    '''
    _a_canvas.bind(event, handler_function)

from tkinter import Tk, Canvas

def setup_shapes(title, background="white", width=600, height=600, grid=False):
    """
    A static function that sets up the pop-up window. **DO NOT ADD CALLS TO THIS FUNCTION IN YOUR PROGRAM**. However,
    at the top of your program, you're more than welcome to edit the inputs given to the function.
    
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
    _a_canvas.focus_set()
    return _a_canvas
