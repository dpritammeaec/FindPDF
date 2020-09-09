arr1=[1,2,3,4]
arr2=[5,6,7,8]

file_1="check.txt"
op_file=open("check.txt","w")

for i in arr1:
    op_file.write("%d\n"%i)

op_file.close()

final_file="final.txt"
sec_file=open("final.txt","w")

file_arr=[line for line in open(file_1).readlines()]
str_i=""
for j in range(0, len(arr2)):
    str_i="%s,%s"%(str(file_arr[j]).rstrip("\n"),str(arr2[j]))
    sec_file.write(str_i+"\n")
    str_i=""

sec_file.close()