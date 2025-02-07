import utime as time
import machine
import network
import rp2

def set_country(country):
    assert country, "country can't be void"
    rp2.country(country)

def connect(ssid, password, max_wait = 20):
    assert ssid, "ssid can't be void"
    assert password, "password can't be void"
    assert max_wait>0, "max_wait must be positive non-zero"
    led = machine.Pin("LED", machine.Pin.OUT)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        led.toggle()
        time.sleep(1)

    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('network connection failed with error: ' + str(wlan.status()))
    else:
        print('connected')
        status = wlan.ifconfig()
        return wlan

