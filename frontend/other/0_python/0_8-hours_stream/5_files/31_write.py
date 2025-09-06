f = open("materials//6_python//0_8-hours_stream//5_files//t.txt", 'r')

g = open("materials//6_python//0_8-hours_stream//5_files//r.txt", 'w')

x = int(f.readline())
y = int(f.readline())

g.write(str(x+y))
