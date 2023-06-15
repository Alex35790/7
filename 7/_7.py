def create_word_set():
  words = input("Enter a list of words separated by commas: ").split(",")
  word_set = set(words)
  return word_set

def count_words():
  words = input("Enter a list of words separated by commas: ").split(",") 
  count = len(words)
  print("Number of words:", count) 

def create_dictionary():
  words = input("Enter a list of words separated by commas: ").split(",") 
  second_list = input("Enter a list of words with the same number of characters: ").split(",") 
  dictionary = dict(zip(words, second_list))
  print(dictionary)
word_set = create_word_set()
count_words()
create_dictionary()
