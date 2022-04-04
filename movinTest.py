import ctypes, sys
#檢測當前程式是不是管理員模式
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    #你要執行的主程式
    import mouse
    import time 
    # Code of your program here
    mouse.move(100, 100, absolute=False, duration=0)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)