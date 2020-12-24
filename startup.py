def create_deck():
    num_words = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

    deck_of_cards = []

    for suit in suits:
        for num in num_words:
            deck_of_cards.append(num + " of " + suit)
    
    return deck_of_cards
        
