"""Given a string s consisting only of lowercase English letters, return a tuple with the count of vowels and consonants in the string."""

def count_vc(s: str) -> tuple:

  vowels = set("aeiou")

  vowel_count = 0
  consonant_count = 0



  for char in s:
    if char in vowels:
      vowel_count += 1
    else:
      consonant_count += 1

  return vowel_count, consonant_count


print(count_vc("hello there"))
print(count_vc("python"))