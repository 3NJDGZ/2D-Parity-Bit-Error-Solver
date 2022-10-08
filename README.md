# 2D-Parity-Bit-Error-Solver
This Program generates a 2D 8*8 binary matrix with an odd parity enforced upon it. Then it will transpose a random bit and print its position.

This Program will create a 2D Binary Array where the first column, and last row are used as parity bits which enforce an odd parity upon the system (so all binary numbers are odd both vertically, and horizontally). The program will generate a random 8 by 8 binary array with an Odd Parity, then it will transpose (flip) a random bit within the 2 dimensional array from a 0 to a 1, and vice versa. Next, the program will then attempt to solve, and find the transposed bit by traversing through the 2 dimensional array vertically, and horizontally therefore printing the solution in terms of its positioning with respect to the columns, and rows. Furthermore, it will also print the transposed 2 dimensional array before attempting to solve for the solution.

Parity bits are used within error checking for computer systems, as data transmitted will always have some sort of defect with them (e.g., an accidental transposed bit). This program is just used to simulate this type of situation.
