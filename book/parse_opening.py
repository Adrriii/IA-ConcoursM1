#!/usr/bin/env python3

# Comme les openings sont pour une grille 8x8, on ajoute 11 à toutes les valeurs pour les faire correspondre à une grille 10x10
# Et comme la board que nous devons utiliser est à l'envers, on inverse horizontalement tout les valeurs.
if __name__ == "__main__":
    from openings import openings
else:
    from book.openings import openings

transformation_table = {
    "a": "8",
    "b": "7",
    "c": "6",
    "d": "5",
    "e": "4",
    "f": "3",
    "g": "2",
    "h": "1",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8"
}

book = dict()

def to_dict(str_move, current_dict):
    if len(str_move) == 0:
        return dict()

    head = str_move[0:2]
    tail = str_move[2:]

    x = transformation_table[head[0]]
    y = transformation_table[head[1]]

    key = x + y
  
    if key not in current_dict.keys():
        current_dict[key] = dict()

    current_dict = current_dict[key]

    return to_dict(tail, current_dict)


def fill_book():
    for moves in openings:
        to_dict(moves, book)
        
def get_book():
    fill_book()

    return book


if __name__ == "__main__":
    print(get_book())