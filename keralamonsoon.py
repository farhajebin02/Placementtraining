#Kerala, blessed with the Western Ghats and abundant monsoon rains, also witnesses a high number of lightning strikes every year, especially during the pre-monsoon and monsoon seasons. On average, districts like Idukki and Wayanad can record intense lightning activity due to their elevation and cloud dynamics.

#Appu, a young engineer from Kothamangalam, is designing lightning protection for a row of buildings in a hilly town in Kerala. He surveys N buildings arranged from west to east along a narrow road winding through the hills. The peak of building i has coordinates (Xi, Yi), where Xi is the horizontal distance from the western end and Yi is the height from sea level (in meters).

#Appu wants to place lightning rods on top of some buildings. A rod on a building protects that building and all buildings that lie on or under the 45° line of depression both westward and eastward.

#In mathematical terms, a lightning rod on building i protects building j if and only if |Xi − Xj| ≤ Yi − Yj.

#Your task is to help Appu determine the minimum number of lightning rods he needs to install to protect all the buildings in the street.
n=int(input())
cord=[]
for i in range(n):
    x,y=list(map(int,input().split()))
    cord.append((x,y))
stack=[cord[0]]
for i in range(n):
    x1,y1=cord[i]
    x2,y2=stack[-1]
    if abs(x1-x2)<=y1-y2:
        stack.pop()
        stack.append((x1,y1))
    elif abs(x2-x1)<=y2-y1:
        continue
    else:
        stack.append((x1,y1))       
        
print(len(stack))        
