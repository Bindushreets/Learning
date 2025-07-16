'''----------------------------------------------------'''
#       Set of Examples for Pattern Matching....!
'''----------------------------------------------------'''

1. # Inverted Right-Angled Triangle :

rows = 5
for i in range(rows, 0, -1):
    print("*" * i)

# Output :
'''
*****
****
***
**
*
'''
#-----------------------------------------------------------------

2. # Left-Aligned Triangle with Spaces :

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

# Output :
'''
    *
   **
  ***
 ****
*****
'''
#-----------------------------------------------------------------

3. # Number Pyramid :

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Output :
'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5             
'''
#-----------------------------------------------------------------

4. # Repeating Number Pattern :

rows = 5
for i in range(1, rows + 1):
    print(str(i) * i)

# Output :
'''
1
22
333
4444
55555
'''
#-----------------------------------------------------------------

5. # Square of Asterisks :

rows = 5
for i in range(rows):
    print("* " * rows)

# Output :
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
#-----------------------------------------------------------------

6. # Right Triangle with Numbers :

rows = 5
for i in range(1, rows + 1):
    print(" ".join(str(x) for x in range(1, i + 1)))

# Output :

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
#-----------------------------------------------------------------

7. # Alternating Binary Pattern :

rows = 5
for i in range(1, rows + 1):
    print("".join("1" if (i + j) % 2 == 0 else "0" for j in range(i)))
     # Uses even/odd logic to alternate 1s and 0s.
    
# Output :
'''
0
10
010
1010
01010
'''
#-----------------------------------------------------------------

8. # Hollow Square :

rows = 5
for i in range(rows):

    for j in range(rows):

        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()

# Output : Borders only, center is empty.
'''
* * * * *
*       *
*       *
*       *
* * * * *
'''
#-----------------------------------------------------------------

9. # Inverted Pyramid :

rows = 5
for i in range(rows, 0, -1):
    spaces = ' ' * (rows - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

# Output :
'''
*********
 *******
  *****
   ***
    *
'''
#-----------------------------------------------------------------

10. # Alphabet Triangle :

rows = 6
for i in range(rows):
    print(chr(65 + i) * (i + 1))  # Uses chr() to convert numbers to letters (A, B, C...).

# Output :
'''
A
BB
CCC
DDDD
EEEEE
FFFFFF
'''
#-----------------------------------------------------------------

11. # Pascal’s Triangle (First Few Rows) :

rows = 5
for i in range(rows):
    number = 1

    for j in range(i + 1):
        print(number, end=" ")
        number = number * (i - j) // (j + 1) # Classic math triangle with binomial coefficients!
    print()

# Output :
'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''
#-----------------------------------------------------------------

12. # Diamond Pattern :

# Combines pyramid and inverted pyramid.
rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Output :
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
#-----------------------------------------------------------------

13. # Zig-Zag Numbers :

rows = 5
for i in range(1, rows + 1):
    print(" ".join(str(i * j) for j in range(1, i + 1))) # Multiplies i with j for dynamic values.

# Output :
'''
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
'''
#-----------------------------------------------------------------

14. # Hollow Triangle :

# use of conditionals for borders only!
rows = 5
for i in range(1, rows + 1):

    for j in range(1, i + 1):

        if j == 1 or j == i or i == rows:
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()

# Output :
'''
*
* *
*   *
*     *
* * * * *
'''
#-----------------------------------------------------------------

15. # Number Square :

# Uniform numbers each row.
rows = 5
for i in range(1, rows + 1):

    for j in range(1, rows + 1):
        print(j, end=" ")
    print()

# Output :
'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
#-----------------------------------------------------------------

16. # Floyd’s Triangle :
''' A right-angled triangular array of natural numbers,
        where the numbers are arranged sequentially,
        starting with 1 in the top left corner and 
        increasing by one in each subsequent row. '''

# understanding incrementing sequences.
rows = 5
num = 1
for i in range(1, rows + 1):

    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Output :
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
#-----------------------------------------------------------------

17. # Snake Pattern : Alternates row directions like a snake!

rows = 5
count = 1

for i in range(rows):
    row = []

    for j in range(rows):
        row.append(str(count))
        count += 1

    if i % 2 == 1:
        row.reverse()
    print(" ".join(row))

# Output :
'''
1 2 3 4 5
10 9 8 7 6
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25
'''
#-----------------------------------------------------------------

18. # Hourglass : Symmetrical top and bottom.

rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

for i in range(2, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Output :
'''
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
'''
#-----------------------------------------------------------------

19. # Centered Cross : Shapes like a big plus sign.

rows = 5
for i in range(rows):

    for j in range(rows):

        if i == rows // 2 or j == rows // 2:
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()

# Output :
'''
    *
    *
* * * * *
    *
    *
'''
#-----------------------------------------------------------------

20. # Continuous Alphabet Fill : Fills letters across rows A, B, C...

rows = 5
ch = 65
for i in range(rows):

    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()

# Output :
'''
A
B C
D E F
G H I J
K L M N O
'''
#-----------------------------------------------------------------

21. # Right Arrow : Builds forward and backward.

rows = 5
for i in range(1, rows + 1):
    print("*" * i)

for i in range(rows - 1, 0, -1):
    print("*" * i)

# Output :
'''
*
**
***
****
*****
****
***
**
*
'''
#-----------------------------------------------------------------

22. # Border Only Grid : Decorates just the outer layer.

rows = 5
for i in range(rows):

    for j in range(rows):

        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("#", end=" ")

        else:
            print(" ", end=" ")
    print()

# Output :
'''
# # # # #
#       #
#       #
#       #
# # # # #
'''
#-----------------------------------------------------------------

23. # Diagonal Line : A simple slash-shaped diagonal.

rows = 5
for i in range(rows):
    print(" " * i + "*")

# Output :
'''
*
 *
  *
   *
    *
'''
#-----------------------------------------------------------------

24. # X Pattern : Connects top-left to bottom-right and vice versa.

rows = 5
for i in range(rows):
    for j in range(rows):
        if i == j or i + j == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Output :
'''
*       *
  *   *
    *
  *   *
*       *
'''
#-----------------------------------------------------------------

25. # Spiral Numbers Matrix :

n = 5
matrix = [[0]*n for _ in range(n)]

val = 1
top, left, bottom, right = 0, 0, n - 1, n - 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        matrix[top][i] = val
        val += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i][right] = val
        val += 1
    right -= 1

    for i in range(right, left - 1, -1):
        matrix[bottom][i] = val
        val += 1
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        matrix[i][left] = val
        val += 1
    left += 1

for row in matrix:
    print(' '.join(str(x).rjust(2) for x in row))

# Output :
'''
 1  2  3  4  5
16 17 18 19  6
15 24 25 20  7
14 23 22 21  8
13 12 11 10  9
'''
#-----------------------------------------------------------------















