student_list = []
if __name__ == '__main__':
    for i in range(int(input())): #prompts user to enter number of students/scores
        name = input()
        score = float(input())
        student_list.append([name,score])
        
student_list.sort(key = lambda x: x[1], reverse = True) #sorts list in descending order based on second element in nested lists.

def second_to_lastf():
    second_to_last = []
    
    if student_list[0][1] == student_list[-1][1]:
        return None
    elif len(student_list) == 2 and student_list[0][1] != student_list[1][1]:
        print(student_list[-1][0])
    else:
        for i in range(len(student_list)):
            if student_list[-2][1] in student_list[i]:
                second_to_last.append(student_list[i][0])
        if len(second_to_last) == 1:
            print(second_to_last[0])
        else:
            second_to_last.sort()
            for i in second_to_last:
                print(i)

second_to_lastf()   



