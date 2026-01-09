def wrapper_sum(func, *a) :
    print("Before", a)
    result = func(*a)
    print("After", result)

wrapper_sum(sum , 1,2,3,4,5)