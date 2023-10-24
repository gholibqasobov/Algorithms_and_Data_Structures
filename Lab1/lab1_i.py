n = int(input())

student_list = [i for i in input()]

while len(student_list) > 1:
    for i in student_list:
        if i == "K":
            rival = ''.join(student_list).find("S")
            student_list.pop(rival)
        elif i == "S":
            rival = ''.join(student_list).find("K")
            student_list.pop(rival)

leader = 'SAKAYANAGI' if ''.join(student_list) == "S" else 'KATSURAGI'
print(leader)
