import pyautogui
import time
import cv2


# screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
# print ("screenWidth:", screenWidth)
# print ("screenHeight:",screenHeight)
# im1 = pyautogui.screenshot('my_screenshot.png')



while 1:
    
    status =  pyautogui.locateOnScreen('game_over.png', confidence=0.9)

    if (status == None):
        print("IN GAME")

        k_log_location = pyautogui.locateOnScreen('k_long.png', confidence=0.8)
        # print ("k_log_location", k_log_location)
        k_log_point = pyautogui.center(k_log_location)
        # print("k_log_point",k_log_point)
        bom1 = pyautogui.screenshot('bom1.png',region=(k_log_point.x+100,k_log_point.y, 10, 10))
        img = cv2.imread('bom1.png',cv2.IMREAD_GRAYSCALE)
        img_ = cv2.resize(img,(5,5))
        




        time.sleep(0.5)
    else:
        print("OUT GAME")  
        time.sleep(0.5)     

        # k_log_location = pyautogui.locateOnScreen('k_long.png', confidence=0.8)
        # # print ("k_log_location", k_log_location)
        # k_log_point = pyautogui.center(k_log_location)
        # # print("k_log_point",k_log_point)
        # bom1 = pyautogui.screenshot('bom1.png',region=(k_log_point.x+100,k_log_point.y, 30, 30))



        # sleep(0.1)