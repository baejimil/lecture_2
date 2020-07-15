def print_star(n=1):
    for _ in range(n):
        print('***********************')


print_star()
print('다음은 인자값으로 위치인자로 3을 넣어 줬을때')
print_star(3)
print('다음은 인자값으로 키워드인자로 4를 넣어 줬을때')
print_star(n=4)