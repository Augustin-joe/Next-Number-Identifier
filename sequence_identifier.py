def start():
    global a
    global no
    a = []
    print("_"*23)
    print("Enter atleast 5 inputs")
    print("_"*23)
    no =int(input("enter no of inputs:"))
    for i in range(no):

        a.append(int(input(f"enter value{i+1}: ")))

def nextval(next,soln):
    print(f'by {soln} \n the next number is: {next}')

def mul():
    count =0
    j= False
    i=0
    b=0
    while b <= abs(a[1]):
        if a[0]*b ==a[1]:
            j=True
            break
        b+=1
    else:
        b=0
        while b >= -abs(a[1]):
            if a[0]*b ==a[1]:
                j=True
                break
            b-=1
    while i!=no-1 and j:
        if a[i]*b == a[i+1]:
            count +=1
        else:
            j=False
        i+=1
        
    if count ==no-1:
        next=a[no-1]*b
        nextval(next,"multiple")
    
def div():
    count =0
    j= False
    i=0
    for k in range(1,a[1]+1):
        if a[0]/k ==a[1]:
            b=k
            j=True
            break
    while i!=no-1 and j:
        if a[i]/b == a[i+1]:
            count +=1
        else:
            j=False
        i+=1
        
    if count ==no-1:
        next=a[no-1]/b
        nextval(next,"division")
     
def addseq():
    count =0
    j = True
    i=0
    while i !=no-2 and j:
        if a[i]+a[i+1] == a[i+2]:
            count+=1
        else:
            j = False
        i+=1
    if count ==no-2:
        next=a[no-1]+a[no-2]
        nextval(next,"add_sequence")

def subseq():
    count =0
    j = True
    i=0
    while i !=no-2 and j:
        if a[i]-a[i+1] == a[i+2]:
            count+=1
        else:
            j = False
        i+=1
    if count ==no-2:
        next=a[no-2]-a[no-1]
        nextval(next,"sub_sequence")
    
def square(b,k):
    i=0
    j=True
    count=0
    while i!=no and j:
        if b**k==a[i]:
            count+=1
        else:
            j = False
        i+=1
        b+=1
    if count == no:
        next=b**k
        nextval(next,"power")
        
def power():
    
    for i in range(21):
        b=0
        while b<=a[0]:
            if b**i == a[0]:
                x=b
                square(x,i)
            b+=1
                 
def number():
    maximum=abs(a[1]-a[0])
    for i in range(no-2):
        maximum=max(abs(a[i+2]-a[i+1]),maximum)
    n=-maximum
    while n<=maximum:
        r=abs(a[1]-a[0])
        s=-r         
        while s<=r :
            b=s
            i=0
            j=True
            count=0
            while i !=no-1 and j:
                if a[i]+b == a[i+1]:
                    count+=1
                else:
                    j = False
                b+=n
                i+=1
            if count ==no-1:
                next=a[no-1]+b
                nextval(next,"number_high_seq")
                break
            s+=1
        n+=1

def prime():
    count=0
    p=True
    for i in range(2,a[0]):
        if a[0]%i==0:
            p = False
            break
    j=0 
    b=a[0]
    while j< no-1 and p:
        pr=True
        while b<=a[j+1] and pr :
            b+=1
            pr=False
            for i in range(2,b):
                if b%i==0:
                    pr=True
                    break
        
        if pr!= True and b==a[j+1]:
            count +=1
        else:
            p= False
        j+=1    
           
    if count ==no-1:
        c=True
        while c:
            b+=1
            for i in range(2,b):
                c=False
                if b%i==0:
                    c =True
                    break
    
        next=b
        nextval(next,"prime")
        
def prime_low():
    count=0
    p=True
    for i in range(2,a[0]):
        if a[0]%i==0:
            p = False
            break
    j=0 
    b=a[0]
    while j< no-1 and p:
        pr=True
        while b>=a[j+1] and pr :
            b-=1
            pr=False
            for i in range(2,b):
                if b%i==0:
                    pr=True
                    break
        
        if pr!= True and b==a[j+1]:
            count +=1
        else:
            p= False
        j+=1    
           
    if count ==no-1:
        c=True
        while c:
            b-=1
            for i in range(2,b):
                c=False
                if b%i==0:
                    c =True
                    break
    
        next=b
        nextval(next,"prime_down")
         
start()
mul()
div()
addseq()
subseq()
power()
number()
prime()
prime_low()
