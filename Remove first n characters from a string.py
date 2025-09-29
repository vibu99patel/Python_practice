def remove_chars(word, n):
    # write your code
    output = ""
    for ch in word:
        output = word[n:]

    return output


print("Removing characters from a string")
print(remove_chars("pynative", 4))

print(remove_chars("pynative", 2))


