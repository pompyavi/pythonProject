def inclusive_range(*args):

    args_length = len(args)
    start = 0
    stop = 0
    step = 1

    if args_length < 0:
        raise TypeError("Expected at least 1 argument")
    elif args_length == 1:
        stop = args[0]
    elif args_length == 2:
        (start, stop) = (args[0], args[1])
    elif args_length == 3:
        (start, stop, step) = (args[0], args[1], args[2])
    else:
        raise TypeError("Function takes at the most 3 arguments")

    while start <= stop:
        yield start
        start += step


for i in inclusive_range(5, 20, 5):
    print(i, end=' ')

