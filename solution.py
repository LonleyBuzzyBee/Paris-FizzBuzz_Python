

# list that counts to input

# test to count up to input
# numlist = [num for num in nums]

class Fizzbuzz:

    def __init__(self, input):
        self.input = input
    
    def make_numslist(self) -> list:
        nums = list(range(1, int(self.input) + 1))
        return nums

    
    def filter(self) -> list:
        nums = self.make_numslist()

        numlist = [str(num) for num in nums]

        for num in numlist:
            if '3' in num:
                numlist[numlist.index(num)] = "Sorry bitch"
            elif '2' in num:
                numlist[numlist.index(num)] = "That's hot"
            elif '1' in num:
                numlist[numlist.index(num)] = "Loves it P"

        result = ", ".join(numlist)
        return result

    def __repr__(self):
        return self.filter()

Paris = Fizzbuzz(10)
print(Paris)