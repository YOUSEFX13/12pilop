import keyboard


def main():
    """
    Simple script to type the content of a file with a pause functionality triggered by the F9 key.
    """
    with open("sui.txt", "r") as file:
        text_content = file.read()

    i = 0
    pauseval = False

    def pause():
        nonlocal pauseval
        pauseval = not pauseval

    def callback(key):
        nonlocal pauseval, i

        if not pauseval:
            try:
                keyboard.send("backspace")
                i += 1
                keyboard.write(text_content[i])
            except IndexError:
                quit()

    keyboard.add_hotkey("F9", lambda: pause())
    keyboard.on_press(callback)
    keyboard.wait()


if __name__ == "__main__":
    main()
