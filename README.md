# Digital_Image_Processing
This repository contains questions involving important constructs of Digital Image Processing with Python code.

## Q1

![image](https://github.com/shubham11941140/Digital_Image_Processing/assets/63910248/a8434e61-1952-415b-b6dc-68f80ed12739)

![image](https://github.com/shubham11941140/Digital_Image_Processing/assets/63910248/f2843534-da04-4a82-95b7-b5eba8e3417d)

Refer to Q1.ipynb for assumptions, code documentation and implementation of the function.

There is a section which is used to invoke the functions for testing purposes. You can change the parameters as you wish for manual test cases within the Q1.ipynb file.

Parameters : (Manual Testing)

mat = Image Matrix containing intensity values
p = start point
q = end point
V = set of intensities for which the path should be extracted
adj = type of path requested by the user where I have defined adj1 for 4-path, adj2 for 8-path and adj3 for m-path.
(Enter the value of adj as '4', '8' or 'm' for adj1, adj2 and adj3 respectively)

There are some examples given within the IPYNB that deal with the changing of parameters. You can change the parameters with your input and run it.

Ensure the arguments that you pass to the function are in the correct order and are valid and of the correct type.
Otherwise the program will throw an error and exit.

Refer to the Q1_output.txt file for the output of the sample test case given in the question.

### Output:
```
All paths of 4 type with their lengths
No path exists of 4 type
All paths of 8 type with their lengths
length: 7  path: (3,0):2->(2,0):2->(1,0):4->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 6  path: (3,0):2->(2,0):2->(1,0):4->(2,1):2->(1,2):4->(0,3):2->(1,4):2
length: 6  path: (3,0):2->(2,0):2->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 5  path: (3,0):2->(2,0):2->(2,1):2->(1,2):4->(0,3):2->(1,4):2
length: 7  path: (3,0):2->(2,0):2->(3,1):4->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 6  path: (3,0):2->(2,0):2->(3,1):4->(2,1):2->(1,2):4->(0,3):2->(1,4):2
length: 5  path: (3,0):2->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 4  path: (3,0):2->(2,1):2->(1,2):4->(0,3):2->(1,4):2
length: 8  path: (3,0):2->(3,1):4->(2,0):2->(1,0):4->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 7  path: (3,0):2->(3,1):4->(2,0):2->(1,0):4->(2,1):2->(1,2):4->(0,3):2->(1,4):2
length: 7  path: (3,0):2->(3,1):4->(2,0):2->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 6  path: (3,0):2->(3,1):4->(2,0):2->(2,1):2->(1,2):4->(0,3):2->(1,4):2
length: 6  path: (3,0):2->(3,1):4->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 5  path: (3,0):2->(3,1):4->(2,1):2->(1,2):4->(0,3):2->(1,4):2
length: 9  path: (3,0):2->(4,1):2->(3,1):4->(2,0):2->(1,0):4->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 8  path: (3,0):2->(4,1):2->(3,1):4->(2,0):2->(1,0):4->(2,1):2->(1,2):4->(0,3):2->(1,4):2
length: 8  path: (3,0):2->(4,1):2->(3,1):4->(2,0):2->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 7  path: (3,0):2->(4,1):2->(3,1):4->(2,0):2->(2,1):2->(1,2):4->(0,3):2->(1,4):2
length: 7  path: (3,0):2->(4,1):2->(3,1):4->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 6  path: (3,0):2->(4,1):2->(3,1):4->(2,1):2->(1,2):4->(0,3):2->(1,4):2
length: 10  path: (3,0):2->(4,1):2->(4,2):4->(3,1):4->(2,0):2->(1,0):4->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 9  path: (3,0):2->(4,1):2->(4,2):4->(3,1):4->(2,0):2->(1,0):4->(2,1):2->(1,2):4->(0,3):2->(1,4):2
length: 9  path: (3,0):2->(4,1):2->(4,2):4->(3,1):4->(2,0):2->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 8  path: (3,0):2->(4,1):2->(4,2):4->(3,1):4->(2,0):2->(2,1):2->(1,2):4->(0,3):2->(1,4):2
length: 8  path: (3,0):2->(4,1):2->(4,2):4->(3,1):4->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 7  path: (3,0):2->(4,1):2->(4,2):4->(3,1):4->(2,1):2->(1,2):4->(0,3):2->(1,4):2
Shortest path of 8 type.
['8', 4, '(3,0):2->(2,1):2->(1,2):4->(0,3):2->(1,4):2']
All paths of m type with their lengths
length: 6  path: (3,0):2->(2,0):2->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
length: 6  path: (3,0):2->(3,1):4->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2
Shortest path of m type.
['m', 6, '(3,0):2->(2,0):2->(2,1):2->(1,2):4->(0,3):2->(0,4):4->(1,4):2']

```

## Q2

![image](https://github.com/shubham11941140/Digital_Image_Processing/assets/63910248/8c970f91-388f-493e-bd25-f12779bdc69b)

**The python's inbuilt function for bwconcomp is skimage.measure.label**

Refer to Q2.ipynb for assumptions, code documentation and implementation of the function.

There is a section which is used to invoke the functions for testing purposes. You can change the parameters as you wish for manual test cases within the Q2.ipynb file.

Parameters : (Manual Testing)
image_1 = image matrix containing intensity values(grayscale image)
rel = connectivity (4 or 8)
V = set of intensities for which the connectivity should be checked

Parameters for comparison in skimage
image_1 = image matrix (grayscale image)
rel = connectivity
(Input connectivity as 1 for 4-path and 2 for 8-path)

There are some examples given within the IPYNB that deal with the changing of parameters. You can change the parameters with your input and run it.

Ensure the arguments that you pass to the function are in the correct order and are valid and of the correct type.
Otherwise the program will throw an error and exit.

**For Image**

![image](https://github.com/shubham11941140/Digital_Image_Processing/assets/63910248/e8e333e8-caed-4809-96a9-428999503815)

### Output:

**Our Algorithm**

![image](https://github.com/shubham11941140/Digital_Image_Processing/assets/63910248/ef4043a0-72a2-459f-a019-5ccf5e8dfcf5)

**Library Algorithm**

![image](https://github.com/shubham11941140/Digital_Image_Processing/assets/63910248/b4eab3b9-8e46-489a-8f0a-8792633c4777)


## Q3

![image](https://github.com/shubham11941140/Digital_Image_Processing/assets/63910248/28b6a68f-2fcd-4b8e-ab2d-0b1c38145a54)

Refer to Q3.ipynb for assumptions, code documentation and implementation of the function.

In the Q3_Test_Script.py,
you can enter the Main function and change the paramenters as you wish for manual test cases.

Random Function has seed set to 0. If you want to change the seed, change the value of the seed variable in the Random Function.

Parameters: (Well-defined in the question)
M - Number of rows in the image matrix
N - Number of columns in the image matrix
border - Border width
n - Number of circles to be drawn
r1 - lower bound of radius of the circles
r2 - upper bound of radius of the circles
Vf - Intensity Value Range of the foreground pixels
Vb - Intensity Value Range of the background pixels

Ensure the arguments that you pass to the function are in the correct order and are valid and of the correct type.
Otherwise the program will throw an error and exit.

**To Run the code and generate the circles in grayscale**

```

python3 Q3_Test_Script.py

```
(Even if you don't change the parameters, the test script will run the default test cases automatically.)

The output is saved as Q3.PNG.

### Output:

![Q3](https://github.com/shubham11941140/Digital_Image_Processing/assets/63910248/fb549788-9794-4a04-a3ee-7edc5c329437)


## Q4

![image](https://github.com/shubham11941140/Digital_Image_Processing/assets/63910248/7492d63c-e01b-4c6c-908c-441bd0546ca7)

Refer to Q4.ipynb for assumptions, code documentation and implementation of the function.

In the Q4_Test_Script.py,
you can enter the Main function and change the paramenters as you wish for manual test cases.

Random Function has seed set to 0. If you want to change the seed, change the value of the seed variable in the Random Function.

Parameters: (Well-defined in the question)
M - Number of rows in the image matrix
N - Number of columns in the image matrix
border - Border width
n - Number of rectangles to be drawn
w1 - lower bound of width of the rectangles
w2 - upper bound of width of the rectangles
alpha - number of possible orientations of the rectangles (either 1 or 2)
orientation - orientation of the rectangles (subset of array([1, 2]))
Vf - Intensity Value Range of the foreground pixels
Vb - Intensity Value Range of the background pixels

Ensure the arguments that you pass to the function are in the correct order and are valid and of the correct type.
Otherwise the program will throw an error and exit.


**To Run the code and generate the rectangles in grayscale**

```

python3 Q4_Test_Script.py

```
(Even if you don't change the parameters, the test script will run the default test cases automatically.)

The output is saved as Q4.PNG.

### Output:

![Q4](https://github.com/shubham11941140/Digital_Image_Processing/assets/63910248/b1f5edd5-c7fa-4212-acdf-6eb5251e2039)


## Q5

![image](https://github.com/shubham11941140/Digital_Image_Processing/assets/63910248/8b68bb81-6ad5-4c67-adc1-0802f71996ce)

Refer to the Q5.ipynb for assumptions, code documentation and implementation of the function.

There is a section which is used to invoke the functions for testing purposes. You can change the parameters as you wish for manual test cases
within the Q5.ipynb file.

Parameters: (Manual Testing)

N - Integer that represents the number of symbols that must be encoded in a chunk

single_channel_image - NumPy Array of shape (H, W) that represents the image to be encoded or variable storing the Grayscale image to be encoded (Default None)

message = Message to be encoded (list of characters) (Default None)

prob_matrix - Probability Matrix (Normalized histogram of the image) (Map of characters and probability values in format specified in example) (Default None)

There are some examples given within the IPYNB that deal with the changing of parameters. You can change the parameters with your input and run it.

Ensure the arguments that you pass to the function are in the correct order and are valid and of the correct type.
Otherwise the program will throw an error and exit.

**Theory to define the Arithmetic Coding**

**Problem**:

$2$ numbers $n_1$ and $n_2$ are given. We need to find the number $n$ such that $n_1 \leq n \leq n_2$ and $n$ has minimum number of digits after decimal point.

**Algorithm / Solution**:

We know that $n_1 = 0.a_1a_2a_3...a_n$ and $n_2 = 0.b_1b_2b_3...b_k$

Now, let there exist a common prefix in $a's$ and $b's$. (Common Prefix can also be empty)

Then, $n_1 = 0.a_1a_2a_3...a_n$ and $n_2 = 0.a_1a_2a_3...a_ic_1c_2c_3...c_m$. ($i \geq 0$)

We know that the number with minimum number of decimal digits will have the prefix $0.a_1a_2a_3...a_i$

So first we take it out and consider the remaining parts $a_{i+1}...a_n$ and $c_1c_2c_3...c_m$

There can be following cases:

**1.)** $m > 1$ i.e. remaiining part of $n_2$ contains atleast $2$ digits. So, we can take $0.a_1a_2a_3...a_ic_1$ as the number with minimum number of digits after decimal point.

Example: $n_1 = 0.123456$ and $n_2 = 0.12345789$.

Here, common prefix is $0.12345$.

Remaining part of $n_1$ is $6$ and remaining part of $n_2$ is $789$.

We see more than $1$ digits in remaining part of $n_2$.

Hence, take $0.123457$ as the number with minimum number of decimal digits.

**2.)** $m = 1$ i.e. remaiining part of $n_2$ contains $1$ digit.

Now we focus on the remaining part of $n_1$.

Remaining part of $n_1$ is $a_{i+1}...a_n$

Now, we know that $n_2 \geq n_1$.

Hence, $c_1 \geq a_{i+1}$

Hence, $a_{i+1} \leq 8$

**2.a)**

If $i+1 = n$ i.e. $a_{i+1}$ is the last digit of $n_1$.

Then, we can take $0.a_1a_2a_3...a_{i+1}$ as the number with minimum number of digits after decimal point.

**2.b)**

Otherwise, let remaining part of $n_1$ be $a_{i+1} \hspace{1mm} 99999..(t-times \hspace{1mm} 9) \hspace{1mm} a_{i+t+2}...a_{n}$ ($t \geq 0$)

if $i + t + 2 \leq n$ i.e. Last digit is not $9$,

Then the answer is $0.a_1a_2a_3...a_{i+1} \hspace{1mm} 99999 \hspace{0.5mm} ._{(t+1-times)}$

Else, the answer is $0.a_1a_2a_3...a_{i+1} \hspace{1mm} 99999 \hspace{0.5mm} ._{(t-times)}$

**Output**:

```
Number with minimum decimal digits in the range (0.399999, 0.422222): 0.4
Number with minimum decimal digits in the range (0.399999, 0.4): 0.399999
Number with minimum decimal digits in the range (0.39999, 0.5): 0.4
Number with minimum decimal digits in the range (0.39999923, 0.4): 0.3999999
Number with minimum decimal digits in the range (0.24123123, 0.3): 0.29
Number with minimum decimal digits in the range (0.24123123, 0.25123124): 0.25
Number with minimum decimal digits in the range (0.88, 0.89): 0.88
```
