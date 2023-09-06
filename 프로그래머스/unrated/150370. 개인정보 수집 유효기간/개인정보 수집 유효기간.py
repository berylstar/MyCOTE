def Date(s):
    y, m, d = list(map(int, s.split('.')))
    return y*336 + m*28 + d

def Check(today, privacy, d):
    date, tp = privacy.split()
    date = Date(date)
    
    return today >= date + d[tp]

def solution(today, terms, privacies):
    today = Date(today)
    
    d = {term[0] : (int(term[2:]) * 28) for term in terms}
    
    return [i for i, v in enumerate(privacies, start=1) if Check(today, v, d)]