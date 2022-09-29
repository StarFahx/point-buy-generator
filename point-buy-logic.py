import random

points = 27
stats = [15,14,13,12,11,10,9,8]
pool = []

for x in range(6):
    print("################")
    print("Step:",x)
    print("Points:",points)
    print("Stats:",stats)

    statmap = []

    for stat in stats:
        statmap.append(stat)
    
    print("Stat map:",statmap)

    for stat in statmap:
        if stat == 15 and points < 9:
            stats.remove(stat)
            print("Removing:",stat)
        elif stat == 14 and points < 7:
            stats.remove(stat)
            print("Removing:",stat)
        elif points < stat - 8:
            stats.remove(stat)
            print("Removing:",stat)
    
    print("After stats:",stats)

    print("################")

    if x == 5:
        if points > 8:
            pool.append(15)
            points -= 9
            print("Last stat:",15)
        elif points > 6:
            pool.append(14)
            points -= 7
            print("Last stat:",14)
        elif points > 5:
            pool.append(7 + points)
            print("Last stat:",7 + points)
            points = 1
        else:
            pool.append(8 + points)
            print("Last stat:",8 + points)
            points = 0
    else:

        rand_stat = random.choice(stats)
        print("Random stat:",rand_stat)
        if rand_stat == 15:
            points -= 9
        elif rand_stat == 14:
            points -= 7
        else:
            points -= (rand_stat - 8)
    
        pool.append(rand_stat)

print("################")
print("Post points:",points)

while points > 0:
    print("################")
    print("Points:",points)

    random.shuffle(pool)

    print("Pool:",pool)

    for i, stat in enumerate(pool):
        print("Stat:",stat)
        if stat == 14 and points > 1:
            pool[i] += 1
            points -= 2
            print("14 -> 15")
            print("New stat:",stat)
            break
        elif stat == 13 and points > 1:
            pool[i] += 1
            points -= 2
            print("13 -> 14")
            print("New stat:",stat)
            break
        elif stat < 13:
            print(stat,"->",stat + 1)
            pool[i] += 1
            points -= 1
            print("New stat:",stat)
            break

pool.sort(reverse=True)

print("################")
print("Final pool:",pool)
print("Points",points)

check = 0
for stat in pool:
    if stat == 15:
        check += 9
    elif stat == 14:
        check += 7
    else:
        check += stat - 8

print("Check:",check)