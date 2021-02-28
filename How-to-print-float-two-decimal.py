if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    toplam=0
    
    for i in student_marks[query_name]:
        toplam+=i
    
    formatted="{:.2f}".format(toplam/3)
    print(formatted)    
    
