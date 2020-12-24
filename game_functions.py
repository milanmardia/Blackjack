def eval_card_value(card, current_total):
    num = card.split()[0]

    if num = 'Two':
        return 2
    elif num = 'Three':
        return 3
    elif num = 'Four':
        return 4
    elif num = 'Five':
        return 5
    elif num = 'Six':
        return 6
    elif num = 'Seven':
        return 7
    elif num = 'Eight':
        return 8
    elif num = 'Nine':
        return 9
    elif num = 'Ace':
        if (21 - current_total) >= 11:
            return 11
        else:
            return 1
    else:
        return 10
