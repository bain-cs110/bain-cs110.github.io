from math import sqrt, pi, radians, sin, cos

the_canvas = None


def interpolate_colors(color1, color2, frac):
    if "#" not in color1:
        color1 = tuple((c // 256 for c in the_canvas.winfo_rgb(color1)))
    else:
        color1 = _tupelize_color(color1)
    if "#" not in color2:
        color2 = tuple((c // 256 for c in the_canvas.winfo_rgb(color2)))
    else:
        color2 = _tupelize_color(color2)
    return _interpolate_tuple(color1, color2, frac)


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


def make_grid(w, h):
    interval = 100
    # Creates all vertical lines at intervals of 100
    for i in range(0, w, interval):
        the_canvas.create_line(i, 0, i, h, tag="grid_line")
    # Creates all horizontal lines at intervals of 100
    for i in range(0, h, interval):
        the_canvas.create_line(0, i, w, i, tag="grid_line")
    # Creates axis labels
    offset = 2
    for y in range(0, h, interval):
        for x in range(0, w, interval):
            the_canvas.create_oval(
                x - offset, y - offset, x + offset, y + offset, fill="black"
            )
            the_canvas.create_text(
                x + offset,
                y + offset,
                text="({0}, {1})".format(x, y),
                anchor="nw",
                font=("Purisa", 8),
            )


def setup_shapes(some_canvas):
    global the_canvas
    the_canvas = some_canvas


def polygon(points=[], color="hotpink", **kwargs):
    return the_canvas.create_polygon(points, fill=color, **kwargs)


def rectangle(top_left=(0, 0), width=25, height=50, color="hotpink", **kwargs):
    point_0 = top_left
    point_1 = (top_left[0] + width, top_left[1])
    point_2 = (top_left[0] + width, top_left[1] + height)
    point_3 = (top_left[0], top_left[1] + height)

    return the_canvas.create_polygon(
        point_0, point_1, point_2, point_3, fill=color, **kwargs
    )


def square(top_left=(0, 0), size=25, color="hotpink", **kwargs):
    return rectangle(top_left=top_left, width=size, height=size, color=color, **kwargs)


def oval(center=(0, 0), radius_x=25, radius_y=50, color="hotpink", **kwargs):
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

    return the_canvas.create_polygon(point_list, fill=color, **kwargs)


def circle(center=(0, 0), radius=25, color="hotpink", **kwargs):
    return oval(center=center, radius_x=radius, radius_y=radius, color=color, **kwargs)


def triangle(
    bottom_center=(0, 0), width=25, top_shift=0, height=0, color="hotpink", **kwargs
):
    if height == 0:
        height = width * sqrt(3) / 2
    point_0 = (bottom_center[0] - width / 2, bottom_center[1])
    point_1 = (bottom_center[0] + width / 2, bottom_center[1])
    point_2 = (bottom_center[0] + top_shift, bottom_center[1] - height)

    return the_canvas.create_polygon(point_0, point_1, point_2, fill=color, **kwargs)


def line(points=[], color="hotpink", **kwargs):
    return the_canvas.create_line(points, fill=color, **kwargs)


def arc(points=[], width=5, color="hotpink", line_steps=15, **kwargs):
    the_canvas.create_line(
        points,  # tuple of x-y pairs
        width=width,
        fill=color,
        splinesteps=line_steps,
        smooth=True,
        **kwargs
    )


def get_top(tag):
    bbox = the_canvas.bbox(tag)
    return bbox[1]


def get_bottom(tag):
    bbox = the_canvas.bbox(tag)
    return bbox[3]


def get_left(tag):
    bbox = the_canvas.bbox(tag)
    return bbox[0]


def get_right(tag):
    bbox = the_canvas.bbox(tag)
    return bbox[2]


def get_height(tag):
    bbox = the_canvas.bbox(tag)
    return bbox[3] - bbox[1] - 1


def get_width(tag):
    bbox = the_canvas.bbox(tag)
    return bbox[2] - bbox[0] - 1


def distance(p1, p2):
    return sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


def center(tag):
    bbox = the_canvas.bbox(tag)
    return (((bbox[2] + bbox[0]) / 2), ((bbox[1] + bbox[3]) / 2))


def overlay(shape1, shape2, offset_x=0, offset_y=0):
    center1 = center(shape1)
    center2 = center(shape2)
    the_canvas.move(
        shape1,
        (center2[0] - center1[0]) + offset_x,
        (center2[1] - center1[1]) + offset_y,
    )
    the_canvas.tag_raise(shape1, shape2)
    return shape1


def underlay(shape1, shape2, offset_x=0, offset_y=0):
    center1 = center(shape1)
    center2 = center(shape2)
    the_canvas.move(
        shape1,
        (center2[0] - center1[0]) + offset_x,
        (center2[1] - center1[1]) + offset_y,
    )
    the_canvas.tag_lower(shape1, shape2)
    return shape1


def above(shape1, shape2, offset_x=0, offset_y=0):
    overlay(shape1, shape2)
    the_canvas.move(
        shape1,
        0 + offset_x,
        -1 * (get_height(shape2) + get_height(shape1)) / 2 + offset_y,
    )
    return shape1


def beside(shape1, shape2, offset_x=0, offset_y=0):
    overlay(shape1, shape2)
    the_canvas.move(
        shape1,
        (get_width(shape2) + get_width(shape1)) / 2 + offset_x,
        0 + offset_y,
    )
    return shape1


def below(shape1, shape2, offset_x=0, offset_y=0):
    overlay(shape1, shape2)
    the_canvas.move(
        shape1,
        0 + offset_x,
        (get_height(shape2) + get_height(shape1)) / 2 + offset_y,
    )
    return shape1


def duplicate(shape, color=None):
    shape_type = the_canvas.type(shape)
    shape_config = the_canvas.itemconfig(shape)
    shape_coords = the_canvas.coords(shape)
    the_copy = None
    if shape_type == "polygon":
        new_config = {key: shape_config[key][-1] for key in shape_config.keys()}
        if color != None:
            new_config["fill"] = color
        the_copy = the_canvas.create_polygon(shape_coords, **new_config)
        return the_copy


def star(center=(0, 0), radius=50, color="hotpink", outer_radius=75, points=5, **kwargs):
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
    return polygon(vertices, color=color, **kwargs)


def rotate(shape, degrees=5, origin=None):
    if origin is None:
        origin = center(shape)

    theta = radians(degrees)
    ox, oy = origin

    coords = the_canvas.coords(shape)
    # update coordinates:
    for i in range(0, len(coords), 2):
        px, py = coords[i], coords[i + 1]
        qx = cos(theta) * (px - ox) - sin(theta) * (py - oy) + ox
        qy = sin(theta) * (px - ox) + cos(theta) * (py - oy) + oy
        coords[i] = qx
        coords[i + 1] = qy
    # set the coordinates:
    the_canvas.coords(shape, coords)

    return shape
