from pynput.mouse import Listener

click_times=0
result=""

def clicked(x, y, button, is_press):
    if is_press:
        global click_times
        global result
        result+=str(x)+","+str(y)
        if(click_times==0):
            result+=","
        click_times+=1

listener = Listener(on_click=clicked)

listener.start()

while True:
    if click_times==2:
        listener.stop()
        break

print("("+result+")")