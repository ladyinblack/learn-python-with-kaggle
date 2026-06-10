# Add code to the folowing cell to swap variables `a` and `b` 
# (so that `a` refers to the object previously referred to by `b` and vice versa).
a = [1, 2, 3]
b = [3, 2, 1]

print("Original contents of lists:")
print("a: ", a)
print("b: ", b)

temp = a
a = b
b = temp

print("Contents of lists after swapping:")
print("a: ", a)
print("b: ", b)
