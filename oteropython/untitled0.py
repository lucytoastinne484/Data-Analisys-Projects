#task automation pyprogram#
import time
import schedule
import webbrowser

def openNuinvest():
    webbrowser.open("https://www.nuinvest.com.br/")


open_nuinvest = schedule.every().day.at("10:07:00")


while True:
    schedule.run_pending()


