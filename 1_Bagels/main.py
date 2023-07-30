def main():
    max_digit = 3
    max_attempts = 10

    print(">>> start")
    while True:
        secret_num = get_secret_num(max_digit)
        attempts = 1
        while attempts <= max_attempts:
            try_ = ''
            while len(try_) != max_digit or not try_.isdecimal():
                print(f">>> {attempts}")
                try_ = input(">>> ")
                if len(try_) != max_digit:
                    print(">>> ONLY DIGIT", "*" * max_digit, "SIZE")
            clues = get_clues(try_, secret_num)
            print(clues)
            attempts += 1

            if try_ == secret_num:
                break
            if attempts > max_attempts:
                print(f">>> You lose. Num is {secret_num}")
        print(">>> again? (yes/no)")
        if not input(">>> ").lower().startswith("y"):
            break
    print(">>> LOSER!!!")


def get_secret_num(max_d):
    from random import shuffle
    nums = list(range(10))
    shuffle(nums)
    s_num = ""
    for i in range(max_d):
        s_num += str(nums[i])
    return s_num


def get_clues(num, s_num):
    if num == s_num:
        return "WELL DONE"

    lst = []

    for i in range(len(num)):
        if num[i] == s_num[i]:
            lst.append("Fermi")
        elif num[i] in s_num:
            lst.append("Pico")
    if not len(lst):
        return "Bagels"
    else:
        lst.sort()
        return " ". join(lst)


if __name__ == '__main__':
    main()
