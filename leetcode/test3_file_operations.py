def update_server_config(file_path:str, key:str, value:str):

    # Reading config file & storing content in list 
    with open(file_path,'r') as file:
        list_of_lines = file.readlines()

    # Writing the config in the specific line
    with open(file_path,'w') as file:
        for line in list_of_lines:
            if(key in line):
                file.write(key+"="+value+'\n')
                print("Config updated successfully!!")
            else:
                file.write(line)


# update_server_config(r"C:\Users\naveen.raj.s\Downloads\New folder\server.conf","PORT","443")
update_server_config(r"C:\Users\naveen.raj.s\Downloads\New folder\server.conf","MAX_CONNECTIONS","1000")