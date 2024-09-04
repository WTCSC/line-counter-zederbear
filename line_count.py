def line_count():
    file = open('file.txt', 'r')
    lines = file.readlines()
    return len(lines)
