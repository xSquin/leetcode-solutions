class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        left, right = 0, 1
        while right < len(asteroids):
            if asteroids[left] > 0 and asteroids[right] < 0:
                if left == 0:
                    if abs(asteroids[left]) > abs(asteroids[right]):
                        asteroids.pop(right)
                    elif abs(asteroids[left]) == abs(asteroids[right]):
                        asteroids.pop(left)
                        asteroids.pop(right-1)
                    else:
                        asteroids.pop(left)
                else:
                    if abs(asteroids[left]) > abs(asteroids[right]):
                        asteroids.pop(right)
                    elif abs(asteroids[left]) == abs(asteroids[right]):
                        asteroids.pop(left)
                        asteroids.pop(right-1)
                    else:
                        asteroids.pop(left)
                    left -= 1
                    right -= 1 
            else:
                right += 1
                left += 1
        return asteroids