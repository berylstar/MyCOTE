def solution(bandage, health, attacks):
    latest = 1
    maxHealth = health
    
    for attack in attacks:
        time = attack[0] - latest
        health = min(health + time * bandage[1] + bandage[2] * (time // bandage[0]), maxHealth)
        
        health -= attack[1]
        
        if health <= 0:
            return -1
        
        latest = attack[0] + 1
        
    return health