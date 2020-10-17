def get_value(items, key):
    return items.get(key)


def get_keys(items):
    return set(items.keys())


def compare_values(left_file, right_file, key):
    val1 = get_value(left_file, key)
    val2 = get_value(right_file, key)
    if val1 == val2:
        return key
    return (key, val1), (key, val2)


def compare_files(left_file, right_file):
    keys_1 = get_keys(left_file)
    keys_2 = get_keys(right_file)
    plus = keys_2 - keys_1
    minus = keys_1 - keys_2
    intersec = keys_2 & keys_1    
    adjusted_intersec = list(map(lambda x: compare_values(right_file, left_file, x), intersec))
    return plus, minus, adjusted_intersec


def make_compare_file(left_file, right_file):
    plus, minus, adjusted_intersec = compare_files(left_file, right_file)
    output_file_name = "{}_{}.txt".format(left_file, right_file)
    with open(output_file_name, 'a') as output_file:
        output_file.write("{\n")
        for key in minus:
            value = get_value(left_file, key)
            output_file.write(" - {}: {}".format(key, value))
        for key in plus:
            value = get_value(right_file, key)
            output_file.write(" + {}: {}".format(key, value)
        for key in adjusted_intersec:
            if isinstance(key, tuple):
                left_file_key = key[0]
                right_file_key = key[1]
                output_file.write(" - {}: {}".format(left_file_key[0], left_file_key[1])) 
                output_file.write(" + {}: {}".format(right_file_key[0], right_file_key[1)])
            else:
                output_file.write("   {}: {}".format(key, get_value(left_file_key, key)))
        output_file.write("}")
