def romanCevir(roman):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    symb = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while roman:
        div = roman // num[i]
        roman %= num[i]
  
        while div:
            print(symb[i], end = "")
            div -= 1
        i -= 1
  
if __name__ == "__main__":
    roman = 16
    print("Roman output:", end = " ")
    romanCevir(roman)