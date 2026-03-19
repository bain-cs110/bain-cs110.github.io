import shutil
import os
import requests
from os import walk

BASE_URL = "https://bain-cs110.github.io/course-files/projects/project2/"

def copy_and_replace(src, dest):
    if os.path.exists(dest):
        os.remove(dest)
    shutil.copy2(src, dest)


def download_a_file(url, file_name):
    file_data = requests.get(url).content
    with open(file_name, "wb") as file:
        file.write(file_data)

# First verify we're in the correct directory
filenames = next(walk("."), (None, None, []))[2]

verify_list = ["install_python_packages.py", "mixtape_maker.py", "restaurant_finder.py", "auto_setup.py"]

for file in verify_list:
    if file not in filenames:
        raise Exception(f"Uh oh. Couldn't find {file}, are you sure you're in the project 2 folder?")

OPTIONS = ["Upgrade yelp.py", "Upgrade audio.py", "Upgrade gui.py", "Upgrade movies.py", "Upgrade twilio.py", "Upgrade ..."]
print("***************")
for i in range(len(OPTIONS)):
    print(i, OPTIONS[i])
print("***************")
user_input = input(
    "What action [0-{}] would you like to perform? ".format(len(OPTIONS)-1))

try:
    option = int(user_input.strip())
except:
    raise Exception("Invalid input! " + user_input)
    
    
if OPTIONS[option] == "Upgrade yelp.py":
    download_a_file(BASE_URL + "apis/yelp.py", "new_yelp.py")
    copy_and_replace("new_yelp.py", "apis/yelp.py")
    print("Updated yelp.py!")


elif OPTIONS[option] == "Upgrade audio.py":
    download_a_file(BASE_URL + "apis/audio.py", "new_audio.py")
    copy_and_replace("new_audio.py", "apis/audio.py")
    print("Updated audio.py!")

elif OPTIONS[option] == "Upgrade gui.py":
    download_a_file(BASE_URL + "apis/gui.py", "new_gui.py")
    copy_and_replace("new_gui.py", "apis/gui.py")
    print("Updated gui.py!")

elif OPTIONS[option] == "Upgrade movies.py":
    download_a_file(BASE_URL + "apis/movies.py", "new_movies.py")
    copy_and_replace("new_movies.py", "apis/movies.py")
    print("Updated movies.py!")
    
elif OPTIONS[option] == "Upgrade twilio.py":
    download_a_file(BASE_URL + "apis/twilio.py", "new_twilio.py")
    copy_and_replace("new_twilio.py", "apis/twilio.py")
    print("Updated twilio.py!")

elif OPTIONS[option] == "Upgrade ...":
    user_input = input("Enter the relative path of the file to update")
    temp_file_name = f"new_{user_input}.py".replace("/", "")
    download_a_file(BASE_URL + user_input, temp_file_name)
    copy_and_replace(temp_file_name, user_input)
    print("Updated", user_input)



