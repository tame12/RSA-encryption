list_ASCII = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
              ' ','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',
              '0','1','2','3','4','5','6','7','8','9',
              ':',';','<','=','>','?',"@",
              'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              '[',None,     #backslash giving problems... '\\' may work.?
              ']','^','_','`',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
              '{','|','}','~','\n']
#actuall ASCII dosent have /n at index 0, i added that just to make this program better...

f_public = open("public_key.txt", 'r') #read the keys
keys = f_public.read() #read as string
f_public.close()

keys = keys.split(" ") #make it a list
shared_key = int(keys[0])
public_key = int(keys[1])

f_text = open("text_to_be_encrypted.txt", 'r') #read the text to be encrypted
text = f_text.read()
f_text.close()

output = ""
text = list(text)
for a in range(len(text)): #encrypt it with public key
    index_ASCII = list_ASCII.index(text[a])
    index_encrypted = pow(index_ASCII,public_key,shared_key)
    output += str(index_encrypted) + " "

f_output = open("encrypted_text.txt", 'w') #output in text doc
f_output.write(output)
f_output.close()
