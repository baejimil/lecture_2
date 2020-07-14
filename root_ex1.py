def root_ex1(a,b,c):
    x1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
    x2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)
    print(x1, '또는', x2)
root_ex1(1, -2, -3)