

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        # for i in range(len(operations)):
        #     if operation[i] = "+":
        #         score += operation[i-1]
        for operation in operations:
            if operation == "+":
                record.append(record[-1] + record[-2])
            elif operation == "D":
                record.append(record[-1]*2)
            elif operation == "C":
                record.pop()
            else:
                record.append(int(operation))
        
        return sum(record)
