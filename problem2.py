
def roman_to_decimal(rom):
    sum = 0
    roman_vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(rom) - 1):
        left = rom[i]
        right = rom[i + 1]
        if roman_vals[left] < roman_vals[right]:
            sum -= roman_vals[left]
        else:
            sum += roman_vals[left]
    sum += roman_vals[rom[-1]]
    return sum

if __name__ == '__main__':
    print(roman_to_decimal("III"))
    print(roman_to_decimal("IV"))
    print(roman_to_decimal("IX"))
    print(roman_to_decimal("LVIII"))
    print(roman_to_decimal("MCMXCIV"))
