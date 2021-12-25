""" def sum(nums):
    result = 0
    for n in nums:
        return result
        #return 0

#sum_3 = sum([1,2,3])
#print(sum_3)
print(sum([1,2,3]))
assert sum(([1,2,3])) == 6, "Should be 6" """


""" import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main() """

# test case for pytest runner
# Writing the TestSum test case example for pytest would look like this:
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
 
def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"