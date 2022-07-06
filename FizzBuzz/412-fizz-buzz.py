class Solution:
    """
        :type n: int
        :rtype: List[str]
    """
    def fizzBuzz(self, n: int) -> List[str]:
        initial_list = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                initial_list.append("FizzBuzz")
            elif i % 3 == 0:
                initial_list.append("Fizz")
            elif i % 5 == 0:
                initial_list.append("Buzz")
            else:
                initial_list.append(str(i))
        return initial_list
