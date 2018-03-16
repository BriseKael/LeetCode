class Solution:
    def palindromePairs(self, words):
        wordict = {}
        result = []
        for i in range(len(words)):
            wordict[words[i]] = i

        for i in range(len(words)):
            for j in range(len(words[i])+1):
                tmp1 = words[i][:j]
                tmp2 = words[i][j:]
                if tmp1[::-1] in wordict and wordict[tmp1[::-1]] != i and tmp2 == tmp2[::-1]:
                    result.append([i, wordict[tmp1[::-1]]])
                if j != 0 and tmp2[::-1] in wordict and wordict[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:
                    result.append([wordict[tmp2[::-1]], i])
        return result
    
