import subprocess

def du(path):
    info_file = subprocess.check_output(['du', '--time', '-sb', path])
    info_file = info_file.decode('utf-8').split()
    datatime = info_file[1] + ' ' + info_file[2]
    name = info_file[3].split('/')[-1]
    size = '{:0.2f} Kb'.format(float(info_file[0]) / 1024)
    return datatime, name, size
if __name__ == "__main__":
    datatime, name, size = du('d:/VOLANDEMORT/1Лабораторна.docx')
    print(datatime, name, size)
    
# import subprocess

# info_files = subprocess.check_output(["du", "--time", "-sb", "d:/VOLANDEMORT/1Лабораторна.docx"])
# info_files = info_files.decode("utf-8").split("\n")
# for i in range(len(info_files) - 1):
#     info_file = info_files[i].split()
#     datatime = info_file[1] + " " + info_file[2]
#     name = info_file[3].split("/")[-1]
#     size = "{:0.2f} Kb".format(float(info_file[0]) / 1024)
#     print(datatime, name, size)    