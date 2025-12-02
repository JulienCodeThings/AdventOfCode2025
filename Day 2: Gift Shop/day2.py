import csv

def sum_double_nums(id_list):
    sum_bad_id = 0

    for items in id_list:
        x = range(int(items.split("-")[0]), int(items.split("-")[1])+1 ,1)
        for n in x:
          if len(str(n))%2 == 0:
            firstpart, secondpart = str(n)[:len(str(n))//2], str(n)[len(str(n))//2:]
            if firstpart == secondpart:
              sum_bad_id = sum_bad_id + int(n)

    return sum_bad_id


def split_into_equal_chunks(s, n):
    # Split string s into n chunks, distributing remainder from left
    k, m = divmod(len(s), n)
    chunks = []
    start = 0
    for i in range(n):
        end = start + k + (1 if i < m else 0)
        chunks.append(s[start:end])
        start = end
    return chunks


def sum_multiple_x_nums(id_list):
    sum_bad_id = 0

    for items in id_list:
        x = range(int(items.split("-")[0]), int(items.split("-")[1])+1 ,1)
        for id in x:
            for i in range(len(str(id))):
                if i != 0:
                    if len(str(id))%(i+1) == 0:
                        chunks = split_into_equal_chunks(str(id),(i+1))
                        if all(c == chunks[0] for c in chunks):
                            sum_bad_id = sum_bad_id + id
                            break

    return sum_bad_id


def import_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=",")
        id_list = next(reader)
    return id_list

def main():

    id_range_list = import_data("Day 2: Gift Shop/puzzle_input.txt")

    sum_invalid_ids = sum_double_nums(id_range_list)
    print(sum_invalid_ids)

    sum_invalid_ids_x = sum_multiple_x_nums(id_range_list)
    print(sum_invalid_ids_x)

if __name__ == "__main__":
    main()