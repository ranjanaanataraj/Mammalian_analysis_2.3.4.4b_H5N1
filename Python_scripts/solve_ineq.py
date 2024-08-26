#conditions
a,b,c,d belongs to (0,1]
a>b>c
#equations
1a+2b+3c-1d> 0
1a+9c-3d> 0
2b+2c-2d> 0
5b-4d > 0
12c -3d > 0
1b +1c-3d<0
5c-3d >0
3a+5c-3d > 0

# Check all combinations of a, b, c, d with the new condition a > b > c
solution = None
for a, b, c, d in product(possible_values, repeat=4):
    if a > b > c and all(inequalities(a, b, c, d)):
        solution = (a, b, c, d)
        break

print(solution)


a=0.04,b=0.03,c=0.02,d=-0.02
a=1, b = 0.5, c=0.25, d =-0.25