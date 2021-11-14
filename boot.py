WIFI_CONFIG = [("SSID1","PASS1")
            ,("SSID2","PASS2")
            ,("SSID3","PASS3")]

import utime
import network
import webrepl

def connect_wifi(wifi_config,timeout=10):
    wifi = network.WLAN(network.STA_IF)

    if wifi.isconnected():
        print("connected")
        return

    wifi.active(True)
    print("wifi scan",end=" ")
    scandata = wifi.scan() 

    for scan in scandata:
        for config in wifi_config:
            if(scan[0].decode() == config[0]):
                print(" ssid:" + config[0])
                wifi.connect(config[0], config[1])
                print("TIME: ",end="")
                while not wifi.isconnected() and timeout > 0:
                    print(str(timeout),end=" ")
                    utime.sleep(1)
                    timeout -= 1
                if wifi.isconnected():
                    print("connected") 
                    return wifi 
                else:
                    print("err")     
                    return      
    print("No Wi-Fi")  

webrepl.start(password="")
wifi = connect_wifi(WIFI_CONFIG)



