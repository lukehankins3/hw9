

infile = open('info_security.txt','r')
text = infile.read()
words = text.strip()
outfile = open('encrypted.txt','w')

alphabet = {'A':'9', 'a':'#', 'B':'n','b':'/', 'C':'<', 'c':'b', 
'D':'X', 'd':'A', 'E':'!', 'e':'h', 'F':'"', 'f':';', 'G':'[', 'g':'|', 
'H':'l', 'h':'J', 'I':'G', 'i':'@', 'J':'D', 'j':'$', 'K':'%', 'k':'*',
'L':'^', 'l':'&', 'M':'6', 'm':'3', 'N':'`', 'n':'~', 'O':'m', 'o':'_', 
'P':'+', 'p':'?', 'Q':'=', 'q':'Z', 'R':'B', 'r':'F', 'S':'.', 's':',', 
'T':'R', 't':'j', 'U':'1', 'u':'0', 'V':'7', 'v':'U', 'W':'Y', 'w':'8', 
'X':'5', 'x':'4', 'Y':'V', 'y':'i', 'Z':'d', 'z':'g'}

code = ''

for letter in words:
    if letter in alphabet:
        code += alphabet[letter]
    else:
        code += letter
        
outfile.write(code)
outfile.close()