import random

def get_pools(num):
    points = 27
    stats = [15,14,13,12,11,10,9,8]
    pool = []

    for x in range(6):

        statmap = []
        for stat in stats:
            statmap.append(stat)

        for stat in statmap:
            if stat == 15 and points < 9:
                stats.remove(stat)

            elif stat == 14 and points < 7:
                stats.remove(stat)

            elif points < stat - 8:
                stats.remove(stat)

        if x == 5:
            if points > 8:
                pool.append(15)
                points -= 9

            elif points > 6:
                pool.append(14)
                points -= 7

            elif points > 5:
                pool.append(7 + points)
                points = 1

            else:
                pool.append(8 + points)
                points = 0

        else:
            rand_stat = random.choice(stats)
            if rand_stat == 15:
                points -= 9

            elif rand_stat == 14:
                points -= 7

            else:
                points -= (rand_stat - 8)
        
            pool.append(rand_stat)

    while points > 0:

        random.shuffle(pool)

        for i, stat in enumerate(pool):
            if stat == 14 and points > 1:
                pool[i] += 1
                points -= 2
                break

            elif stat == 13 and points > 1:
                pool[i] += 1
                points -= 2
                break
            
            elif stat < 13:
                pool[i] += 1
                points -= 1
                break

    pool.sort(reverse=True)
    print("Pool #" + str(num) +":",pool)

def ask():
    print("How many pools to generate?")
    num = input()

    if not num.isnumeric():
        "Invalid response"
        ask()

    else:
        for x in range(int(num)):
            get_pools(x + 1)

def main():
    ask()

main()
