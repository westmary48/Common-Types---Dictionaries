word_definitions = {
  "awesome": "extremely good excellent.",
  "cool": "calmness and composure",
  "nice": "subtle"
  }

# Create an empty dictionary
word_definitions = dict()
# Add k/v pairs
word_definitions["awesome"] = "extremely good excellent"
word_definitions["cool"] = "calmness and composure"
word_definitions["nice"] = "subtle"

word_definitions = {
  "awesome": "extremely good excellent.",
  "cool": "calmness and composure",
  "nice": "subtle"
  }

for (key, value) in word_definitions.items():
    print(f"The definition of {key} is {value}")


idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}


for (key, value) in idioms.items():
     print(f"{key}: {value}")