## DON'T OPEN THIS FILE! USE THE PURPLE BUTTON ON THE ASSIGNMENT
##   to see what functions are available and what their inputs are!

###################################################################

## PROCEED AT YOUR OWN RISK! THERE BE DRAGONS!

_VERSION = "2025.1.1"

## 2025.1.1
# Feature: adds ability to fill the screen with the window
# Feature: grid - add show_label param

###################################################################
### IGNORE EVERYTHING THAT STARTS WITH A _
from random import randint
from math import sqrt, pi, radians, sin, cos, floor
from time import sleep
from tkinter import Tk, Canvas


__docformat__ = "google"

_a_canvas = None
_resize_enabled = False


Shape_Drawing_Functions = ""


def arc(points=[], width=5, color="hot pink", line_steps=15, tag="", **kwargs):
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
        **kwargs,
    )


def car(top_left=(0, 0), size=100, body_color="#3D9970", wheel_color="black", tag=""):
    """
    Draws a cool car.

    Args:
        top_left (`tuple`): A coordinate at which to draw the car.
        body_color (`str`): Color to make the body of the car.
        wheel_color (`str`): Color to make the wheel of the car.
        tag (`str`): The tag to assign to the shape.
    """
    x, y = top_left
    rectangle((x + 5 * size / 10, y), size, size / 10 * 4, color=body_color, tag=tag)
    rectangle(
        (x, y + size - 7 * size / 10),
        size * 2,
        size / 10 * 4.5,
        color=body_color,
        tag=tag,
    )
    circle(
        (x + 5 * size / 10, y + size - size / 5), size / 5, color=wheel_color, tag=tag
    )
    circle(
        (x + 15 * size / 10, y + size - size / 5), size / 5, color=wheel_color, tag=tag
    )


def circle(center=(0, 0), radius=25, color="hot pink", outline="", tag="", **kwargs):
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
    return oval(
        center=center, radius_x=radius, radius_y=radius, color=color, tag=tag, **kwargs
    )


def cloud(center=(0, 0), size=30, color="white", tag=""):
    """
    Reporter function that draws a cloud to the screen.
    Args:
        center (`tuple`): the point on which to center the cloud
        size (`int`): how big (roughly) the cloud is drawn
        color (`str`): which determines the color of the cloud
        tag (`str`): to give the cloud a name

    Returns:
        `Shape`: The cloud that was created.
    """
    for i in range(10):
        x_offset = randint(int(-1 * size * 1.333), int(size * 1.333))
        y_offset = randint(0, int(size * 0.667))
        circle(
            center=(center[0] + x_offset, center[1] + y_offset),
            radius=randint(int(size * 0.667), int(size * 1.667)),
            color=color,
            tag=tag,
        )
    return tag


def diamond(
    center=(0, 0), width=25, height=50, color="hot pink", outline="", tag="", **kwargs
):
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
        point_0,
        point_1,
        point_2,
        point_3,
        fill=_safe_color(color),
        tags=tag,
        outline=outline,
        **kwargs,
    )


def grid(width=None, height=None, interval=100, show_labels=True):
    """
    Draws a grid on a screen with intervals of 100.

    Args:
        width (`int`): The width of the grid to draw (defaults to the whole window)
        height (`int`): The height of the grid to draw (defaults to the whole window)
        interval (`int`): The interval to draw the grid on.
        show_labels (`bool`): Whether or not to show coordinate labels.

    """

    if width is None:
        width = get_window_width()

    if height is None:
        height = get_window_height()

    # Creates all vertical lines at intervals of 100
    for i in range(0, width, interval):
        _a_canvas.create_line(i, 0, i, height, tag="grid", fill="black")
    # Creates all horizontal lines at intervals of 100
    for i in range(0, height, interval):
        _a_canvas.create_line(0, i, width, i, tag="grid", fill="black")

    if show_labels:
        # Creates axis labels
        offset = 2
        for y in range(0, height, interval):
            for x in range(0, width, interval):
                _a_canvas.create_oval(
                    x - offset,
                    y - offset,
                    x + offset,
                    y + offset,
                    fill="black",
                    tag="grid",
                )
                _a_canvas.create_text(
                    x + offset,
                    y + offset,
                    text="({0}, {1})".format(x, y),
                    anchor="nw",
                    font=("Purisa", 8),
                    fill="black",
                    tag="grid",
                )


