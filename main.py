# Name: Ciota Dragos Ioan
# Programming language: python

# Here we check if it's possible to split A into two arrays with the same average
# With the formula we found (sum(B) = (len(B)*sum(A))/len(A)) we take all the number of
# elements B and C could have
# B and C can have maximum n-1 elements but then results that the other one will have 1 element,
# and it should also respect the formula. So it's alright to only go until B and C are equal in size
# if we find one possible solution we return True
def check_if_possible(n, sum):
    for i in range(1, int(n / 2 + 1)):
        if (sum * i) % n == 0:
            return True
    return False


def split_array_problem(A):
    # We know that the average of B is equal to the average of C
    # We also know that the average of C is equal to sum(C)/len(C)
    # Also sum(C)/len(C) = (sum(A)-sum(B))/(len(A)-len(B))
    # So from here results that: sum(B)/len(B) = sum(C)/len(C) = (sum(A)-sum(B))/(len(A)-len(B))
    # We multiply the first and last fraction diagonally
    # => sum(B)*(len(A)-len(B)) = len(B)*(sum(A)-sum(B))
    # After simplifying we have a formula: sum(B) = (len(B)*sum(A))/len(A)
    # So we know that both B and C should respect this formula
    # We check and return False if it's not possible
    if check_if_possible(len(A), sum(A)) == 0:
        return False

    # Now I am making a set that will contain pairs of all possible sums and for each sum how many numbers it is
    # composed of
    sums = set()
    sums.add((0, 0))

    # We go through all of A's elements
    for i in range(len(A)):
        newSums = set()
        for element in sums:
            # We add the pair(A[i], 1) to the sums set, and we add A[i] to all existing sums and increase how many
            # elements are in that sum
            newSums.add((element[0] + A[i], element[1] + 1))
            newSums.add((A[i], 1))
        sums = sums | newSums

    # For all of our results we check to see if any of them respects the formula we found
    # If yes we return True, otherwise we return False
    for pair in sums:
        if pair[1] != len(A) and pair[1] != 0:
            if float(pair[0]) == float(float(pair[1] * sum(A)) / float(len(A))):
                return True

    return False


def main():
    print(split_array_problem([1, 2, 3, 4, 5, 6, 7, 8]))


main()
