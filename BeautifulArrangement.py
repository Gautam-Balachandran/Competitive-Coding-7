# Time Complexity : O(n!), where n is the input number
# Space Complexity : O(n)

class Solution:
    def __init__(self):
        self.count = 0

    def countArrangement(self, n: int) -> int:
        visited = [False] * (n + 1)
        self.countPerm(n, 1, visited)
        return self.count

    def countPerm(self, n: int, pos: int, visited: list):
        if pos > n:
            self.count += 1
            return
        for i in range(1, n + 1):
            if not visited[i] and (i % pos == 0 or pos % i == 0):
                visited[i] = True
                self.countPerm(n, pos + 1, visited)
                visited[i] = False  # Backtrack

# Example usage
solution = Solution()

# Example 1
print(solution.countArrangement(2)) # Expected Output: 2

# Example 2
solution = Solution()
print(solution.countArrangement(3)) # Expected Output: 3

# Example 3
solution = Solution()
print(solution.countArrangement(4)) # Expected Output: 8