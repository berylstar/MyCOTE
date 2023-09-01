def solution(answers):
    student = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    score = [0,0,0]
    
    for i, answer in enumerate(answers):
        for j in range(3):
            score[j] += int(answer == student[j][i % len(student[j])])
        
    return [i + 1 for i in range(len(score)) if score[i] == max(score)]