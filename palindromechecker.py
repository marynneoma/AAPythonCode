def maryreverse(input_text): 
  reversed_text = ""    # declare a varable
  for i in input_text:   # looping through input
    reversed_text = i + reversed_text   # reverse the order of text starting with empty text
  return reversed_text   # return reversed text
  
input_text = input("Enter Text: ")
  
print ("you entered: ") 
print (input_text)
  
print ("The reversed text is: ") 
print (maryreverse(input_text))

if input_text== maryreverse(input_text):  # Checking if both input_text and maryreverse are equal
  print("True the word is a palindrome")
else:
    print ("False the word is not a palindrome")
