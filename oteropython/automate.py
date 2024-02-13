#task automation pyprogram#
import time
import schedule
import webbrowser

def openNuinvest():
    webbrowser.open("https://www.nuinvest.com.br/")


open_nuinvest = schedule.every(10).seconds.do(openNuinvest())


while True:
    schedule.run_pending()
    time.sleep(1)


