s=input()
stack=[]
for i in s:
    if i =='{':
        stack.append(i)
    elif i=='}':
        if not stack:
            print("Not Matching")
            break
        stack.pop()
else:
    if not stack:
        print("Matching")
    else:
        print("Not Matching")
