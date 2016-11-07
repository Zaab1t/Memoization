stash = {}


def make_key(func, args, **kwargs):
    arg_key = [(func.__code__.co_varnames[i], args[i]) for i in range(len(args))]
    kwarg_key = [(arg, value) for arg, value in kwargs.items()]
    return tuple(sorted(arg_key + kwarg_key))


def cache(func):
    def inner(*args, **kwargs):
        key = make_key(func, args, **kwargs)
        if func.__name__ in stash:
            if key in stash[func.__name__]:
                return stash[func.__name__][key]
        else:
            stash[func.__name__] = {}
        result = func(*args, **kwargs)
        stash[func.__name__][key] = result
        return result
    return inner
