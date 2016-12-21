
fout = open("output", "w")

with open("syntax", "r") as fin:
    for line in fin:
    	a = line.split('\t')
    	fout.write("insert into TABLE(col1, col2, col3, col4, col5, col6) values(x, '" + str(a[2]) + "', 'y', " + str(a[0]) + ", z, " + str(a[1]) + ");\n")

fin.close()
fout.close()