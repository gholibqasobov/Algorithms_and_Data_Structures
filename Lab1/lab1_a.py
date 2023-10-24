"""
the code is going to run until number of the cards equals to n;
when it equals to, we will move the last element to first place and return it


till then

input:
n - deck



card = n
create a list and add the card in the beginning
card = n-1
add the card in the beginning:
    take the last card in the deck and add to the first
    repeat card times


"""

# inputting the decks


def royal_flush(n):
    deck = []
    card = n
    while len(deck) != n:
        deck.insert(0, card)
        for i in range(card):
            moving_card = deck.pop()
            deck.insert(0, moving_card)
        card -= 1

    return deck


n = int(input())
for i in range(n):
    print(*royal_flush(int(input())))
