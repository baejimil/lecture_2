def kwarg_param(**kwargs):
    print('인자의 개수는 :', len(kwargs))
    print('인자는:', kwargs)


kwarg_param(first='a', second='b', third='c')