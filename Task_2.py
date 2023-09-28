import arcpy
import os

arcpy.env.workspace = r"D:\Sem 3\Prog_3\assign_3\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists.gdb"

output_folder_path = r"D:\Sem 3\Prog_3\assign_3"

output_text_file = "MajorAttractions_info.txt"

output_file_path = os.path.join(output_folder_path, output_text_file)

print(output_file_path)

file_obj = open(output_file_path, "w")

fc_list = arcpy.ListFeatureClasses("MajorAttractions")

for fc_name in fc_list:
    print(fc_name)

print("--------------------------------")

field_list = arcpy.ListFields("MajorAttractions")
for field in field_list:
    print("Field Name: {},  Type: {}, Length: {}".format(field.name, field.type, field.length))
    file_obj.write("Name: {}, Type: {}, Length: {} \n".format(field.name, field.type, field.length))

    print("--------------------------")
    file_obj.write("-------------------------------\n")
file_obj.close()
print("Process Completed")




