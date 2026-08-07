# 0 and 1 sandwiches



class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hashS = [0,0]
        for student in students:
            hashS[student] += 1
        
        for sandwich in sandwiches:
            if hashS[sandwich] > 0:
                hashS[sandwich] -=1
            else:
                return sum(hashS)
        return 0