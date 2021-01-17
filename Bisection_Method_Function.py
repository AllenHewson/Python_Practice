def bisection_method(func, lowerbound, upperbound, error_margin):
    while abs(upperbound - lowerbound) >= abs(error_margin):
        middle = (upperbound + lowerbound)/2
        if func(lowerbound)*func(middle) < 0:
            upperbound = middle
        else:
            lowerbound = middle
    # display which bound evaluates closer to 0
    root = 0
    if abs(func(lowerbound)) < abs(func(upperbound)):
        root = lowerbound
    else:
        root = upperbound
    return root