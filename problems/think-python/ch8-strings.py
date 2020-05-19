# Exercise 2
print("banana".count("a"))


# Exercise 3
def is_palindrome(word):
    return word.strip().lower() == word[::-1].strip().lower()


print(is_palindrome("Bob"))
print(is_palindrome("Able was I ere I saw Elba"))
print(is_palindrome("nope"))


# Exercise 5
print(chr((ord("z") - 97) % 26 + 97))


def caesar_cypher(str, rot):
    encrypted = ""
    for c in str:
        if c.isupper():
            encrypted += chr((ord(c) + rot - 65) % 26 + 65)
        else:
            encrypted += chr((ord(c) + rot - 97) % 26 + 97)
    return encrypted


print(caesar_cypher("cheer", 7))
print(caesar_cypher("melon", -10))
