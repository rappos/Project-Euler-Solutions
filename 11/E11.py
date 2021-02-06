def get_grid(filename):
    str_grid = []
    with open(filename, 'r') as f:
        for row in f.readlines():
            str_grid.append(row.strip().split(" "))
    grid = []
    for row in str_grid:
        temp = []
        for item in row:
            temp.append(int(item))
        grid.append(temp)
    return grid


def sum_row(grid):
    summa = 0
    return summa


def main():
    grid = get_grid("grid.txt")


if __name__ == '__main__':
    main()
