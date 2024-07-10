import random
from wordsList import words

chances=7

picked_word= random.choice(words)

blank ="_"* len(picked_word)

print(f"Guess the word: {blank}")
has_chance = True

while has_chance:
  if chances >0:
    if blank == picked_word:
      print("Yaay! You won.")
      break
    user_letter =input("Guess the letter: ")
    
    if user_letter in picked_word:
      letter_pos= picked_word.find(user_letter)
      
      blank_list=list(blank)
      blank_list[letter_pos]=user_letter
      blank= "".join(blank_list)
      
      print(blank)
      print(f"You have {chances} chance left.\n")
    else:
      chances-=1
      print(f"You have {chances} chance left.\n")
  else:
      print("Opps! You ran out of chances.")
      has_chance=False
      
      
    












