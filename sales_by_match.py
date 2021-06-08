# Sales by Match
# Problem Statement:
# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.

# Example
# arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# There is two pair of color 10 and one of color 20.
# There are three odd socks left, one of each color (30, 50, 20 ).
# The number of pairs is 3.


def sock_merchant(socks):
    x = {}
    count = 0
    for sock in socks:
        if x.get(sock) is None:
            x.update({sock: 1})
        else:
            x.pop(sock)
            count += 1
    return count


if __name__ == "__main__":
    arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    pairs = sock_merchant(arr)
    print(pairs)

    arr2 = [1, 1, 2, 2, 3, 2, 1, 4, 5, 3, 1, 2]
    pairs2 = sock_merchant(arr2)
    print(pairs2)
