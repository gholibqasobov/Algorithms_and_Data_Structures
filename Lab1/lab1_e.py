boris = [int(card) for card in input().split()]
nursik = [int(card) for card in input().split()]

count = 0

while count < 10**6:
    if len(boris) != 0:
        boris_card = boris.pop(0)

    else:
        print('Nursik', count)
        break
    if len(nursik) != 0:
        nursik_card = nursik.pop(0)
    else:
        print('Boris', count)
        break

    if boris_card == 0 and nursik_card == 9:
        boris.append(boris_card)
        boris.append(nursik_card)
    elif nursik_card == 0 and boris_card == 9:
        nursik.append(boris_card)
        nursik.append(nursik_card)
    elif boris_card > nursik_card:
        boris.append(boris_card)
        boris.append(nursik_card)
    else:
        nursik.append(boris_card)
        nursik.append(nursik_card)

    count += 1
else:
    print(' blin nichya')
