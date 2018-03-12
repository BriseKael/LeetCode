class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        y = str(x)
        if x < 0:
            z = ''
            for i in reversed(y[1:]):
                z += i
            z = '-' + z
        elif x == 0:
            return 0
        else:
            z = ''
            for i in reversed(y):
                z += i
        if abs(int(z)) > 2**31 - 1:
            return 0
        else:
            return int(z)
            
