class Solution:

    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = {}

        for j in J:
            jewels[j] = 0

        for s in S:
            if s in jewels.keys():
                jewels[s] += 1

        return sum(jewels.values())
