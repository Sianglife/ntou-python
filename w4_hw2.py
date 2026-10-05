mir = {
    'A': 'A',
    'E': '3',
    'H': 'H',
    'I': 'I',
    'J': 'L',
    'L': 'J',
    'M': 'M',
    'O': 'O',
    'S': '2',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': '5',
    '1': '1',
    '2': 'S',
    '3': 'E',
    '5': 'Z',
    '8': '8'
}
# print(len(mir))

def isMirror(s):
    mirrored = []
    for index, char in enumerate(s):
        if char in mir:
            mirrored.append(mir[char])
        else:
            return False

    return mirrored[::-1] == list(s)

def isPalindrome(s):
    return s[::-1] == s

while True:
    try:
        s = input().strip()
    except EOFError:
        break
    s = s.replace("0", "O")

    m = isMirror(s)
    p = isPalindrome(s)

    if m and p:
        print(f"{s} -- is a mirrored palindrome.")
    elif m:
        print(f"{s} -- is a mirrored string.")
    elif p:
        print(f"{s} -- is a regular palindrome.")
    else:
        print(f"{s} -- is not a palindrome.")
    print()
    # print(s, s[::-1], s1, s1[::-1])
