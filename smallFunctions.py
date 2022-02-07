import Parameters as par


def varNum():  # a function to define number of variables based on pid numbers
    a = 0
    if par.pid1 == 2:
        a = a + 3
    if par.pid2 == 2:
        a = a + 3
    if par.pid3 == 2:
        a = a + 3
    return a
