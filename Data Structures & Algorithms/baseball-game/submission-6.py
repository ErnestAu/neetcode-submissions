

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        newops = []
        for i in range(len(operations)):
            if  operations[i] == "+":
                newops.append(newops[-1] + newops[-2])
            elif operations[i] == "C":
                newops.pop()
            elif operations[i] == "D":
                newops.append(newops[-1] * 2)
            else:
                newops.append(int(operations[i]))
        return sum(newops)