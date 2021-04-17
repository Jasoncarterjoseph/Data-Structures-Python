from stack import Stack

s=Stack()
choice=0
while choice<5:
    print("Stack Operations")
    print("1. Push Element")
    print("2. Pop Element")
    print("3. Peep Element")
    print("4. Search Element")
    print("5. Exit")
    ch=int(input("Enter Choice: "))
    if ch==1:
        ele=input('Enter Element: ')
        s.push(ele)
    elif ch==2:
        ele=s.pop()
        if ele==-1:
            print("Stack Empty")
        else:
            print("Popped Element: ",ele)
    elif ch==3:
        ele=s.peep()
        print("Top Most Elemment: ",ele)
    elif ch==4:
        ele=input("Enter Element: ")
        pos=s.search(ele)
        if pos==-1:
            print("Stack Empty")
        elif pos==-2:
            print("Not Found!")
        else:
            print("Found at Pos: ",pos)        
    else:
        break
    print("Stack",s.display())