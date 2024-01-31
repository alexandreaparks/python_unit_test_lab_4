def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ This function returns the discount earned for a list of item prices.
    If a customer has ordered three or more items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then it will return 4.
    """
    if len(item_prices) >= 3:
        return min(item_prices)
    else:
        return 0

    # more requirements needed - what to do if list is empty, if list has strings, etc.?


if __name__ == '__main__':
    main()