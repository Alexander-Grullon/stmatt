
g=-9.81
k=0
h=40
start=-2
end=2
for seconds in range(start,end+1):
    height=g*seconds**2+k*seconds+h
    height=round(height,2)
    print("("+str(seconds)+","+str(height)+")")
