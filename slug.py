#slugify string

def slugify(string):
    return string.lower().strip().replace(' ', '-')
num = slugify("hello world I LOVE YOU  ")
print(num)

# count vowels
def count_vowels(word):
    count = 0
    for char in word:
        if char in 'aeiou':
            count += 1
    return count

num_vowels = count_vowels("hello world")
print(num_vowels)