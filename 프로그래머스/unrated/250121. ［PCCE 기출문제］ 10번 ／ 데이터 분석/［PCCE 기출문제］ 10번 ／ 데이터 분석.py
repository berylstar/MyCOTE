def solution(data, ext, val_ext, sort_by):
    answer = []
    tp = {"code":0, "date":1, "maximum":2, "remain":3}
    
    ext = tp[ext]
    sort_by = tp[sort_by]
    
    for datum in data:
        if datum[ext] < val_ext:
            answer.append(datum)
            
    return sorted(answer, key=lambda x:x[sort_by])