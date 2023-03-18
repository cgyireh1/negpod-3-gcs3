#!/usr/bin/python3
class TwoSum:
    def __init__(self, list1, target):
        self.list1 = list1
        self.target = target

    def solution(self):
        length = len(list1)

        for i in range(length - 1):
            for j in range(i + 1, length):
                if list1[i] + list1[j] == self.target:
                    new_list = i, j
                    return list(new_list)
        return -1


list1 = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    list1.append(ele)

target = int(input("enter a target: "))
print("the list is : ", list1)
print("target is :", target)

obj = TwoSum(list1, target)
print_tuples = tuple(obj.solution())
print("Expected Output", print_tuples)

