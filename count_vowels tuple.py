 
def Check_Vow(string, vowels): 
      
    string = string.casefold() 
    duplicate = 0
    ostring = ""
      
    #count = {}.fromkeys(vowels, 0)  
    for character in string:
       # print(ostring) 
        if character in vowels:
            if character in ostring:
                duplicate +=1
            else:
                ostring +=character
    print((ostring, duplicate)) 
vowels = 'aeiou'
string = "examples are good"
Check_Vow(string, vowels)