
import math
class Card:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite

def biCo(n, r):
    return (math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))

def holeProb(card1, card2):
    num_of_players = 3
    remaining_cards = 52
    remaining_cards = remaining_cards - (2*num_of_players)

def pairprob(card1:Card, card2):
    probs = {}
    isPair = False
    if card1.value == card2.value:
        probs["set_or_better"] = (1 - biCo(48, 3) * (1/biCo(50, 3)) )
        probs["quads"] = (48 * (1/biCo(50, 3)))
        probs["overpair_or_better"] = (biCo(46 -((13 - card1.value)*4), 3) * (1/biCo(50, 3)))

    if card1.suite == card2.suite:
        probs["flush"] = (biCo(11, 3)*(1/biCo(50,3)))   
        probs["flush_draw"] = 39 * biCo(11, 2)*(1/biCo(50, 3))
        probs["backdoor_flush_draw"] = (biCo(39, 2)*11*(1/biCo(50, 3))) 

    else:
        probs["quads"] = (2*(1/biCo(50, 3)))
        probs["full_house"] = (2* biCo(3, 2)*biCo(3, 1)*(1/biCo(50, 3)))
        probs["trips"] = 2*6*44*(1/biCo(50, 3))
        probs["two_pair"] = 3*3*44*1/(biCo(50, 3))
        probs["one_pair"] = (1-biCo(44, 3) * (1/biCo(50, 3)))
    print(probs)

first_card = Card(10, "S")
second_card = Card(10, "S")

pairprob(first_card, second_card)


# set -> 3 of a kind made by pocket pair + 1 card in flop
# overpair -> 


