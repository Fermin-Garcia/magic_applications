import random
import pandas as pd

face_cards = ['Jack', 'Queen', 'King', 'Ace']
full_deck = []

number_cards = list(range(2,11))
spade_cards = []
for card_values in number_cards:
    spade_cards.append(f'{card_values} of Spade')
spade_cards
for faces in face_cards:
    spade_cards.append(f'{faces} of Spade')
full_deck.append(spade_cards)


number_cards = list(range(2,11))
heart_cards = []
for card_values in number_cards:
    heart_cards.append(f'{card_values} of Hearts')
spade_cards
for faces in face_cards:
    heart_cards.append(f'{faces} of Hearts')
full_deck.append(heart_cards)


number_cards = list(range(2,11))
club_cards = []
for card_values in number_cards:
    club_cards.append(f'{card_values} of Clubs')
for faces in face_cards:
    club_cards.append(f'{faces} of Clubs')
full_deck.append(club_cards)


number_cards = list(range(2,11))
diamonds_cards = []
for card_values in number_cards:
    diamonds_cards.append(f'{card_values} of Diamonds')
for faces in face_cards:
    diamonds_cards.append(f'{faces} of Diamonds')
full_deck.append(diamonds_cards)


df = pd.DataFrame(full_deck)

def random_card(df):
    import random
    x = random.randint(0,3)
    y = random.randint(0,12)
    
    print(df.iloc[x,y])


random_card(df)