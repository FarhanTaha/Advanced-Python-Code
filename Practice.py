import timeit
print(timeit.timeit(stmt="[1,2,3,4]",number=100000))
print(timeit.timeit(stmt="(1,2,3,4)",number=100000))