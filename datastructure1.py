ll=[]

ll.append("America")
ll.append("Australia")
ll.append("India")

print("List: ",ll)

choice=0
while choice<5:
    print("1. Add Element")
    print("2. Remove Element")
    print("3. Replace Element")
    print("4. Search Element")
    print("5. Exit")
    ch=int(input("Enter Choice: "))
    if ch==1:
        ele=input('Enter Element: ')
        pos=int(input("Enter Pos Of Element: "))
        ll.insert(pos,ele)
    elif ch==2:
        try:
            ele=input("Enter Element: ")
            ll.remove(ele)
        except ValueError:
            print("Element Not Found")
    elif ch==3:
        ele=input("Enter New Element: ")
        pos=int(input("At what Pos: "))
        ll.pop(pos)
        ll.insert(pos,ele)
    elif ch==4:
        try:
            ele=input("Enter Element: ")
            pos=ll.index(ele)
            print("At Pos ",pos)
        except ValueError:
            print("Not Found!")
    else:
        break
    print("NEw List: ",ll)