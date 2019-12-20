m=3
n=5
grid = [[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]]
k = 1
hinder=100
MinCost=0
x=0
y=0
# d[i][j]=min(d[i-1][j],d[i][i-1])+1
dic=[[0]*m]*n
print(dic)
while x<n-1 or y<m-1:
	print(x,y)
	if y<m-1:

		if grid[x][y+1]==0:
			dic[x][y+1]=dic[x][y]+1
			print(dic[x][y+1])

		y-=1
	if x<n-1:
		if grid[x+1][y]==0:
			dic[x+1][y]=dic[x][y]+1
			print(dic[x+1][y])

	else:
		x-=1
	x+=1
	y+=1
	dic[x][y]=min(dic[x][y-1],dic[x-1][y])+1
	print(dic[x][y])
	break
# print(dic)
