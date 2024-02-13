import pyautogui as pyauto
import runpy as run

def DataInput():
    pyauto.moveTo(x=280,y=750,duration=5)
    pyauto.click(x=280,y=750,interval=0,button='left',duration=0)
    pyauto.moveTo(x=220,y=600,duration=5)
    pyauto.click(x=220,y=600,interval=0,button='left',duration=0)
    pyauto.typewrite('Hello',interval=0)
    pyauto.typewrite(['enter'],interval=0)
    
    
    
def Process ():
    pass


def Output():
    pass
    