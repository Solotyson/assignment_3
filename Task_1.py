
file_path = r"D:\Sem 3\Prog_3\assign_3\Taaron ki karli sawaari.txt"

file_obj = open(file_path,'r')

lines = file_obj.readlines()
for S in lines:
    print(S)