f = open("materials//6_python//0_8-hours_stream//5_files//t.txt", 'r')

n = 1000
for i in range(n):
  s = f.readline()
  if i == 1:
    x = int(s)
  if i == 2:
    y = int(s)

print(x+y)
