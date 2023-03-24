import random

letter_scores = {
  "E": 1, "A": 1, "I": 1, "O": 1,
  "N": 1, "R": 1, "T": 1, "L": 1,
  "S": 1, "U": 1, "D": 2, "G": 2,
  "B": 3, "C": 3, "M": 3, "P": 3,
  "F": 4, "H": 4, "V": 4, "W": 4,
  "Y": 4, "K": 5, "J": 8, "X": 8,
  "Q": 10, "Z": 10
}

letter_count = {
  "E": 12, "A": 9, "I": 9, "O": 8,
  "N": 6, "R": 6, "T": 6, "L": 4,
  "S": 4, "U": 4, "D": 4, "G": 3,
  "B": 2, "C": 2, "M": 2, "P": 2,
  "F": 2, "H": 2, "V": 2, "W": 2,
  "Y": 2, "K": 1, "J": 1, "X": 1,
  "Q": 1, "Z": 1
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def create_bag_of_tiles(alphabet:str) -> list:
    """returns a bag of tiles"""
    bag_of_tiles = []
    for letter in alphabet:
        for _ in range(letter_count[letter]):
            bag_of_tiles.append(letter)
    return bag_of_tiles

bag_of_tiles = create_bag_of_tiles(alphabet)

def calc_score(s:str)->int:
    """returns score for a list of tiles"""
    tot_score = 0
    for letter in s:
        cap_letter = letter.upper()
        tot_score += letter_scores[cap_letter]
    return tot_score

def assign_7_tiles(bag_of_tiles:list)->list:
    """returns 7 tiles at random from bag of tiles
    and removes tiles from the bag"""
    tiles =[]
    for _ in range(7):
        tile = random.choice(bag_of_tiles)
        tiles.append(tile)
    return tiles

print(assign_7_tiles(bag_of_tiles))




