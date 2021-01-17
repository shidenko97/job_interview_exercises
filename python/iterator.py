class Card:
    """Object in iterator"""

    SUITS = ("HEARTS", "DIAMONDS", "CLUBS", "SPADES",)
    INDEXES = (2, 3, 4, 5, 6, 7, 8, 9, 10, "JACK", "QUEEN", "KING", "ACE",)

    def __init__(self, *, suit, index):
        if suit not in self.SUITS or index not in self.INDEXES:
            raise ValueError(f"{index} of {suit} is incorrect card")

        self.suit = suit
        self.index = index

    def __eq__(self, other):
        return str(self) == str(other)

    def __repr__(self):
        return f"{self.index} of {self.suit}"


class CardContainer(list):
    """Iterator"""

    def __next__(self):
        return next(self)


class Deck:
    """Iterable object"""

    def __init__(self):
        self._cards = CardContainer()

    def add_card(self, *, card: Card):
        if card in self._cards:
            raise ValueError(f"{card} already in deck")

        self._cards.append(card)

    def remove_card(self, *, card: Card):
        if card not in self._cards:
            raise ValueError(f"{card} not present in deck")

        self._cards.remove(card)

    def __iter__(self):
        return iter(self._cards)

    def __repr__(self):
        return ", ".join(map(str, self._cards))


if __name__ == "__main__":
    deck = Deck()

    deck.add_card(card=Card(suit="HEARTS", index=10))

    try:
        deck.add_card(card=Card(suit="HEARTS", index=10))
    except ValueError as err:
        print(err)

    deck.add_card(card=Card(suit="HEARTS", index=9))
    deck.remove_card(card=Card(suit="HEARTS", index=10))

    try:
        deck.remove_card(card=Card(suit="HEARTS", index=10))
    except ValueError as err:
        print(err)

    deck.add_card(card=Card(suit="HEARTS", index=10))

    print(f"Deck contains: {deck}")

    for card in deck:
        print(f"Current card: {card}")
