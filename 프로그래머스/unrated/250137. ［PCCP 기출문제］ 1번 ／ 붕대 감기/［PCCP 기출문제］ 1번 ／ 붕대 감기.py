def solution(bandage, health, attacks):
    latest = 1
    maxHealth = health
    
    for attack in attacks:
        time = attack[0] - latest
        health += time * bandage[1] + bandage[2] * (time // bandage[0])
        health = min(health, maxHealth)
        
        health -= attack[1]
        latest = attack[0] + 1
        
        if health <= 0:
            return -1
        
    return health