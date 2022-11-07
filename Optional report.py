import webbrowser
import pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time


#account 1 - ******* / ********
#account 2 - ******* / ********
# ^ 2 nextiva accounts. Account #2 is used in the automation

nextiva_login = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
nextiva_login.set_window_size(1000, 1000)
nextiva_login.set_window_position(800, 25, windowHandle='current')
# ^ Opens nextova windows and sets the window sizes

webbrowser.open("https://docs.google.com/spreadsheets/d/1WbQKONN8P3hfFVttaSS_*****/edit#gid=0")
time.sleep(2)
webbrowser.open("https://docs.google.com/spreadsheets/d/1tFkhYXIqPUihI5qE-******/edit?pli=1#gid=******")
nextiva_login.get("http://cp3.nextiva.com/callcenter")
time.sleep(25)
#  ^ Logs in Google Sheets and opens Nextiva
# Massive delay, to make sure that the raw data sheet opens and loads...

search = nextiva_login.find_element('xpath', '//*[@id="isc_N"]')
time.sleep(3)
search.send_keys("********")
time.sleep(1)
search = nextiva_login.find_element('xpath', '//*[@id="isc_P"]')
time.sleep(1)
search.send_keys("*******")
search.send_keys(Keys.RETURN)
time.sleep(4)
m = nextiva_login.find_element('xpath', '//*[@id="isc_LinkItem_6$20j"]')
m.click()
time.sleep(10)
l = nextiva_login.find_element('xpath', '//*[@id="isc_LinkItem_8$20j"]')
l.click()
time.sleep(5)
nextiva_login.minimize_window()
# ^Opens the Nextiva dashboard and reports tab

pyautogui.click(779, 474)
time.sleep(10)
# ^ Switch to Dashboard

pyautogui.click(1622, 259)
time.sleep(0.5)

pyautogui.click(1622, 280)
time.sleep(0.5)

pyautogui.click(1622, 302)
time.sleep(0.5)

pyautogui.click(1622, 325)
time.sleep(0.5)

pyautogui.click(1622, 347)
time.sleep(3)
# ^clicks the 5 checkboxes of T1, to T5 with the cursor.

# ^ Gets current time.
# start_work = now.replace(hour=8, minute=0, second=0, microsecond=0)
# end_work = now.replace(hour=18, minute=0, second=0, microsecond=0)
# Defines end and start work hours for reporting

