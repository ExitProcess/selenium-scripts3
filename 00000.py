import sys
zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

seven = ["*******",
         "     * ",
         "    *  ",
         "  ***  ",
         "   *   ",
         "   *   ",
         "   *   "]

digits = [zero, seven]

try:
    digits = sys.argv[0]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = digits[number]
            line += digit[row] + "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: 00000.py <number>")
except ValueError as err:
    print(err, "in", digits)
