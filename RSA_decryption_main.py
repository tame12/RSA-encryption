list_ASCII = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
              ' ','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',
              '0','1','2','3','4','5','6','7','8','9',
              ':',';','<','=','>','?',"@",
              'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              '[',None,     #backslash giving problems... '\\' may work.?
              ']','^','_','`',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
              '{','|','}','~','\n']
#actuall ASCII dosent have /n at last index, i added that just to make this program better...

f_private = open("private_key.txt", 'r') #read the keys
keys = f_private.read() #read as string
f_private.close()

keys = keys.split(" ") #make it a list
shared_key = int(keys[0])
private_key = int(keys[1])

f_text = open("encrypted_text.txt", 'r') #read the text to be decrypted
text = f_text.read()
f_text.close()

output = ""
text = text.split(" ")
text.pop()

for a in range(len(text)): #decrypt it with private key
    encrypted_index = int(text[a])
    index_ASCII = pow(encrypted_index,private_key,shared_key)
    output += list_ASCII[index_ASCII]

f_output = open("decrypted_text.txt", 'w') #output in text doc
f_output.write(output)
f_output.close()
