from cs110_t4 import *
_ignore = setup_shapes('Lecture 15', background="white", grid=True, width=900, height=800)

########################## YOUR CODE BELOW THIS LINE ##############################
def get_xy(origin, pixel_size, mario_coord):
    x = origin[0]  # extract the x-coordinate
    y = origin[1]  # extract the y-coordinate

    col = mario_coord[0]  # extract the col number
    row = mario_coord[1]  # extract the row number

    new_x = x + col * pixel_size  # calculate the new x
    new_y = y + row * pixel_size  # calculate the new y

    return (new_x, new_y)


def mario(origin, pixel=25, clothes="red", accessories="saddle brown", features="black", tone="bisque", buttons="gold", overalls="blue"):
    # row 0
    # blank, pixel (0,0)
    # blank, pixel (1,0)
    # blank, pixel (2,0)
    square(top_left=get_xy(origin, pixel, (3, 0)), size=pixel, color=clothes)  # pixel (3, 0)
    square(top_left=get_xy(origin, pixel, (4, 0)), size=pixel, color=clothes)  # pixel (4, 0)
    square(top_left=get_xy(origin, pixel, (5, 0)), size=pixel, color=clothes)  # pixel (5, 0)
    square(top_left=get_xy(origin, pixel, (6, 0)), size=pixel, color=clothes)  # pixel (6, 0)
    square( top_left=get_xy(origin, pixel, (7, 0)), size=pixel, color=clothes)  # pixel (7, 0)
    square( top_left=get_xy(origin, pixel, (8, 0)), size=pixel, color=clothes)  # pixel (8, 0)
    
    # row 1
    # blank, pixel (0,1)
    # blank, pixel (1,1)
    square(top_left=get_xy(origin, pixel, (2, 1)), size=pixel, color=clothes)  # pixel (2, 1)
    square(top_left=get_xy(origin, pixel, (3, 1)), size=pixel, color=clothes)  # pixel (3, 1)
    square(top_left=get_xy(origin, pixel, (4, 1)), size=pixel, color=clothes)  # pixel (4, 1)
    square(top_left=get_xy(origin, pixel, (5, 1)), size=pixel, color=clothes)  # pixel (5, 1)
    square(top_left=get_xy(origin, pixel, (6, 1)), size=pixel, color=clothes)  # pixel (6, 1)
    square(top_left=get_xy(origin, pixel, (7, 1)), size=pixel, color=clothes)  # pixel (7, 1)
    square(top_left=get_xy(origin, pixel, (8, 1)), size=pixel, color=clothes)  # pixel (8, 1)
    square(top_left=get_xy(origin, pixel, (9, 1)), size=pixel, color=clothes)  # pixel (9, 1)
    square(top_left=get_xy(origin, pixel, (10, 1)), size=pixel, color=clothes)  # pixel (10, 1)
    square(top_left=get_xy(origin, pixel, (11, 1)), size=pixel, color=clothes)  # pixel (11, 1)

    # row 2
    # blank, pixel (0,2)
    # blank, pixel (1,2)
    square(top_left=get_xy(origin, pixel, (2, 2)), size=pixel, color=accessories)  # pixel (2, 2)
    square(top_left=get_xy(origin, pixel, (3, 2)), size=pixel, color=accessories)  # pixel (3, 2)
    square(top_left=get_xy(origin, pixel, (4, 2)), size=pixel, color=accessories)  # pixel (4, 2)
    square(top_left=get_xy(origin, pixel, (5, 2)), size=pixel, color=tone)  # pixel (5, 2)
    square(top_left=get_xy(origin, pixel, (6, 2)), size=pixel, color=tone)  # pixel (6, 2)
    square(top_left=get_xy(origin, pixel, (7, 2)), size=pixel, color=tone)  # pixel (7, 2)
    square(top_left=get_xy(origin, pixel, (8, 2)), size=pixel, color=features )  # pixel (8, 2)
    square(top_left=get_xy(origin, pixel, (9, 2)), size=pixel, color=tone)  # pixel (9, 2)
    
    # row 3
    square(top_left=get_xy(origin, pixel, (1,3)),size=pixel, color=accessories) 
    square(top_left=get_xy(origin, pixel, (2,3)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (3,3)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (4,3)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (5,3)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (6,3)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (7,3)),size=pixel, color=tone) 
    square(top_left=get_xy(origin, pixel, (8,3)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (9,3)),size=pixel, color=features)
    square(top_left=get_xy(origin, pixel, (10,3)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (11,3)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (12,3)),size=pixel, color=tone)

    # row 4
    square(top_left=get_xy(origin, pixel, (1,4)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (2,4)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (3,4)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (4,4)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (5,4)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (6,4)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (7,4)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (8,4)),size=pixel, color=features)
    square(top_left=get_xy(origin, pixel, (9,4)),size=pixel, color=features)
    square(top_left=get_xy(origin, pixel, (10,4)),size=pixel, color=features)
    square(top_left=get_xy(origin, pixel, (11,4)),size=pixel, color=features)

    # row 5
    square(top_left=get_xy(origin, pixel, (2,5)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (3,5)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (4,5)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (5,5)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (6,5)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (7,5)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (8,5)),size=pixel, color=overalls)

    # row 6
    square(top_left=get_xy(origin, pixel, (1,6)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (2,6)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (3,6)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (4,6)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (5,6)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (6,6)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (7,6)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (8,6)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (9,6)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (10,6)),size=pixel, color=clothes)

    # row 7
    square(top_left=get_xy(origin, pixel, (0,7)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (1,7)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (2,7)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (3,7)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (4,7)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (5,7)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (6,7)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (7,7)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (8,7)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (9,7)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (10,7)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (11,7)),size=pixel, color=clothes)

    # row 8
    square(top_left=get_xy(origin, pixel, (0,8)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (1,8)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (2,8)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (3,8)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (4,8)),size=pixel, color=buttons)
    square(top_left=get_xy(origin, pixel, (5,8)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (6,8)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (7,8)),size=pixel, color=buttons)
    square(top_left=get_xy(origin, pixel, (8,8)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (9,8)),size=pixel, color=clothes)
    square(top_left=get_xy(origin, pixel, (10,8)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (11,8)),size=pixel, color=tone)

    # row 9
    square(top_left=get_xy(origin, pixel, (0,9)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (1,9)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (2,9)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (3,9)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (4,9)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (5,9)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (6,9)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (7,9)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (8,9)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (9,9)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (10,9)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (11,9)),size=pixel, color=tone)

    # row 10
    square(top_left=get_xy(origin, pixel, (0,10)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (1,10)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (2,10)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (3,10)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (4,10)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (5,10)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (6,10)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (7,10)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (8,10)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (9,10)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (10,10)),size=pixel, color=tone)
    square(top_left=get_xy(origin, pixel, (11,10)),size=pixel, color=tone)


    # row 11
    # blank square
    # blank square
    square(top_left=get_xy(origin, pixel, (2,11)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (3,11)),size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (4,11)),size=pixel, color=overalls)
    # blank square
    # blank square
    square(top_left=get_xy(origin, pixel, (7,11)), size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (8,11)), size=pixel, color=overalls)
    square(top_left=get_xy(origin, pixel, (9,11)), size=pixel, color=overalls)

    # row 12
    square(top_left=get_xy(origin, pixel, (1,12)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (2,12)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (3,12)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (4,12)),size=pixel, color=accessories)
    # blank
    # blank
    square(top_left=get_xy(origin, pixel, (7,12)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (8,12)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (9,12)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (10,12)),size=pixel, color=accessories)

    # row 13
    square(top_left=get_xy(origin, pixel, (0,13)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (1,13)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (2,13)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (3,13)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (4,13)),size=pixel, color=accessories)
    # blank
    # blank
    square(top_left=get_xy(origin, pixel, (7,13)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (8,13)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (9,13)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (10,13)),size=pixel, color=accessories)
    square(top_left=get_xy(origin, pixel, (11,13)),size=pixel, color=accessories)

# Now let's make some marios!
mario((0, 20))
mario((420, 250), clothes='#E0607E', pixel=10)
mario((55, 415), clothes='green', pixel=15)
mario((350, 115), pixel=5, clothes='#75B9BE')
mario((420, 400), clothes='#E5F77D', overalls='#75B9BE', pixel=15)
mario((420, 10), pixel=15)

########################## YOUR CODE ABOVE THIS LINE ##############################
_ignore.mainloop()