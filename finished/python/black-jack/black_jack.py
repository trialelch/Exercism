"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
FACE_CARDS = 'JQK'




def value_of_card(card: str):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card.isnumeric():
        return int(card)
    if card.lower() == 'a':
        return 1
    return 10
    


def higher_card(card_one: str, card_two: str):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    cards = {value_of_card(card_one) : card_one,
        value_of_card(card_two) : card_two}

    if value_of_card(card_one) == value_of_card(card_two.lower()):
        return (card_one, card_two)

    return cards[max(key for key in cards.keys())]

def value_of_ace(card_one: str, card_two: str):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    cards = (card_one, card_two)
    for card in cards:
        if card.lower() == 'a':
            return 1
    if sum(value_of_card(card) for card in cards) + 11 > 21:
        return 1
    return 11


def is_blackjack(card_one: str, card_two: str):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    cards = (card_one, card_two)
    value_high_ace = []
    for card in cards:
        if card.lower() == 'a':
            value_high_ace.append(11)
        else:
            value_high_ace.append(value_of_card(card))

    return sum(value_high_ace) == 21


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    # if (card_one in FACE_CARDS) and (card_two in FACE_CARDS):
    #     return True
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    amount_cards = sum(value_of_card(card)\
        for card in [card_one, card_two])
    return (amount_cards >= 9) and (amount_cards <= 11)
