import time
import pyautogui


# Follow pyautogui.moveTo(x,y) with a pyautogui.dragTo(x,y, button='left') that way it will drag the towers 

# print(pyautogui.size())
screenSize = pyautogui.size()
# print(screenSize[0], screenSize[1])

if ((screenSize[0] == 1920) and (screenSize[1] == 1080)) :
    print("Correct")
    time.sleep(5)
    pyautogui.click(966, 960)
    pyautogui.click(234, 98)
    pyautogui.click(944, 647)
    pyautogui.click(337, 95)
    pyautogui.moveTo(472,963)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(605,688, 0.15)
    pyautogui.mouseUp(button='left')
    pyautogui.click(605,688)
    print("Basic Tower 1 Placed")
    time.sleep(11)
    pyautogui.click(640,483)
    print("Basic Tower Projectile Bounce Bought")
    time.sleep(8.9)
    pyautogui.click(644,436)
    print("Basic Tower Speed Bought")
    time.sleep(9.3)
    pyautogui.click(650,407)
    print("Basic Tower Range Bought")
    time.sleep(8.65)
    pyautogui.click(659,472)
    print("Basic Tower Strength Bought")
    time.sleep(7.6)
    pyautogui.moveTo(472,963)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(611, 631, 0.15)
    pyautogui.mouseUp(button='left')
    print("Basic Tower 2 Placed")
    pyautogui.click(611,631)
    time.sleep(16)
    pyautogui.click(630,425)
    print("Basic Tower Projectile Bounce Bought")
    time.sleep(12.87)
    pyautogui.click(637,381)
    print("Basic Tower Speed Bought")
    time.sleep(7.53)
    pyautogui.click(647,414)
    print("Basic Tower Strength Bought")
    time.sleep(4.4)
    pyautogui.click(644,347)
    print("Basic Tower Range Bought")
    time.sleep(23.1)
    pyautogui.click(635,447)
    print("Basic Tower #2 Bounce 8 Bought")
    pyautogui.click(605,688)
    time.sleep(9.55)
    pyautogui.click(638,504)
    print("Basic Tower #1 Bounce 8 Bought")
    time.sleep(26)
    pyautogui.click(337, 95)
    pyautogui.moveTo(1028,960)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(609, 575, 0.15)
    pyautogui.mouseUp(button='left')
    pyautogui.click(605,688)
    pyautogui.click(611,366)
    pyautogui.click(611,631)
    pyautogui.click(611,310)
    pyautogui.moveTo(1450,960)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(611, 631, 0.15)
    pyautogui.mouseUp(button='left')
    print("Cannon and Ultimate Tower Placed")
    pyautogui.click(337,95)
    pyautogui.click(611,571)
    pyautogui.click(635,350)
    print("Cannon Bigger Explosions Bought")
    # time.sleep()
    # pyautogui.click(638,352)
    # pyautogui.click(3635,952)
    
else:
    print("Commit Sepuku") 

