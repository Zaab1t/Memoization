import cache
import time

# This runs in 3 seconds with the annotation and 8 seconds without.


@cache.cache
def f(x):
    time.sleep(1)
    return x**2


@cache.cache
def h(l, p):
    time.sleep(1)
    return l**2 + p


print(f(5))
print(f(x=5))

print(f(9))
print(f(9))

print(h(l=5, p=2))
print(h(p=2, l=5))
print(h(5, 2))
print(h(5, p=2))

print(cache.stash)
