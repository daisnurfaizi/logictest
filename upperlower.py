# Hello World program in Python
def reverseWordSentence(Sentence): 
  
    # All in One line 
    return ' '.join(word[::-1] for word in Sentence.split(" ")) 
  
# Driver's Code  
Sentence = "Awesome Is Coding"
data = list(reversed(Sentence))
print(data)
listToStr = ''.join([str(elem) for elem in data]) 
print(reverseWordSentence(listToStr)) 
reverse = reverseWordSentence(listToStr)
upperlower =''
count1 = 0
count2 = 0
count3 = 0
for a in reverse: 
# Checking for lowercase letter and converting to uppercase. 
    if (a.isupper()) == True:  
        count1+= 1
        upperlower+=(a.lower()) 
# Checking for uppercase letter and converting to lowercase. 
    elif (a.islower()) == True: 
        count2+= 1
        upperlower+=(a.upper()) 
# Checking for whitespace letter and adding it to the new string as it is. 
    elif (a.isspace()) == True: 
        count3+= 1
        upperlower+= a 
print("In original String : ") 
print("Uppercase -", count1) 
print("Lowercase -", count2) 
print("Spaces -", count3) 

print("After changing cases:") 
print(upperlower) 