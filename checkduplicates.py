n=int(input())
nums=list(map(int,input().split()))
arr=set(tuple(nums))
if len(nums)==len(arr):
    print("false")
else:
    print("true")
