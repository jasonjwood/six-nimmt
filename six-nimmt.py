
hand = []
table = []

point_values = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1, 10: 3,
                11: 5, 12: 1, 13: 1, 14: 1, 15: 2, 16: 1, 17: 1, 18: 1, 19: 1, 20: 3,
                21: 1, 22: 5, 23: 1, 24: 1, 25: 2, 26: 1, 27: 1, 28: 1, 29: 1, 30: 3,
                31: 1, 32: 1, 33: 5, 34: 1, 35: 2, 36: 1, 37: 1, 38: 1, 39: 1, 40: 3,
                41: 1, 42: 1, 43: 1, 44: 5, 45: 2, 46: 1, 47: 1, 48: 1, 49: 1, 50: 3,
                51: 1, 52: 1, 53: 1, 54: 1, 55: 7, 56: 1, 57: 1, 58: 1, 59: 1, 60: 3,
                61: 1, 62: 1, 63: 1, 64: 1, 65: 2, 66: 5, 67: 1, 68: 1, 69: 1, 70: 3,
                71: 1, 72: 1, 73: 1, 74: 1, 75: 2, 76: 1, 77: 5, 78: 1, 79: 1, 80: 3,
                81: 1, 82: 1, 83: 1, 84: 1, 85: 2, 86: 1, 87: 1, 88: 5, 89: 1, 90: 3,
                91: 1, 92: 1, 93: 1, 94: 1, 95: 2, 96: 1, 97: 1, 98: 1, 99: 5, 100: 3,
                101: 1, 102: 1, 103: 1, 104: 1}




def read_state():
    global hand
    global table

    with open('state.txt', 'r') as state_file:
        lines = state_file.readlines()

    # Parse hand
    hand = lines[1].replace('\n', '').split(' ')

    # Parse table rows
    table = []
    for i in range(4, 8):
        table.append(lines[i].replace('\n', '').split(' '))

    assert (len(table) == 4)


def probability_row_gets_replaced():
    # - Is anyone likely to replace given the board state?
    # - Is this the row that would be chosen?
    # - What if I am intentionally making the play to pickup a row
    # TODO: Implement
    return 0

def most_likely_stat_value_on_replacement():
    # TODO: Get more sophisticated later
    return 10


def total_points_in_a_row(row):
    points = 0
    for c in row:
        #TODO: Adapt this to factor in the points on each card
        points += 1

    return points


CUR_VAL = 0
PROB_REPLACED = 1
MOST_LIKELY_REPLACEMENT = 2


def expected_value(card):

    # TODO: Factor in number of points per card

    # What are the odds that each row gets replaced?
    for r in range(0, 4):



        row_active_cards[r] = [table[r][len(table[r])-1], 0, 0]



        #Is it the best choice to replace?
        #Is it a low enough cost to replace at all?

        # What are the odds that if the row gets replaced that my play will be lowest (thus taking the row)
       # Get the set of numbers that could be played if each row were replaced (bounded by 1 to lowest number active elsewhere, minus all numbers visible)
        #If my card is the lowest in the set, the odds are 100% I take it.  If higher than the highest, 0%.  Interpolate between.

    # What are the odds that I take each row








def choose_card_to_play():
    # For each card in hand, determine expected value of playing each card
    lowest_expected_value = 999
    lowest_expected_value_card = None
    for card in hand:
        this_ev = expected_value(card)
        if this_ev < lowest_expected_value:
            # Ties go to the lower card, which we'll examine first
            lowest_expected_value = this_ev
            lowest_expected_value_card = card

    print('Play: ', lowest_expected_value_card, '    (Expected Value = ', lowest_expected_value)


def main():
    # Loop for duration of one deal of the deck
    while True:
        input('Press enter when state.txt is populated...')

        read_state()

        choose_card_to_play()

        # Possibilities:
        #   - For each card in hand, determine expected value of playing each card
        #   - Expert system to decide


main()
