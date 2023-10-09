# Generate a random haiku

import random

HAIKU_SYLLABLES = [5, 7, 5]

def generate_haiku():
  """Generates a random haiku poem."""

  haiku = []

  for syllable_count in HAIKU_SYLLABLES:
    words = []
    while sum(len(word) for word in words) < syllable_count:
      word = random.choice(["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"])
      words.append(word)

    haiku.append(" ".join(words))

  return haiku

def main():
  haiku = generate_haiku()
  print("\n".join(haiku))

if __name__ == '__main__':
  main()
