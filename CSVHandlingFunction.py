import os
import csv

#Function that list create list of CSV file path that contain 'name' parameter in give directory path
def getCSVFilesPath(input_path:str or os.path, name:str):
    files_list = []
    #Looping in given directory path append CSV files that name contain str in parameter 'name' path to list
    for file in os.listdir(input_path):
        if file.endswith("csv") and name in file:
            read_file = os.path.join(input_path, file)
            files_list.append(read_file)

    return files_list

#Function that read and copy array of data from target CSV file in form of list
def getDataArray(file:os.path,col_target:int, row_target:int, arr_width:int, arr_height:int):
    row_iter = 0
    height_iter = 0
    data_arr = []
    line_read = []

    with open(file, "r", encoding="utf-8-sig") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row_iter >= row_target:
                if height_iter < arr_height:
                    for col in range(col_target, col_target+arr_width):
                        line_read.append(row[col])
                    data_arr.append(line_read)
                height_iter += 1
            row_iter += 1
            line_read = []

    return data_arr

#Function looping read array of data from files path list and write to Output CSV fil. return looping files.
def loopDiggingArray(files_list:list, col_target:int, row_target:int, arr_width:int, arr_height:int):
    script_path = os.path.dirname(os.path.realpath(__file__))
    file_count = 0
    #looping get data from files using getDataArray function and write output files
    with open(os.path.join(script_path,"ArrayDigger Output.csv"),"w", newline= '') as output_file:
        csv_writer = csv.writer(output_file)
        for file in files_list:
            datainfile = getDataArray(file, row_target, col_target, arr_width, arr_height)
            csv_writer.writerows(datainfile)
            file_count += 1
        output_file.close()
    
    return int(file_count)

