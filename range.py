"""
range(stop): integers from 0 to stop
range(start, stop): integers between start (including) till stop (excluding)
range(start, stop, step): integers between start (including) till stop (excluding), 
that are incremented by the value of step
"""

range(5)            # 0, 1, 2, 3, 4
range(1, 5)         # 1, 2, 3, 4
range(2, 10, 2)     # 2, 4, 6, 8
range(10, 2, -2)    # 10 8 6 4 


for i in range(5):
    print(i, end=" ")
# 0, 1, 2, 3, 4


# Multiplication table
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n")


numbers = list(range(10))
print(numbers)      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(2, 10))
print(numbers)      # [2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(10, 2, -2))
print(numbers)      # [10, 8, 6, 4]
