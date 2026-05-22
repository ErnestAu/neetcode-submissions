# sandwiches order matters


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentCount = Counter(students)
        
        noEat = len(students)

        for sandwich in sandwiches:
            if studentCount[sandwich] == 0:
                return noEat
            studentCount[sandwich] -= 1
            noEat -= 1
        return noEat