#!/usr/bin/python
from netmiko import ConnectHandler
import getpass
import csv

print("Enter AD password: ")
password = getpass.getpass()


with open('./cisco_list_edit.csv') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  next(reader)
  for row in reader: 
    try:
      net_connect = ConnectHandler(
        device_type='cisco_ios',
        host=row[0],
        username='username',
        password= password
      )
    
      with open('command_file.txt',"r") as f:
        commands = f.readlines()
        commands = [command.strip("\n").strip() for command in commands]
        commands.append("do copy run start")
        output = net_connect.send_config_set(commands)
        print(output)
        net_connect.disconnect()
        print("Radius server update completed for {}".format(row[1]))
        print("\n")

    
    except Exception as err:
      exception_type = type(err).__name__
      print(exception_type)



  
      




