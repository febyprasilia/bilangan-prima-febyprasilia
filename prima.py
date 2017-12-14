print("tugas alpro")
x=int(input("masukkan angka awal: "))
y=int(input("masukkan batas: "))

def bil1(x):
    for a in range (b%c):
	    if (a%x)==1:
	        a=True
	    else:
	        a=False
	    print(a)
for i in range(x,y+1):
    prima=True
    for j in range(2,i):
        if(i%j==0):
            prima=False
    if(prima):
        print(i)
