class Solution(object):

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        index = 0
        for i in range(0, len(A)):
            if A[i] >= 0:
                break
            else:
                index += 1

        neg = [x*x for x in A[:index]]
        pos = [x*x for x in A[index:]]

        return self.merge(neg[::-1], pos)

    def merge(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        i = 0
        j = 0
        sorted_list = []

        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                sorted_list.append(A[i])
                i += 1
            else:
                sorted_list.append(B[j])
                j += 1

        while i < len(A):
            sorted_list.append(A[i])
            i += 1

        while j < len(B):
            sorted_list.append(B[j])
            j += 1

        return sorted_list
