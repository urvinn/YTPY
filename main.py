import requests
import os
import platform

os.system("cls||clear")
header = """
======================================

>  SIMPLE PYTHON YOUTUBE DONWLOADER  
>  ONLY FOR WINDOWS OPERATING SYSTEM 

========= [ Created By Vinn ] ========\n"""
print(header)
operating = platform.system()
if operating == "Windows":
    link = input("Input Link Youtube : ")
    type = input("Download Type mp3/mp4 : ")
    link2 = f"https://zekais-api.herokuapp.com/yt{type}?apikey=MNVjaY58&url={link}"
    res = requests.get(link2)
    data = res.json()
    status = f"{data['status']}"
    print(status)
    if status == "200":
        os.system("cls||clear")
        print(header)
        print(f"JUDUL     : {data['title']}")
        print(f"CHANNEL   : {data['channel']}")
        print(f"FILE SIZE : {data['size']}")
        print(f"LINK DOWN : {data['result']}")
        tanya = input("\nDownload Now ? (Y/N) ")
        if tanya == "Y":
            os.system(f"start {data['result']}")
        if tanya == "y":
            os.system(f"start {data['result']}")
        else:
            print("Thank You...")
    else:
        os.system("cls||clear")
        print(header)
        print(f"ERROR : {data['message']}") 
else:
    print("This Script Only Can be Used On Windows Platform")
