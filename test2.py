

import ctypes, sys

ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

try:
    print(ctypes.windll.shell32.IsUserAnAdmin())
except:
    print("right")