while True:
    now = datetime.now()
    # ^ Gets current time.
    x = now.weekday()
    start_work = now.replace(hour=8, minute=0, second=0, microsecond=0)
    end_work = now.replace(hour=18, minute=0, second=0, microsecond=0)
    # Gets day of week as an integer (1,2,3,4...)
    # 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday, 7 = Monday.
    # ^BECAUSE REASONS. TRY ME! I'LL FIGHT YOU!

    timeFormattedToUS = time.strftime("%I:00 %p")
    timeUSFinal = time.time() - 60*60
    timeInThePastFormattedToUS = time.strftime("%I:00 %p", time.localtime(timeUSFinal))
    # ^ Local time now (EST)

    if int(time.strftime('%M')) != 5:
        # ^ Checks if 5 minutes have passed of the hour. Example - id it's 13:05 or 14:05 etc.

        pyautogui.click(779, 474)
        time.sleep(0.5)
        # ^ Switch to Dashboard

        pyautogui.click(779, 474)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        # ^Copies from nextiva

        pyautogui.click(406, 22)
        time.sleep(0.5)
        # ^ Switch to NEW primary queue

        pyautogui.click(102, 242)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        # ^Pastes in Google Sheets
        ################################################
        continue

    # ------------CCCD 9AM - 10AM START __________________________

    pyautogui.click(406, 22)
    time.sleep(2)
    # ^ Switch to NEW primary queue

    pyautogui.click(240, 241)
    time.sleep(2)
    # ^ Sets B2 = TRUE in "Auto update status"

    pyautogui.click(1436, 0)
    time.sleep(2)
    # ^ Switch to reports

    pyautogui.click(1063, 231)
    time.sleep(2)
    # ^ clicks the dropdown menu

    pyautogui.click(1002, 455)
    time.sleep(3)
    # ^ Selects "Call center call detail report"

    pyautogui.click(1530, 357)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('backspace')
    time.sleep(0.5)
    pyautogui.write(f"{timeInThePastFormattedToUS}")
    time.sleep(1)
    # ^ Clicks "Start time" and sets value

    pyautogui.click(1542, 385)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.write(f"{timeFormattedToUS}")
    time.sleep(1)
    # ^ Clicks "End time" and sets value

    pyautogui.click(876, 468)
    time.sleep(7)
    # ^ clicks "Run report"

    pyautogui.click(833, 262)
    pyautogui.click(833, 262)
    pyautogui.click(833, 262)

    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('f5')
    time.sleep(1)
    # Copies info

    pyautogui.click(151, 25)
    time.sleep(5)
    # ^ Selects "Support reporting automation" tab

    pyautogui.click(159, 1021)
    time.sleep(5)
    # ^ Selects "CCCD" Google sheets tab

    pyautogui.click(84, 347)
    time.sleep(2)
    # ^ Selects cell "A6"

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    # ^ Pastes info.

    pyautogui.click(201, 276)
    time.sleep(7)
    # ^ Clicks on "TRANSFER" button to trigger the script

    pyautogui.click(101, 280)
    time.sleep(7)
    # ^ Clicks on "DELETE DATA" button to wipe the data.

    # ------------CCCD 9AM - 10AM END __________________________
    # ------------ACD 9AM - 10AM START __________________________

    pyautogui.click(1063, 231)
    time.sleep(2)
    # ^ clicks the dropdown menu

    pyautogui.click(987, 314)
    time.sleep(3)
    # ^ Selects "Agent call detail report"

    pyautogui.click(1530, 357)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.write(f"{timeInThePastFormattedToUS}")
    time.sleep(1)
    # ^ Clicks "Start time" and sets values

    pyautogui.click(1542, 385)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.write(f"{timeFormattedToUS}")
    time.sleep(1)
    # ^ Clicks "End time" and sets values

    pyautogui.click(886, 481)
    time.sleep(7)
    # ^ clicks "Run report"

    pyautogui.click(833, 262)
    pyautogui.click(833, 262)
    pyautogui.click(833, 262)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('f5')
    time.sleep(1)
    # Copies info from nextiva and refreshes page

    pyautogui.click(151, 25)
    time.sleep(5)
    # ^ Selects "Support reporting automation" tab

    pyautogui.click(246, 1018)
    time.sleep(5)
    # ^ Selects "ACD" Google sheets tab

    pyautogui.click(84, 347)
    time.sleep(2)
    # ^ Selects cell "A6"

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    # ^ Pastes info.

    pyautogui.click(201, 276)
    time.sleep(7)
    # ^ Clicks on "TRANSFER" button to trigger the script

    pyautogui.click(101, 280)
    time.sleep(7)
    # ^ Clicks on "DELETE D08:26 AMATA" button to wipe the data.

    # ------------ACD 9AM - 10AM END __________________________
    # ------------AUR 9AM - 10AM START __________________________

    pyautogui.click(1063, 231)
    time.sleep(2)
    # ^ clicks the dropdown menu

    pyautogui.click(995, 441)
    time.sleep(3)
    # ^ Selects "Agent Unavailability report"

    pyautogui.click(1062, 434)
    time.sleep(2)
    # ^ clicks "Sampling"

    pyautogui.click(938, 486)
    time.sleep(2)
    # ^ clicks "Hourly"

    pyautogui.click(1530, 357)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.write(f"{timeInThePastFormattedToUS}")
    time.sleep(1)
    # ^ Clicks "Start time" and sets values

    pyautogui.click(1542, 385)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.write(f"{timeFormattedToUS}")
    time.sleep(1)
    # ^ Clicks "End time" and sets values

    pyautogui.click(891, 507)
    time.sleep(7)
    # ^ clicks "Run report"

    pyautogui.click(833, 262)
    pyautogui.click(833, 262)
    pyautogui.click(833, 262)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('f5')
    time.sleep(1)
    # Copies info from nextiva and refreshes page

    pyautogui.click(151, 25)
    time.sleep(5)
    # ^ Selects "Support reporting automation" tab

    pyautogui.click(325, 1020)
    time.sleep(5)
    # ^ Selects "ACD" Google sheets tab

    pyautogui.click(84, 347)
    time.sleep(2)
    # ^ Selects cell "A6"

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    # ^ Pastes info.

    pyautogui.click(201, 276)
    time.sleep(7)
    # ^ Clicks on "TRANSFER" button to trigger the script

    pyautogui.click(101, 280)
    time.sleep(7)
    # ^ Clicks on "DELETE DATA" button to wipe the data.

    # ------------ AADR START ------------

    pyautogui.click(1063, 231)
    time.sleep(2)
    # ^ clicks the dropdown menu

    pyautogui.click(991, 264)
    time.sleep(3)
    # ^ Selects "Agent call detail report"

    pyautogui.click(1530, 357)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.write(f"{timeInThePastFormattedToUS}")
    time.sleep(1)
    # ^ Clicks "Start time" and sets values

    pyautogui.click(1542, 385)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.write(f"{timeFormattedToUS}")
    time.sleep(1)
    # ^ Clicks "End time" and sets values

    pyautogui.click(886, 481)
    time.sleep(20)
    # ^ clicks "Run report"

    pyautogui.click(833, 262)
    pyautogui.click(833, 262)
    pyautogui.click(833, 262)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('f5')
    time.sleep(1)
    # Copies info from nextiva and refreshes page

    pyautogui.click(151, 25)
    time.sleep(5)
    # ^ Selects "Support reporting automation" tab

    pyautogui.click(414, 1016)
    time.sleep(1)
    # ^ Clicks the arrow to expose the AADR tab in Google sheets

    pyautogui.click(309, 1017)
    time.sleep(2)
    # ^ Selects "AADR" Google sheets tab

    pyautogui.click(84, 347)
    time.sleep(2)
    # ^ Selects cell "A6"

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    # ^ Pastes info.

    pyautogui.click(201, 276)
    time.sleep(7)
    # ^ Clicks on "TRANSFER" button to trigger the script

    pyautogui.click(101, 280)
    time.sleep(7)
    # ^ Clicks on "DELETE DATA" button to wipe the data.

    pyautogui.click(381, 1016)
    time.sleep(1)
    # ^ Clicks the arrow to expose the CCCD tab in Google sheets

    # ------------ AADR END ------------

    pyautogui.click(406, 22)
    time.sleep(2)
    # ^ Switch to NEW primary queue

    pyautogui.click(240, 241)
    time.sleep(2)
    # ^ Sets B2 = FALSE in "Auto update status"
