import os
import time
import datetime
import sys
import getpass

username = getpass.getuser()
today = time.strftime("%m/%Y").replace("/","-")
create_sorted_folder_command = "mkdir /home/"+username+"/Desktop/Sorted-Files-"+today
create_subfolders_command = "mkdir /home/"+username+"/Desktop/Sorted-Files-"+today+"/photos /home/"+username+"/Desktop/Sorted-Files-"+today+"/videos /home/"+username+"/Desktop/Sorted-Files-"+today+"/documents /home/"+username+"/Desktop/Sorted-Files-"+today+"/songs /home/"+username+"/Desktop/Sorted-Files-"+today+"/archives /home/"+username+"/Desktop/Sorted-Files-"+today+"/others /home/"+username+"/Desktop/Sorted-Files-"+today+"/folders"
os.system(create_sorted_folder_command)
os.system(create_subfolders_command)
if(len(sys.argv)<=1):
    output = os.popen("ls /home/"+username+"/Desktop").read()
    files = output.splitlines()
    for file_name in files:
        file_name = file_name.replace(" ","\ ")
        file_name = file_name.replace("(","\(")
        file_name = file_name.replace(")","\)")
        formatted_name = file_name.split(".")
        if(len(formatted_name) == 1):
            if(formatted_name[len(formatted_name)-1] != "Sorted-Files-"+today and "Sorted-Files-" not in formatted_name[len(formatted_name)-1] ):
                os.system("mv /home/"+username+"/Desktop/"+formatted_name[len(formatted_name)-1]+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/folders")
        else:
            extention =formatted_name[len(formatted_name)-1]
            if(extention == "png" or extention == "jpg" or extention == "jpeg" or extention == "svg"):
                os.system("mv /home/"+username+"/Desktop/"+file_name+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/photos/"+file_name)
            elif(extention == "mkv" or extention == "mp4"):
                os.system("mv /home/"+username+"/Desktop/"+file_name+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/videos/"+file_name)
            elif(extention == "mp3"):  
                os.system("mv /home/"+username+"/Desktop/"+file_name+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/songs/"+file_name)            
            elif(extention == "doc" or extention == "docx" or extention=="pdf" or extention=="txt"):
                os.system("mv /home/"+username+"/Desktop/"+file_name+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/documents/"+file_name)
            elif(extention == "zip" or extention == "rar" or extention == "tar"):
                os.system("mv /home/"+username+"/Desktop/"+file_name+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/archives/"+file_name) 
            else:
                os.system("mv /home/"+username+"/Desktop/"+file_name+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/others/"+file_name)
else:
    for url in sys.argv:
        output = os.popen('ls '+url).read()
        files = output.splitlines()
        for file_name in files:
            file_name = file_name.replace(" ","\ ")
            file_name = file_name.replace("(","\(")
            file_name = file_name.replace(")","\)")
            formatted_name = file_name.split(".")
            if(len(formatted_name) == 1):
                if(formatted_name[len(formatted_name)-1] != "Sorted-Files-"+today and "Sorted-Files-" not in formatted_name[len(formatted_name)-1] ):
                    os.system("mv "+url+"/"+formatted_name[len(formatted_name)-1]+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/folders")
            else:
                extention =formatted_name[len(formatted_name)-1]
                if(extention == "png" or extention == "jpg" or extention == "jpeg"):
                    os.system("mv "+url+"/"+file_name+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/photos/"+file_name)
                elif(extention == "mkv" or extention == "mp4"):
                    os.system("mv "+url+"/"+file_name+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/videos/"+file_name)
                elif(extention == "mp3"):  
                    os.system("mv "+url+"/"+file_name+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/songs/"+file_name)            
                elif(extention == "doc" or extention == "docx" or extention=="pdf"):
                    os.system("mv "+url+"/"+file_name+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/documents/"+file_name)
                elif(extention == "zip" or extention == "rar"):
                    os.system("mv "+url+"/"+file_name+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/archives/"+file_name) 
                else:
                    os.system("mv "+url+"/"+file_name+" /home/"+username+"/Desktop/Sorted-Files-"+today+"/others/"+file_name)
        
    
