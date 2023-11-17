import keyboard
import time , os



def typer(text_content):
    i = 0
    pauseval = False

    def pause():
        nonlocal pauseval
        pauseval = not pauseval

    def callback(key):
        nonlocal pauseval, i

        if not pauseval:
            try:
                time.sleep(1e-10)  # Short delay
                keyboard.send("backspace")
                keyboard.write(text_content[i])
                i += 1
            except IndexError:
                os._exit(0)

    keyboard.add_hotkey("F9", lambda: pause())
    keyboard.add_hotkey("F10", lambda: os._exit(0))
    keyboard.on_press(callback)
    keyboard.wait()


