def solve_puzzle(move_list, dial_position, dial_numbers):
    zero_couter = 0
    for items in move_list:
        # Indexing the first element
        first_char = items[0]
        # Slicing to get everything after the first Element
        number  = items[1:]

        if first_char == "L":
            dial_position = dial_position - int(number)
        elif first_char == "R":
             dial_position = dial_position + int(number)
        else:
            print("Illegal Operation")

        dial_position = dial_position%dial_numbers

        if dial_position == 0:
            zero_couter = zero_couter + 1

    return zero_couter


def import_data(file_path):
    with open(file_path, 'r') as file:
        move_list = file.read().splitlines()
    return move_list

def main():
    dial_start_position = 50
    modulo_operator = 100

    rotation_list = import_data("Day 1: Secret Entrance/puzzle_input.txt")
    print(solve_puzzle(rotation_list, dial_start_position, modulo_operator))



if __name__ == "__main__":
    main()