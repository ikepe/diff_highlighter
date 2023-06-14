from colorama import Fore, Style

def highlight_diff(str_a, str_b):
    min_len = min(len(str_a), len(str_b))
    same_chars = 0
    for i in range(min_len):
        if str_a[i] != str_b[i]:
            print(Fore.RED + str_b[i] + Style.RESET_ALL, end='')
        else:
            print(str_b[i], end='')
            same_chars += 1
    if len(str_b) > min_len:  # In case str_b is longer than str_a
        print(Fore.RED + str_b[min_len:] + Style.RESET_ALL, end='')
    return same_chars

def main():
    print("文字列Aを入力してください:")
    str_a = input()
    print("文字列Bを入力してください:")
    str_b = input()

    print("\n差分を表示します\n")

    print("A:", str_a)
    print("\n")
    print("B: ", end='')
    same_chars = highlight_diff(str_a, str_b)

    print()

    print(f"\nA: {len(str_a)}文字")
    print(f"B: {len(str_b)}文字")
    print(f"先頭{same_chars}文字まで一致しました")

if __name__ == "__main__":
    main()
