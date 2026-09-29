p = input()
rp = " "

for i in reversed (p):
    rp+=i
    

if p != p[::-1]:
    print ("NP")
else:
    print("P")
