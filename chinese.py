#With the introduction of RP and the removal of the O-levels for the Raffles schools, the annual school rankings for both RI and RGS have hit all-time lows, since the only O-level subject left is Mother Tongue. The teachers have decided that drastic action is required, and without considering the welfare of the students have demanded that remedial Higher Chinese lessons be conducted every night. However, if a teacher works above a certain number of minutes 0 < x ≤ 1,000 per day, the school has to pay that teacher overtime pay, at the rate of $100 per extra minute, since Higher Chinese is a particularly tiring and frustrating subject to teach.

#Assume, for just a while, that you're actually trying to help put this nefarious scheme into action. Given a list of the durations (in minutes) of 0 < n ≤ 1,000 day shifts and n night shifts, help to pair up these day and night shifts such that the total amount of overtime pay that the school has to fork out is minimised. Of course, the number of minutes a teacher has to work each day is the sum of the length of his/her day and night shift.

n=int(input())
day=list(map(int,input().split()))
night=list(map(int,input().split()))
minutes=int(input())
pay=0
day.sort()
night.sort(reverse=True)
for i in range(n):
    if day[i]+night[i] > minutes:
        overtime= day[i] + night[i] - minutes
        pay+=overtime*100
print(pay)
