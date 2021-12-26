import binascii

f = open('πάσο.png', 'rb')
def printk(k, m):
    s = ''
    count = 0
    for i in k:
        s = s + str(i) + m
        count+=1
        if count%16==0:
            s=s + '\n'

    if s[-1] != '\n':
            s = s + '\n'
    print(s)       
byte = f.read(1)
L=[]
l=[]
while byte != b"":
    x = binascii.b2a_hex(byte) #μετατροπή bytes σε δεκαεξαδικούς χαρακτήρες του ascii
    a = str(x) 
    b = a.upper()           #μετατροπή των χαρακτήρων σε string, κεφαλαιοποίηση  των 'γραμμάτων' και ταξινόμηση τους σε λίστα
    L.append(b[2:4])
    byte = f.read(1)
for i in range (len(L)):
    c = L[i]
    d = int(c,16)
    e = chr(d)
    l.append(e)
    

printk(L, ' ')
printk(l, '')
f.close()


