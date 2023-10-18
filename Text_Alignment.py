n = int(input())
txt = "H"
#Head
for a in range(1,n*2,2):
    print((txt*a).center((n*2)," "))
#upper body
for b in range(1,n+2):
    print((txt*n).center(n*2).rstrip(),(txt*n).rjust((4*n-1)))
#body center
for c in range((n//2)+1):
    print((((txt*n)).center(n*2)).rstrip()+(txt*(4*n)).center(n))
#Leg
for d in range(1,n+2):
    print((txt*n).center(n*2).rstrip(),(txt*n).rjust((4*n-1)))
#Head down
for e in reversed(range(1,n*2,2)):
    print((" "*n).center((n*2)),(txt*e).center(n*2).rjust(4*n-1))
