#-------------------------------
#file:myscript
def square(x):
    """Return the square"""
    return x**2
for n in range(1,4):
    square(n)
    print(n,"Squares is ",square(n))