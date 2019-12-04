def maryreverse(input_text): 
  reversed_text = ""    # declare a varable
  for i in input_text:   # looping through input
    reversed_text = i + reversed_text   # reverse the order of text starting with empty text
  return reversed_text   # return reversed text
  
input_text = input("Enter Text: ")
  
print ("You entered: ") 
print (input_text)
  
print ("The reversed text is: ") 
print (maryreverse(input_text))
