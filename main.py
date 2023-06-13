from Levenshtein import editops
from colorama import Fore, Style

def print_colored_diff_a(str_a, ops):
    i = 0
    for op in ops:
        while i < op[1]:
            print(str_a[i], end='')
            i += 1
        if op[0] == 'replace' or op[0] == 'delete':
            print(Fore.RED + str_a[i] + Style.RESET_ALL, end='')
            i += 1
    print(str_a[i:], end='')

def print_colored_diff_b(str_b, ops):
    j = 0
    for op in ops:
        while j < op[2]:
            print(str_b[j], end='')
            j += 1
        if op[0] == 'replace' or op[0] == 'insert':
            print(Fore.GREEN + str_b[j] + Style.RESET_ALL, end='')
            j += 1
    print(str_b[j:], end='')

def main():
    print("文字列Aを入力してください:")
    str_a = input()
    print("文字列Bを入力してください:")
    str_b = input()

    print("\n差分を表示します\n")

    ops = editops(str_a, str_b)

    print("A\n", end='')
    print_colored_diff_a(str_a, ops)

    print("\nB\n", end='')
    print_colored_diff_b(str_b, ops)

    print()

if __name__ == "__main__":
    main()
