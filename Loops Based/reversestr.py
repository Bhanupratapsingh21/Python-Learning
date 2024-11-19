def reverse(name):
    name2 = ""
    for i in range(len(name) - 1, -1, -1):  # Start from last index, stop at -1, step backwards
        name2 += name[i]  # Print characters without a newline
    return name2
