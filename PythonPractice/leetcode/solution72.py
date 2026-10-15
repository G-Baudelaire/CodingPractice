# Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]

        # Initialise
        for i in range(len(word1)+1):
            matrix[i][-1] = len(word1) - i

        for j in range(len(word2)+1):
            matrix[-1][j] = len(word2) - j

        print(matrix)
        for i in reversed(range(len(word1))):
            for j in reversed(range(len(word2))):
                if word1[i] == word2[j]:
                    ans = matrix[i+1][j+1]
                else:
                    ans = min(matrix[i+1][j],matrix[i][j+1],matrix[i+1][j+1]) + 1
                matrix[i][j] = ans

        return matrix[0][0]

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1, word2))