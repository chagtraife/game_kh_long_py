import pyautogui
import time
import cv2
import logging
import numpy as np

# Gets or creates a logger
logger = logging.getLogger(__name__) 

# set log level
logger.setLevel(logging.DEBUG)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)



# screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
# print ("screenWidth:", screenWidth)
# print ("screenHeight:",screenHeight)
# im1 = pyautogui.screenshot('my_screenshot.png')



while 1:
    
    status =  pyautogui.locateOnScreen('game_over.png', confidence=0.9)

    if (status == None):
        # print("IN GAME")
        logger.debug('IN GAME')

        k_log_location = pyautogui.locateOnScreen('k_long.png', confidence=0.8)
        if (k_log_location != None):

            # print ("k_log_location", k_log_location)
            logger.debug(k_log_location)  

            k_log_point = pyautogui.center(k_log_location)
            # print("k_log_point",k_log_point)
            logger.debug(k_log_point)

            bom1 = pyautogui.screenshot('bom1.png',region=(k_log_point.x+100,k_log_point.y-25, 50, 50))
            img = cv2.imread('bom1.png',cv2.IMREAD_GRAYSCALE)
            # img = cv2.imread('bom1.png')
            # cv2.namedWindow("Display check bom")
            # # cv2.resizeWindow("Display 1", 300, 300)
            # cv2.imshow("Display check bom", img)

            



            # img_nobom = cv2.imread('no_bom.png')
            # img_ = cv2.resize(img,(5,5))





            # pyautogui.press('space')
            # if (np.allclose(img1,img_nobom)):
            #     logger.debug("look bom")
            #     pyautogui.press('space')     # Press the space key. All key names are in pyautogui.KEY_NAMES
        




        time.sleep(0.1)
    else:
        # print("OUT GAME")
        logger.debug('OUT GAME')  
        time.sleep(0.5)     

        # k_log_location = pyautogui.locateOnScreen('k_long.png', confidence=0.8)
        # # print ("k_log_location", k_log_location)
        # k_log_point = pyautogui.center(k_log_location)
        # # print("k_log_point",k_log_point)
        # bom1 = pyautogui.screenshot('bom1.png',region=(k_log_point.x+100,k_log_point.y, 30, 30))



        # sleep(0.1)