def foo(*args):
    print('인자의 개수:', len(args))
    print('인자는:', args)

foo(10,20,30)
#foo(a=10,b=10,c=30)