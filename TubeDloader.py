#Import Required Modules
import pytube
from getpass import getpass
import time

#login Credentials
loginCredentials = ["habib", "ytd@habib"]


#Author Information
print(
    """
Name       : TubeDLoader - Youtube Video Downloader.
Author     : Md. nur habib
Email      : thenurhabib@gmail.com
GitHub     : github.com/thenurhabib
HackerRank : hackerrank.com/thenurhabib      
    """
)

#Get Username and Password from user.
getUsername = input("Enter Username : ")
getPassword = getpass("Enter Password :")

#Check Login Inputs
if getUsername == loginCredentials[0] and getPassword == loginCredentials[1]:
    print("\n  Login Successful.")
    print("\n Loading Please Wait...")
    time.sleep(2)
    takeVideoLinkFromUser = input("\nEnter Youtube Video Link : ")
    saveMemoryPath = input("Enter Memory Path to Save The Video : ")
    yt = pytube.YouTube(takeVideoLinkFromUser)
    stream = yt.streams.filter(file_extension="mp4").first()
    stream.download(saveMemoryPath)
    print(f"Successfully Download Your Video In {saveMemoryPath}")
#If User Inter Wrong Login Information.
else:
    print("\nWrong Login Informattion.")
