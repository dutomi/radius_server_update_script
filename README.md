# radius_server_update_script
This is a simple Netmiko script to update raidus server configuration settings on some cisco switches. 
The Cisco device IP & hostname are compiled in a csv file: cisco_list_edit.csv 
The configuration commands would be loaded from a text file: command_file.txt
I tried to run this script. I am getting a NetmikoTimeoutException error. 
I logged into the switches manually and I can see the commands in the running config, but not in the startup config (show archive configuration differences)
I included "do copy run start" as part of the commands list as seen in the code, but I still get the same errror. 
My goal is to be able to save this commands to the startup config, not just the running-config. I would also like someway to get confirmation that my code was completed successfully, which is why I added the line: print("Radius server update completed for {}".format(row[1]))

Thank you. 
