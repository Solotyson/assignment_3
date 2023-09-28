import arcpy

arcpy.env.workspace = r"D:\Sem 3\Prog_3\assign_3\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists.gdb"

feature_class_list = arcpy.ListFeatureClasses()
print(feature_class_list)

for fc in feature_class_list:
    desc_obj = arcpy.Describe(fc)
    shape_type = desc_obj.shapeType

    if shape_type == "Point":
        buffer_distance = "400 feet"
    elif shape_type == "Polyline":
        buffer_distance = "1500 feet"
    elif shape_type == "Polygon":
        buffer_distance = "800 feet"

    Output_buffer = fc + "_Buffer"
    arcpy.analysis.Buffer(fc, Output_buffer, buffer_distance)

print("process complete")