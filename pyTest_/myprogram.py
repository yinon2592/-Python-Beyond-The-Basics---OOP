import sys


def doubleit(x):
    if not isinstance(x, (int, float)):
        raise TypeError
    var = x * 2
    return var

def doublelines(filename):
    with open(filename) as fh:
        new_list = [str(doubleit(int(val))) for val in fh]
        with open(filename, "w") as fh:
            fh.write("\n".join(new_list))

if __name__ == "__main__":     # this lines will be executed just if our file is the main file and not imported one
    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)

    print(f"the value of {input_val} is {doubled_val}")