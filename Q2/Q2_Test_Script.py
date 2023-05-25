# Refer to Q2.ipynb for assumptions, code documentation and implementation of the function.
# There is a section which is used to invoke the functions for testing purposes. You can change the parameters as you wish for manual test cases within the Q2.ipynb file.

# Parameters : (Manual Testing)
# image_1=image matrix containing intensity values(binary image)
# rel=connectivity (4 or 8)

# Parameters for comparison in skimage
# image_1=image matrix(binary image)

# test1_input.txt file is the input image(binary image) which we got by converting the rgb image to gray #and then the gray to binary

# label files are for the first pass throughout the matrix(label_8conn.txt for the 1st pass through #the input image for 8 connectivity and label_4conn.txt for 1st pass in 4 connectivity)

# new_label files for second pass throughout the matrix(new_label_8conn.txt for 2nd pass through the #input image for 8 connectivity and new_label_4conn.txt for 2nd pass in 4 connectivity)

# compare.txt file for comparison with the skimage.measure.label function output for the test1_input.txt image

# There are some examples given within the IPYNB that deal with the changing of parameters. You can change the parameters with your input and run it.

# Ensure the arguments that you pass to the function are in the correct order and are valid and of the correct type.
# Otherwise the program will throw an error and exit.
