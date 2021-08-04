def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    # Jared's attempt:
    x = range(start, stop)
    for counter in x:
        print(counter)
    print(stop)   


count_up(5, 7)        