_cache = []


def image(image_path, position=(200, 200), rotation=None, scale=None, tag="", **kwargs):
    """
    Draws a given image on the screen. NOTE: Requires the `pillow` package to be installed - contact
    Prof. Bain or post on edSTEM if you'd like more details!

    Args:
        image_path (`str`): Location of the image file on your computer.
        position (`tuple`): A coordinate at which to render the image.
        rotation (`int`): A number of degrees to rotate the given image.
        scale (`int`): A scaling factor to multiply the image size by.
        tag (`str`): A string representing the "name" fo this shape.
    """
    # import PIL libraries
    from PIL import Image, ImageTk

    anchor = "nw"

    import os

    # 1. create PIL image and apply any image transformations:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(dir_path, image_path)
    pil_image = Image.open(image_path)
    if scale:
        size = (round(pil_image.size[0] * scale), round(pil_image.size[1] * scale))
        pil_image = pil_image.resize(size)
    if rotation:
        pil_image = pil_image.rotate(rotation)  # note: returns a copy

    # 2. convert to tkinter-compatible image format:
    tkinter_image = ImageTk.PhotoImage(pil_image)
    _cache.append(
        tkinter_image
    )  # workaround for known tkinter bug: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm

    # 3. draw image on canvas:
    _a_canvas.create_image(
        *position, image=tkinter_image, anchor=anchor, tags=tag, **kwargs
    )


def line(points=[], curvy=False, color="hot pink", tag="", **kwargs):
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


def oval(
    center=(0, 0),
    radius_x=25,
    radius_y=50,
    color="hot pink",
    outline="",
    tag="",
    **kwargs,
):
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

    return _a_canvas.create_polygon(
        point_list, fill=_safe_color(color), tags=tag, **kwargs
    )


def pixel_art(top_left, artwork, palette, pixel=10, tag=""):
    """
    Draws a pixel art design!

    Args:
        top_left (`tuple`): the top left coordinate of the pixel art
        artwork (sequence of sequences): the art to draw
        palette (sequence): the palette of colors to use for each different square
        pixel (`int`, optional): how big each individual pixel should be
        tag (`str`, optional): the tag to assign to every square in the row

    Note: this doesn't return anything so make sure to use a tag if you want to animate / modify.
    """
    x = top_left[0]
    y = top_left[1]
    for row in artwork:
        # draw each row at the specified (x, y) position:
        _draw_row(row, (x, y), colors=palette, pixel=pixel, tag=tag)
        # ...and don't forget to shift the y-value down by the proper
        #  amount so that the next row won't draw on top of the first one:
        y += pixel


def polygon(points=[], color="hot pink", outline="", tag="", **kwargs):
    """
    A reporter function that draws a polygon given a list of points.
    Args:
        points (`list`): The points outlining the polygon; this should be a list of tuples (coordinates).
            defaults to an empty list.
        outline (`str`): What color should the border of the shape be.
        color (`str`): What color to make the shape.

    Returns:
        `Shape`: The polygon that was created.
    """
    return _a_canvas.create_polygon(points, fill=_safe_color(color), tags=tag, **kwargs)


def rectangle(
    top_left=(0, 0), width=25, height=50, color="hot pink", outline="", tag="", **kwargs
):
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
        point_0, point_1, point_2, point_3, fill=_safe_color(color), tags=tag, **kwargs
    )


def spiral(
    center=(0, 0), width=100, roughness=0.01, start=0, spirals=5, line_width=1, **kwargs
):
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
        r = start + distance * theta
        pos = _polar_to_cartesian(r, theta)
        all_points.append((pos[0] + center[0], pos[1] + center[1]))

    return arc(points=all_points, width=line_width, **kwargs)


def square(top_left=(0, 0), size=25, color="hot pink", outline="", tag="", **kwargs):
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
    return rectangle(
        top_left=top_left, width=size, height=size, color=color, tag=tag, **kwargs
    )


