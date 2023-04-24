# ░ ▒ ▓ █
def draw(w, h):
    for i in range(h):
        for j in range(w):
            if j == 0 or j == w - 1:
                print(f"█", end="")
            elif h >= 3 and 1 <= i < h - 1 and 1 < j < w - 2:
                print(f"▒", end="")
            else:
                print(f"░", end="")
        print("")


# draw(10, 7)

def shift_encode(word):
    str_end = ""
    for letter in word:
        str_end += chr(ord(letter) + 1)
    print(str_end)


def shift_decode(word):
    str_end = ""
    for letter in word:
        str_end += chr(ord(letter) - 1)
    print(str_end)


shift_encode("test")
shift_decode("uftu")
