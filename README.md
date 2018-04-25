# Pascal's Triangle
## Code Em Assignment - Middle Intermediate

Pascal's triangle is a 2-D (triangular) array where each element is the sum of the two numbers above it. Every row/level sums to 2<sup>i</sup>, where i is the triangle level, starting with 0. In python, we can represent this as a list of lists:

`` [ [1], [1,1], [1,2,1], [1,3,3,1], ... ] ``

Your assignment is to create a program (in any language, but Python is encouraged since that is our Primary instructional language) that will generate Pascal's triangle given an input for the number of levels. Then you will produce a plot where the x-axis is the level number and y is the sum of that level, but you should actually sum the row your program generated.

For this assignment, you'll see a python program you can use as a basis for your solution. The included program generates the Fibonacci series and plots it. To run it, using Python 3.6, you can simply:

``python fib_plot.py``

in the same directory that the file is in or use IDLE to execute the file.

## Minimum Requirements

* Python program includes a function to return an arbitrary level Pascal's triangle -- input: level, return: list of lists.
* Python program uses the returned list of lists and plots the triangle where x is the level and y is the sum of the level.

## Additional Requirements (think extra credit)

* Enhance the program to either take a command line argument or prompt for input in order to set the depth of the triangle.
* Use a list comprehension to prepare the list of sums for the plot.
* Explain why we, at Tech Em, truly appreciate Pascal's triangle!

## Rubric

| Criteria | Superior (5) | Excellent (4) | OK (3) | Not OK (2) | Unsatisfactory (1) | Grade/Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Readability (50%) | The code is organized (modular) well documented, easy to read and follow. | The code is easy to read and well documented. | The code can be followed. | The code is not easily followed. | The code is a mess. |  |
| Specifications (40%) | The program works and meets all the requirements. | The program works and meets most of the requirements. | The program produces correct results but does not display/plot them correctly. | The program does not meet most of the requirements or fails to display or plot any. | Program does not work at all. |  |
| Efficiency (10%) | The code is highly efficient without affecting readability. | The code is reasonably efficient without affecting readability. | The code runs within a few seconds. | The code runs within a few minutes. | The code takes over an hour to run (or doesn't run at all). | |

