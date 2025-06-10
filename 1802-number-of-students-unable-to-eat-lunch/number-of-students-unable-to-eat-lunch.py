class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i=0
        while students!=[] and sandwiches!=[]:
            if students[0]==sandwiches[0]:
                i=0
                students.pop(0)
                sandwiches.pop(0)
            else:
                x=len(students)
                i+=1
                l=students[1:x+1]
                l.append(students[0])
                print(l)
                students=l
                if i > x-1:
                    break
        return len(students)