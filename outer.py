with open('./requirements.txt','r') as requirements_text:
    required = requirements_text.read().split("\n")
print(required)

for element in required:
    
    print(isinstance(element,str),":" ,element)