def newton_raphsons_method(func, dfunc, start_value, evaluation_error_margin):
    # func = function, dfunc = derivative of function, start_value = initial guess,
    # evaluation_error_margin = how close the root evaluates to 0
    approx = start_value
    while func(approx) > evaluation_error_margin:
        approx = approx - func(approx)/dfunc(approx)
    return approx


