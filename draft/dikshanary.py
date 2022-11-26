# From pypi.org, search for the dictionary module of your choice and follow the instruction that the developer has there.
# Project description
# In-memory Python dictionary of the English language for easy access in NLP applications.

# To my knowledge, this does not exist. Current dictionary packages rely on API calls under the hood, which are obviously extremely slow compared to key lookup.

# Install
# pip install english_dictionary
# Usage
# from english_dictionary.scripts.read_pickle import get_dict
# english_dict = get_dict()

# english_dict["xylophone"]  # english_dict is a Python dictionary of English



from english_dictionary.scripts.read_pickle import get_dict
english_dict = get_dict()

the_word = input('enter an english word to get the meaning: ')

print(english_dict[the_word])
