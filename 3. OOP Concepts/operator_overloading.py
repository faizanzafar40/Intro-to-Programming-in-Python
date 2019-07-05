class Matrix:
    """ Matrix class. 

    ------ n ----
    | 1 2  3  4
   m| 5 6  7  8
    | 9 10 11 12
    -------------

    """

    def __init__(self, arr):
        self.m = len(arr)
        self.n = len(arr[0])
        self.data = arr

    def get_data(self):
        import copy
        return copy.deepcopy(self.data)

    def __str__(self):
        """ String representation of matrix. """
        ret = ""
        # Iterate through matrix rows
        n = len(self.data)
        for i in range(self.m):
            row = self.data[i]
            for j in range(self.n):
                ret += "{:4}".format(str(row[j]))

            if i != n-1:
                ret += "\n"

        return ret

    # Implement __add__() method to allow
    #       for matrix addition with +-operator

    def __add__(self, m): #m is the object upon which self calls method
        new_data = self.get_data()
        data = m.get_data()

        for i in range(self.m):
            for j in range(self.n):
                new_data[i][j] += data[i][j]
        
        return Matrix(new_data)

if __name__ == "__main__":
    data1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    data2 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]

    # Create matrix object m1 with data of
    #       list data1 and print it to screen.
    m1 = Matrix(data1)
    print(m1)
    print("#" * 20)

    # Create matrix object m2 with data of
    #       list data2 and print it to screen.
    m2 = Matrix(data2)
    print(m2)
    print("#" * 20)
    print("#" * 20)

    # Add up matrices m1 and m2 by using
    #       the +-operator and print result to screen.
    m3 = m1 + m2
    print(m3)

    # Add up matrices m1 and m2 by calling the
    #       __add__() method

    m4 = m1.__add__(m2)
    print(m4)