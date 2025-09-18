import random

# Function to create a single card as a tuple (suit, value)
def create_card(suit: str, value: int) -> tuple[str, int]:
    return (suit, value)

# Function to create a full deck of 52 cards
# The deck is represented as a list of tuples (suit, value)
def create_deck() -> list[tuple[str, int]]:
    deck = []
    suits = ["hertta", "risti", "pata", "ruutu"]

    for suit in suits:
        for value in range(2, 15):
            card = create_card(suit, value)
            deck.append(card)
    return deck

# Function to format a card as a string (e.g., "Hertta 2")
def format_card(card: tuple[str, int]) -> str:
    (suit, value) = card
    return f"{suit.capitalize()} {value}"

# Function to print the entire deck, one card per line
def print_deck(deck: list[tuple[str, int]]) -> None:
    for card in deck:
        print(format_card(card))

# Define function "shuffle_deck"
def shuffle_deck(deck: list[tuple[str, int]]) -> list[tuple[str, int]]:
    shuffled = deck.copy()
    random.shuffle(shuffled)
    return shuffled

# Define main
def main():
    original_deck = create_deck()
    print("Alkuperäinen pakka:")
    print_deck(original_deck)
    
    shuffled_deck = shuffle_deck(original_deck)
    print("\nSekoitettu pakka:")
    print_deck(shuffled_deck)

# Start main
if __name__ == "__main__":
    main()