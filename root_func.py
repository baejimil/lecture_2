def get_root(a,b,c):
    r1= (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    r2= (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return r1,r2

#한번에 전체를 반환받는 법
root = get_root(1,5,6)
print(root)

#각각을 따로 반환 받는 법
root1, root2 = get_root(1,5,6)
print('r1값은', root1)
print('r2값은', root2)

#SyntaxError: positional argument follows keyword argument
#print(get_root(1,b=5,6))

#TypeError: get_root() got multiple values for argument 'b'
#root3 = get_root(1,6,b=5)


root3 = get_root(1,c=6,b=5)
print(root3)