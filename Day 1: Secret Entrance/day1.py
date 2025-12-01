def count_zero_results(move_list, dial_position, dial_numbers):
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


def count_zero_clicks(move_list, dial_position, dial_numbers):
    zero_clicks_couter = 0
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

        if dial_position <= 0:
            zero_clicks_couter = zero_clicks_couter + (dial_position // (dial_numbers*-1))
            if int(number) != (int(dial_position) * -1):
                zero_clicks_couter = zero_clicks_couter + 1

        elif dial_position >= 100:
            zero_clicks_couter = zero_clicks_couter + (dial_position // dial_numbers)
        
        dial_position = dial_position%dial_numbers

    return zero_clicks_couter

def import_data(file_path):
    with open(file_path, 'r') as file:
        move_list = file.read().splitlines()
    return move_list

def main():
    dial_start_position = 50
    modulo_operator = 100

    rotation_list = import_data("Day 1: Secret Entrance/puzzle_input.txt")
    print(count_zero_results(rotation_list, dial_start_position, modulo_operator))
    print(count_zero_clicks(rotation_list, dial_start_position, modulo_operator))


if __name__ == "__main__":
    main()