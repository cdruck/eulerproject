def int_to_en_str(n):
    """
    :param n: integer <= 1000
    :return: the litteral English representation of n
    """
    s = str(n)
    if len(s) > 4:
        raise Exception("Works up to 9999 only")

    if s == "1000":
        return "one thousand"

    if len(s) == 3:
        remainder = int_to_en_str(s[1:])
        return int_to_en_str(s[0]) + " hundred" + (" and " + remainder if remainder not in ("", "zero") else "")

    if len(s) == 2:
        if s[0] == '1':  # the "teens"
            return {
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
            }[s]
        remainder = int_to_en_str(s[1:])
        return {
            '0': '',
            '2': 'twenty',
            '3': 'thirty',
            '4': 'forty',
            '5': 'fifty',
            '6': 'sixty',
            '7': 'seventy',
            '8': 'eighty',
            '9': 'ninety',
        }[s[0]] + ("-" if s[0] != '0'  and remainder != "zero" else '') + (remainder if s[1] != "zero" and remainder != "zero" else "")

    if len(s) == 1:
        return {
           '0': 'zero',
           '1': 'one',
           '2': 'two',
           '3': 'three',
           '4': 'four',
           '5': 'five',
           '6': 'six',
           '7': 'seven',
           '8': 'eight',
           '9': 'nine',
        }[s]

def main():
    en = []
    for i in range(1, 1001):
        tmp = int_to_en_str(i)
        print(tmp)
        en.append(tmp)

    print(len(''.join(en).replace(' ', '').replace('-', '')))

main()
