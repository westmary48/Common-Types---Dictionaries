my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    },
    'father': {
      'name':'Ray',
      'age': 79
    }
}

for fam_member, details in my_family.items():
  print(f'{details["name"]} is my {fam_member} and is {str(details["age"])} years old')
