def args_func(*args):
    print(len(args))
    for ar in args:
        print(ar)
    return args


def key_args_func(**kwargs):
    print(kwargs.keys(), kwargs.values())
    print('hey', kwargs.get('lol'))

    for arg in kwargs:
        print(arg)


def unpack(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


# args_func('one', 2, ['a', 'b'])
# key_args_func(lol='lol1', kw='hello')
tup = ('arg1', 'arg2', 'arg3')
unpack(*tup)