def star(
    center=(0, 0),
    radius=50,
    color="hot pink",
    outer_radius=75,
    points=5,
    outline="",
    tag="",
    **kwargs,
):
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


def text(
    top_left=(0, 0), text="", font=("Purisa", 32), color="black", tag="", **kwargs
):
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
    return _a_canvas.create_text(
        top_left, text=text, font=font, fill=color, tags=tag, **kwargs
    )


def triangle(
    bottom_center=(0, 0),
    width=25,
    top_shift=0,
    height=0,
    color="hot pink",
    outline="",
    tag="",
    **kwargs,
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

    return _a_canvas.create_polygon(
        point_0, point_1, point_2, fill=_safe_color(color), tags=tag, **kwargs
    )


def wedge(
    center=(0, 0), radius=25, angle=180, color="hot pink", outline="", tag="", **kwargs
):
    """
    A reporter function that draws a circle.
    Args:
        center (`tuple`): A coordinate representing the center of the shape.
        radius (`int`): Specifies the circle's radius.
        angle (`int`): A number between 0 and 360 that specifies how much of the circle to draw.
        color (`str`): What color to draw the shape.
        outline (`str`): What color should the border of the shape be.
        tag (`str`): The tag to assign to the shape.

    Returns:
        `Shape`: The wedge that was created.
    """
    point_list = [center[0], center[1]]
    for i in range(0, 0 + angle):
        x1 = center[0] + radius * cos(radians(i))
        point_list.append(x1)
        y1 = center[1] + radius * sin(radians(i))
        point_list.append(y1)

    point_list.append(center[0])
    point_list.append(center[1])

    return _a_canvas.create_polygon(
        point_list, fill=_safe_color(color), outline=outline, tags=tag, **kwargs
    )


Shape_Modifier_Functions = ""


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


def align(shape1, shape2, via="middle", offset_x=0, offset_y=0):
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
        raise ValueError(
            "The via input must be one of "
            + str(via_options)
            + " but instead we found "
            + str(via)
        )

    outline1 = _get_outline(shape1)
    outline2 = _get_outline(shape2)

    if via == "center":
        _a_canvas.move(
            shape1, (outline2["center"][0] - outline1["center"][0]) + offset_x, offset_y
        )

    elif via == "middle":
        _a_canvas.move(
            shape1, offset_x, (outline2["center"][1] - outline1["center"][1]) + offset_y
        )

    elif via == "top":
        _a_canvas.move(shape1, offset_x, (outline2["top"] - outline1["top"]) + offset_y)

    elif via == "bottom":
        _a_canvas.move(
            shape1, offset_x, (outline2["bottom"] - outline1["bottom"]) + offset_y
        )

    elif via == "left":
        _a_canvas.move(
            shape1, (outline2["left"] - outline1["left"]) + offset_x, offset_y
        )

    elif via == "right":
        _a_canvas.move(
            shape1, (outline2["right"] - outline1["right"]) + offset_x, offset_y
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


def change_color(shape, color):
    """
    Change the fill color of a tagged object.

    Args:
        shape (`Shape` or Tag): The shape or tag to re-fill.
        color (`str`): A color name or hex code to re-fill with.
    """
    ids = _a_canvas.find_withtag(shape)
    for id in ids:
        _a_canvas.itemconfig(id, fill=color)


def delete(shape):
    """
    A function that deletes a shape from our screen.

    Args:
        shape (`Shape` or Tag): The shape to delete.
    """
    _a_canvas.delete(shape)


def assign_tag(shape, tag):
    """
    A function that assigns a `Shape` or other tagged object a new tag. This will
    overwrite any existing tag that matches the provided `tag` argument. This means that if you have
    a shape with multiple tags, _this function will only overwrite that one tag_. You would need to run
    the function multiple times to rewrite the remaining tags.

    Args:
        shape (`Shape` or Tag): The shape to which you'd like to assign a new tag
        tag (`str`): A new valid tag for this shape.

    """
    ids = _a_canvas.find_withtag(shape)
    for id in ids:
        the_tags = list(_a_canvas.gettags(id))        
        if shape in the_tags: # if it has a tag replace it
            index = the_tags.index(shape)
            the_tags[index] = tag
        else: # otherwise it didn't have a tag
            the_tags.append(tag)
        _a_canvas.itemconfig(id, tags=the_tags)
            

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
    A function that takes a shape and flips it across its vertical
    axis, returning the modified shape.

    Args:
        shape (`Shape` or Tag): The shape in question.

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


def move(shape, x_shift=0, y_shift=0):
    """
    Purpose: Move the x and y position of all shapes that have been tagged
    with the tag argument

    Args:
        shape (`Shape` or Tag): The shape in question.
        x_shift (`int`; optional): amount to move in the x direction
        y_shift (`int`; optional): amount to move in the y direction
    """
    shape_ids = _a_canvas.find_withtag(shape)
    for id in shape_ids:
        _a_canvas.move(id, x_shift, y_shift)


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
        raise ValueError(
            "The anchor input must be one of "
            + str(anchor_options)
            + " but instead we found "
            + str(anchor)
        )

    outline = _get_outline(tag)
    delta_x = 0
    delta_y = 0

    if anchor == "top_left":
        delta_x = to[0] - outline["left"]
        delta_y = to[1] - outline["top"]
    elif anchor == "top_right":
        delta_x = to[0] - outline["right"]
        delta_y = to[1] - outline["top"]
    elif anchor == "bottom_right":
        delta_x = to[0] - outline["right"]
        delta_y = to[1] - outline["bottom"]
    elif anchor == "bottom_left":
        delta_x = to[0] - outline["left"]
        delta_y = to[1] - outline["bottom"]
    elif anchor == "center":
        delta_x = to[0] - outline["center"][0]
        delta_y = to[1] - outline["center"][1]

    _a_canvas.move(tag, delta_x, delta_y)


def overlay(shape1, shape2, offset_x=0, offset_y=0):
    """
    A reporter function that overlays shape1 onto shape2. It does this by moving shape 1's center
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
    _a_canvas.tag_raise(shape1, shape2)
    return shape1


def portion(shape, start=0, end=0.5):
    """
    Purpose: Take a slice or portion of some already created shape.

    Args:
        shape (`Shape` or Tag): The shape to take a portion of
        start (`float`): A number between 0 and 1 representing where to start the slice.
        end (`float`): A number between 0 and 1 representing where to end the slice.

    For example, taking a portion from 0 to 0.5 of a circle would result in a semi-circle.

    Note: this function is experimental. It might produce unexpected results!
    """
    all_shapes = _a_canvas.find_withtag(shape)

    for a_shape in all_shapes:
        coords = _a_canvas.coords(a_shape)

        start_coord = floor(start * len(coords))
        if start_coord % 2 == 1:
            start_coord = start_coord - 1  # need to start with an x,y pair
        end_coord = floor(end * len(coords))
        if end_coord % 2 == 1:
            end_coord = end_coord - 1  # need to end with an x,y pair

        # slice is up to not including so get the last x,y pair
        new_coords = coords[start_coord : end_coord + 2]

        # loop shape back in on itself
        new_coords.append(new_coords[0])
        new_coords.append(new_coords[1])

        # set the coordinates:
        _a_canvas.coords(a_shape, new_coords)


def put_in_back(shape):
    """
    A function that "lowers" a shape to the "bottom" of the screen."

    Args:
        shape (`Shape` or Tag): The shape in question.
    """
    _a_canvas.tag_lower(shape)


def put_in_front(shape):
    """
    A function that "raises" a shape to the "top" of the screen."

    Args:
        shape (`Shape` or Tag): The shape in question.
    """
    _a_canvas.tag_raise(shape)


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


def scale(shape, x_scale=1.0, y_scale=1.0):
    """
    A function that takes a given `Shape` or tag and scales it on either/both the x and y-axis.

    The two optional inputs accept floats between 0.0 and 1.0. Values greater than 1 will cause
    the shape to grow along that access. Values less than 1.0 will cause the shape to shrink.

    Args:
        shape (`Shape` or Tag): The shape or tag to re-fill.
        x_scale (`float`): How much to scale in the x-axis.
        y_scale (`float`): How much to scale in the y-axis.
    """
    ids = _a_canvas.find_withtag(shape)

    coord = get_center(shape)

    for i in ids:
        _a_canvas.scale(i, coord[0], coord[1], x_scale, y_scale)


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


Utility_Functions = ""


def clear_window(keep_grid=True):
    """
    A function that deletes everything from the window.

    Args:
        keep_grid (`bool`): Whether or not to keep the grid.
    """
    all_shapes = _a_canvas.find_all()

    for shape in all_shapes:
        tags = _a_canvas.gettags(shape)
        if "grid" in tags and keep_grid:
            continue
        _a_canvas.delete(shape)

    global _resize_enabled
    _resize_enabled = True


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


def does_tag_exist(tag):
    """
    Returns `True` if a given tag exists otherwise returns `False`.

    Args:
        `tag` (`str`): [Required] The tag of the object to lookup.

    """
    result = _a_canvas.find_withtag(tag)

    if result:
        return True
    else:
        return False


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
        raise Exception(
            f"We couldn't find the shape with id/tag {shape}. Make sure it exists!"
        )

    return (((bbox[2] + bbox[0]) / 2), ((bbox[1] + bbox[3]) / 2))


def get_colors(shape_or_shapes):
    """
    A reporter function that returns all the colors associated with a tag or list of tags.

    Args:
        shape_or_shapes (`str`/`Shape` or `List`): the shape/tag or list of shapes/tags you'd like to find the colors of

    Returns:
        A `List` containing all **unique** colors associated with that tag(s)
    """
    all_shapes = []
    if not isinstance(shape_or_shapes, list):
        shape_or_shapes = [shape_or_shapes]
    for shape in shape_or_shapes:
        all_shapes += _a_canvas.find_withtag(shape)

    all_colors = []
    for shape in all_shapes:
        color = _a_canvas.itemcget(shape, "fill")
        if color not in all_colors:
            all_colors.append(color)

    return all_colors


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


def get_tag_from_event(event, precision=25):
    """
    Tries to return a tag of an object at a given mouse-event.

    Args:
        event (`Event`): Must be a mouse event otherwise we'll give back an error.
        precision (`int`): How precise in number of pixels does a user have be in order to "select" an object

    Returns a blank string `""` if no shapes are found closer than `precision`.
    """

    if int(event.type) not in [4, 6]:
        raise Exception(f"Received an event that isn't a mouse event: {event}")

    try:
        x = event.x
        y = event.y
        shape_id = _a_canvas.find_closest(x, y)  # get the top shape
        if shape_id and distance(get_center(shape_id), (x, y)) < precision:
            tags = _a_canvas.gettags(shape_id)
            if len(tags) > 0:
                return tags[0]
        return ""

    except:
        raise Exception(
            "No tag found! Maybe you passed us an event that isn't a mouse event?"
        )


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


def get_window_height():
    """
    A reporter function that returns the current height of the window.

    Returns:
         An `int` representing height of the window.
    """
    return _a_canvas.winfo_height()


def get_window_width():
    """
    A reporter function that returns the current width of the window.

    Returns:
         An `int` representing width of the window.
    """
    return _a_canvas.winfo_width()


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


def random_color():
    """
    Returns a random color as a `string` to be used.
    It does not accept any inputs.
    """
    r = lambda: randint(0, 255)
    return "#%02X%02X%02X" % (r(), r(), r())


def listen_for(event_str, handler_function, override=False):
    """
    Sets up a listener for a given event on our window.

    Args:
        event_str (`str`): The magic string that represents this event in the window
        handler_function (`func`): The name (not a string though) of the function you want called when the event his heard
        override (`bool`): Only use this if you speak to Prof. Bain and he recommends it.

    The supported events are:
      * `"LEFT-CLICK"`: Left mouse click
      * `"RIGHT-CLICK"`: Right mouse click
      * `"ALT-CLICK"`: If you're using a PC, this event might instead work for Right Click
      * `"LEFT-DRAG"`: Left mouse clicked and dragged on the screen
      * `"RIGHT-DRAG"`: Right mouse clicked and dragged on the screen
      * `"ALT-DRAG"`: For PCs, this event might instead work for RIGHT-DRAG
      * `"DOUBLE-LEFT"`: Left mouse double click
      * `"DOUBLE-RIGHT"`: Right mouse double click
      * `"DOUBLE-ALT"`: For PCs, this event might instead work for DOUBLE-RIGHT
      * `"KEY"`: The catch-all event for Keyboard presses
    """

    event_translator = {
        "LEFT-CLICK": "<Button-1>",
        "RIGHT-CLICK": "<Button-2>",
        "ALT-CLICK": "<Button-3>",
        "LEFT-DRAG": "<B1-Motion>",
        "RIGHT-DRAG": "<B2-Motion>",
        "ALT-DRAG": "<B3-Motion>",
        "DOUBLE-LEFT": "<Double-Button-1>",
        "DOUBLE-RIGHT": "<Double-Button-2>",
        "DOUBLE-ALT": "<Double-Button-3>",
        "KEY": "<Key>",
    }

    if event_str not in event_translator and not override:
        raise (
            TypeError(
                f"The event you entered, {event_str}, isn't supported. Here are the supported events: {[i for i in event_translator]}"
            )
        )

    event = event_translator[event_str]
    
    listen_for.tracker.add(event_str)

    _a_canvas.bind(event, handler_function)


listen_for.tracker = set()

def setup_shapes(title, background="white", include_grid=True, width=600, height=600):
    """
    A static function that sets up the pop-up window. You can specify the size of the window here.

    However, you should NOT add any calls to this function unless Prof. Bain specifically tells you to!

    Args:
        title (`str`): The title of the pop-up window.
        background (`str`): A valid color as a string to be used as the background color.
        include_grid (`bool`): Whether or not to draw the grid.
        width (`int` or `str`): How wide the window should appear (advanced: use the string "FULLWIDTH" to maximize the width)
        height (`int` or `str`): How wide the window should appear (advanced: use the string "FULLHEIGHT" to maximize the width)
    """

    global _a_canvas
    gui = Tk()
    gui.title(title)

    if width == "FULLWIDTH":
        width = gui.winfo_screenwidth()

    if height == "FULLHEIGHT":
        height = gui.winfo_screenheight()

    _a_canvas = Canvas(gui, background=background, width=width, height=height)
    _a_canvas.pack()
    if include_grid:
        grid(width, height)

    _a_canvas.focus_set()
    return _a_canvas


def update():
    """
    A static function that sets up the pop-up window. **DO NOT USE THIS FUNCTION** unless Prof. Bain explicitly says to use it.
    """
    _a_canvas.update()


def _safe_color(color: str):
    color = color.strip()
    # Could also do some other verifications here...
    return color


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


def _polar_to_cartesian(r, theta):
    return int(r * cos(theta)), int(r * sin(theta))


def _get_outline(shape):
    """
    A reporter function that takes in a shape and calls the various helper functions to generate
    a sort of "summary" of that particular shape and returns it in the form of a dictionary.

    Args:
        shape (`Shape` or Tag): The shape in question.

    Returns:
        a `Dictionary` with the various properties of the shape
    """

    return {
        "center": get_center(shape),
        "left": get_left(shape),
        "right": get_right(shape),
        "top": get_top(shape),
        "bottom": get_bottom(shape),
    }


def _draw_row(row, top_left, colors, pixel=25, tag=""):
    """
    Draws a single row of some pixel art.

    Args:
        row (sequence): the row of artwork to draw
        top_left (`tuple`): the top left coordinate of the pixel art
        color (sequence): the colors to use for each square
        pixel (`int`, optional): how big each individual pixel should be
        tag (`str`, optional): the tag to assign to every square in the row
    """
    x = top_left[0]
    y = top_left[1]
    for cell in row:
        if cell != 0:
            square((x, y), pixel, color=colors[cell], tag=tag)
        x += pixel


def _safe_bbox(shape):
    try:
        bbox = _a_canvas.bbox(shape)
        if bbox is None:
            Exception(
                f"We couldn't find the shape with tag/id: {shape}. Make sure this shape exists!"
            )
        return bbox
    except:
        raise Exception(
            f"We couldn't find the shape with tag/id: {shape}. Make sure this shape exists!"
        )
