n=int(input())
arr=list(map(int,input().split()))
target=int(input())
end=n-1
left=0
arr.sort()
found=False
while left<end:
    sum=arr[left]+arr[end]
    if sum==target:
        found=True
        break
    elif sum<target:
        left+=1
    else:
        end-=1
if found:
    print("Yes")
else:
    print("No")
