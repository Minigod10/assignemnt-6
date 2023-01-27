"""Write a Python class to find the three elements that sum to zero from a set of n real
numbers.
Input array: [-25, -10, -7, -3, 2, 4, 8, 10]
Output: [[-10, 2, 8], [-7, -3, 10]]"""
class SumToZero:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_triplets(self):
        triplets = []
        self.numbers.sort()
        for i in range(len(self.numbers)-2):
            if i > 0 and self.numbers[i] == self.numbers[i-1]:
                continue
            l, r = i+1, len(self.numbers)-1
            while l < r:
                s = self.numbers[i] + self.numbers[l] + self.numbers[r]
                if s == 0:
                    triplets.append([self.numbers[i], self.numbers[l], self.numbers[r]])
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return triplets

# Test the class
numbers = [-25, -10, -7, -3, 2, 4, 8, 10]
s = SumToZero(numbers)
print(s.find_triplets())