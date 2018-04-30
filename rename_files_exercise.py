import os
def rename_files():
    #1 set directory and get files
    currentDir = os.getcwd()
    print('the current directory is:' + currentDir)
    print('')
    print('changing directory ...')
    print('')
    os.chdir(r'C:\Users\a110939\Desktop\Programming\alphabet\message')
    currentDir = os.getcwd()
    print('')
    print('the current directory is:' + currentDir)
    file_list = os.listdir(r'C:\Users\a110939\Desktop\Programming\alphabet\message')
    #2 remove numbers from files
    for file_name in file_list:
        print('current file name: ' + file_name)
        table = file_name.maketrans(dict.fromkeys('0123456789'))
        new_file_name = file_name.translate(table)
        print('new file name: ' + new_file_name)
        print('')
rename_files()
