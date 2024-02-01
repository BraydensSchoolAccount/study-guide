# Study Guide
# Brayden Towner
# 02/01/2024

# Yes, joey valence & brae counts as one. look it up
bad_musicians_i_like = ["ajr", "machine girl", "vertigoway", "joey valence & brae"]
print(f"My favorite musicians are {", ".join(bad_musicians_i_like)}")
more_bad_musicians_i_like = bad_musicians_i_like.copy()
more_bad_musicians_i_like.insert(2, "hkmori")
more_bad_musicians_i_like.sort()
print(f"Oops forgot one lol: {", ".join(more_bad_musicians_i_like)}")

names = ["John", "Abraham", "Sally", "Mary", "Carol"]

for i in names:
    print(f"The first letter of {i} is {i[0]}")

numbers = [3, 4, 5, 5, 12, 13, 5, 8, 7, 4, 5]
print(f"There are {numbers.count(5)} fives in the following list: {numbers}")
new_numbers = numbers.copy()
new_numbers.remove(5)
new_numbers.remove(5)
print(f"If you remove the first 2 fives in the list, it has {len(new_numbers)} elements")
