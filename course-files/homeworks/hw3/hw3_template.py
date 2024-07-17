from cs110_hw3_shapes import *
_ignore = setup_shapes('HW 3', background="white", width=800, height=800)
########################## YOUR CODE BELOW THIS LINE ##############################

## Sample Design! (delete this before you submit)

face = circle((450, 450), radius=100, color="yellow") #face
left_eye = oval(radius_x=20, radius_y=30, color="red") #left eye 
right_eye = oval(radius_x=20, radius_y=30, color="green") # right eye 
mouth = oval(radius_x=40, radius_y=10, color="blue") # mouth 

# Now position the features
overlay(left_eye, face, offset_x=-30, offset_y=-20) 
overlay(right_eye, face, offset_x=30, offset_y=-20) 
overlay(mouth, face, offset_y=50)

## End sample design





########################## YOUR CODE ABOVE THIS LINE ##############################
_ignore.mainloop()