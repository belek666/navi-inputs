import serial, time, uinput, os

# ==== Keyboard buttons configurations ====
device = uinput.Device([
        uinput.KEY_NEXTSONG,
        uinput.KEY_PREVIOUSSONG,
        uinput.KEY_UP,
        uinput.KEY_DOWN,
        uinput.KEY_ESC,
        uinput.KEY_LEFT,
        uinput.KEY_RIGHT,
        uinput.KEY_PLAYPAUSE,
        uinput.KEY_VOLUMEUP,
        uinput.KEY_VOLUMEDOWN,
        uinput.KEY_ENTER,
        uinput.KEY_M,
        uinput.KEY_SPACE,
    ])

ser = serial.Serial()
ser.baudrate = 19200
ser.port = '/dev/serial0'
ser.timeout = 0.01
ser.open()

while True:
    msg = ser.readline()
    msg = msg.decode("utf-8", "ignore")
 
    if "NAVI" in msg:
        pressed = msg[-1] == "1"
        if "NAVI_LEFT" in msg:
            device.emit(uinput.KEY_PREVIOUSSONG, pressed)
        elif "NAVI_UP" in msg:    
            device.emit(uinput.KEY_UP, pressed)
        elif "NAVI_RIGHT" in msg:
            device.emit(uinput.KEY_NEXTSONG, pressed)
        elif "NAVI_DOWN" in msg:
            device.emit(uinput.KEY_DOWN, pressed)
        elif "NAVI_PLUS" in msg:
            device.emit(uinput.KEY_VOLUMEUP, pressed)
        elif "NAVI_MINUS" in msg:
            device.emit(uinput.KEY_VOLUMEDOWN, pressed)
        elif "NAVI_RETURN" in msg:
            device.emit(uinput.KEY_ESC, pressed)
        elif "NAVI_MODE" in msg:
            device.emit(uinput.KEY_M, pressed)
        elif "NAVI_SCROLL_RIGHT" in msg:
            device.emit_click(uinput.KEY_RIGHT)
        elif "NAVI_SCROLL_LEFT" in msg:
            device.emit_click(uinput.KEY_LEFT)
        elif "NAVI_SCROLL_PRESS" in msg:
            device.emit(uinput.KEY_ENTER, pressed)
        elif "NAVI_AS" in msg:
            device.emit(uinput.KEY_SPACE, pressed)
        elif "NAVI_TURN_OFF" in msg:
            os.system('sudo poweroff')
        print(msg)

            