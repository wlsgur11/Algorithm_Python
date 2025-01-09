def solution(bandage, health, attacks):
    t, x, y = bandage
    cont = 0
    max_health = health
    k = 0
    for i in range(attacks[-1][0] + 1):
        time, damage = attacks[k]
        if time == i:
            k += 1
            health -= damage
            cont = 0
            if health <= 0:
                return -1
        else:
            if health >= max_health:
                health = max_health
            elif cont == t:
                health += x + y
                cont = 0
            else:
                health += x
        print(health, cont)
        cont += 1
    return health