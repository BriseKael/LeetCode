class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        n = n
        results = list()

        def try_n_times_line_by_line(deep, q_list):
            if -1 in q_list:
                level = n - deep
                x_plus_y = set()
                x_minus_y = set()

                for x in range(level):
                    x_plus_y.add(x + q_list[:level][x])
                    x_minus_y.add(x - q_list[:level][x])

                for y in range(n):
                    if y not in q_list[:level] and \
                       level + y not in x_plus_y and \
                       level - y not in x_minus_y:
                        next_q_list = q_list[:]
                        next_q_list[level] = y
                        try_n_times_line_by_line(deep - 1, next_q_list)

            else:
                results.append(q_list)

        try_n_times_line_by_line(n, [-1] * n)
        return [['.' * i + 'Q' + '.' * (n-i-1) for i in result] for result in results]
        
