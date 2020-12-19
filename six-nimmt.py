
hand = []
table = []


def read_state():
    global hand
    global table

    with open('state.txt', 'r') as state_file:
        lines = state_file.readlines()

    # Parse hand
    hand = lines[1].replace('\n', '').split('\t')

    # Parse table rows
    table = []
    for i in range(4, 8):
        table.append(lines[i].replace('\n', '').split('\t'))

    assert (len(table) == 4)

    print(table)


def main():
    # Loop for duration of one deal of the deck
    while True:
        # Wait for key to indicate input is ready
        input('Press enter when state.txt is populated...')

        # Read in state
        read_state()

        # Decide which card to play


        # NOTE: Start with no memory of played cards


main()