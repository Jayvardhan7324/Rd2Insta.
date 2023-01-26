import praw
import requests
import os
import time
from prawcore.exceptions import Forbidden
import pyautogui
from time import sleep


reddit = praw.Reddit(client_id='client_id',
                     client_secret='client_secret',
                     user_agent='useragent')

upload_every = "X_SECONDS"

profile_1 = "https://www.instagram.com/profile_name_1/"
profile_2 = "https://www.instagram.com/profile_name_2/"
profile_3 = "https://www.instagram.com/profile_name_3/"

captions_profile_1 = "Adding Captions for profile 1"
captions_profile_2 = "Adding Captions for profile 2"
captions_profile_3 = "Adding Captions for profile 3"


subreddit_name_1 = "subreddit_name"
folder_1 = r"path"

subreddit_name_2 = "subreddit_name"
folder_2 = r"path"

subreddit_name_3 = "subreddit_name"
folder_3 = r"path"

#declaring cords for pyautogui mouse
create_icon_cords = "x, y"
select_from_computer_cords = "x, y"
open_image_computer_cords = "x, y"
next_image_1_cords = "x, y"
next_image_2_cords = "x, y"
adding_captions_cords = "x, y"
share_cords = "x ,y"
url_bar_cords = "x, y"

while True:
    
    subreddit = reddit.subreddit(subreddit_name_1)
    for submission in subreddit.new(limit=1):
        if submission.url.endswith('.jpg') or submission.url.endswith('.png') or submission.url.endswith('.gif'):
            response = requests.get(submission.url)
            file_name = submission.url.split("/")[-1]
            open(os.path.join(folder_1, file_name), "wb").write(response.content)

    subreddit = reddit.subreddit(subreddit_name_2)
    for submission in subreddit.new(limit=1):
        if submission.url.endswith('.jpg') or submission.url.endswith('.png') or submission.url.endswith('.gif'):
            response = requests.get(submission.url)
            file_name = submission.url.split("/")[-1]
            open(os.path.join(folder_2, file_name), "wb").write(response.content)

    subreddit = reddit.subreddit(subreddit_name_3)
    for submission in subreddit.new(limit=1):
        if submission.url.endswith('.jpg') or submission.url.endswith('.png') or submission.url.endswith('.gif'):
            response = requests.get(submission.url)
            file_name = submission.url.split("/")[-1]
            open(os.path.join(folder_3, file_name), "wb").write(response.content)

    print(">>>>>DOWLADED IMAGES")
    
    print(">>>>>GETTING LATEST IMAGES FROM THE FOLDER")

    folder_path_1 = r"path_for_folder_1"
    files = os.listdir(folder_path_1)
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path_1, x)))
    latest_image_1 = os.path.join(folder_path_1, image_files[-1])
    print(latest_image_1)

    folder_path_2 = r"path_for_folder_2"
    files = os.listdir(folder_path_2)
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path_2, x)))
    latest_image_2 = os.path.join(folder_path_2, image_files[-1])
    print(latest_image_2)

    folder_path_3 = r"path_for_folder_3"
    files = os.listdir(folder_path_3)
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path_3, x)))
    latest_image_3 = os.path.join(folder_path_3, image_files[-1])
    print(latest_image_3)

    print(">>>>>GOT LATEST IMAGES FOLDERS PROCEDING TO UPLOAD")
    print(">>>>>UPLOADING IMAGES TO INSTAGRAM")
    
    #INSTAGRAM FIRST PROFILE
    pyautogui.hotkey('ctrl','shift','g')
    time.sleep(2)
    pyautogui.hotkey('alt','tab')
    time.sleep(5)
    pyautogui.typewrite(profile_1)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(create_icon_cords) #click on create icon
    time.sleep(2)
    pyautogui.click(select_from_computer_cords) #click on select from computer
    time.sleep(2)
    pyautogui.typewrite(latest_image_1) #latest image path 
    time.sleep(2)
    pyautogui.click(open_image_computer_cords) #click on open image 
    time.sleep(2)
    pyautogui.click(next_image_1_cords) #click on next image 1
    time.sleep(2)
    pyautogui.click(next_image_2_cords) #click on next image 2
    time.sleep(2)
    pyautogui.click(adding_captions_cords) #click on caption
    time.sleep(2)
    pyautogui.typewrite(captions_profile_1) #caption text
    time.sleep(2)
    pyautogui.click(share_cords) #click on share button
    time.sleep(2)
    pyautogui.hotkey('ctrl','r') #reload page
    time.sleep(2)
    
    print(">>>>>IMAGE UPLOADED TO FIRST INSTAGRAM PROFILE")

    pyautogui.click(url_bar_cords) #click on url bar
    time.sleep(2)   

    #INSTAGRAM SECOND USER
    pyautogui.typewrite(profile_2)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(create_icon_cords) #click on create icon
    time.sleep(2)
    pyautogui.click(select_from_computer_cords) #click on select form computer
    time.sleep(2)
    pyautogui.typewrite(latest_image_2) #latest image path
    time.sleep(2)
    pyautogui.click(open_image_computer_cords) #click on open image
    time.sleep(2)
    pyautogui.click(next_image_1_cords) #click on next image 1
    time.sleep(2)
    pyautogui.click(next_image_2_cords) #click on next image 2
    time.sleep(2)
    pyautogui.click(adding_captions_cords) #click on captions
    time.sleep(2)
    pyautogui.typewrite(captions_profile_2) #caption text 
    time.sleep(2)
    pyautogui.click(share_cords) #click on share button
    time.sleep(2)
    pyautogui.hotkey('ctrl','r') #reload page
    time.sleep(2)

    print(">>>>>IMAGE UPLOADED TO SECOND INSTAGRAM PROFILE")
    
    pyautogui.click(url_bar_cords) #click on url bar
    time.sleep(2)

    #THIRD THIRD USER
    pyautogui.typewrite(profile_3)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(create_icon_cords) #click in create icon
    time.sleep(2)
    pyautogui.click(select_from_computer_cords) #click on select from computer
    time.sleep(2)
    pyautogui.typewrite(latest_image_3) #latest image path
    time.sleep(2)
    pyautogui.click(open_image_computer_cords) #click on open image
    time.sleep(2)
    pyautogui.click(next_image_1_cords) #click on next image 1
    time.sleep(2)
    pyautogui.click(next_image_2_cords) #click on next image 2
    time.sleep(2)
    pyautogui.click(adding_captions_cords) #click on caption
    time.sleep(2)
    pyautogui.typewrite(captions_profile_3) #caption text
    time.sleep(2)
    pyautogui.click(share_cords) #click share button
    time.sleep(5)
    pyautpgui.hotkey('ctrl','r')
    print(">>>>>IMAGE UPLOADED TO THIRD INSTAGRAM PROFILE")
    
    pyautogui.click(url_bar_cords) #click on url bar
    time.sleep(2)

    pyautogui.hotkey('alt','f4')
    
    print(">>>>>UPLOADED TO ALL ACCOUNTS SUCESSFUL QUITING BROWSWER AND UPLOADING AGAIN IN x SECPONDS")

    time.sleep(upload_every)
