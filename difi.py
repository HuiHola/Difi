import time
from modules import sudowifi
from pywifi import PyWiFi, const, Profile
import climanu
import subprocess
import os
import csv
def makeManu(title, console_text,context,option):
    mymanu=climanu.SimpleManu()
    mymanu.setManu(options=option,title=title,console_text=console_text,context=context)
    mymanu.showManu()
    return mymanu
def checkAndChangeMode(interface):
    try:
        # Run the iwconfig command and suppress output
        result = subprocess.run(
            ["iwconfig", interface],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            text=True
        )
        
        # Check the return code: if 0, the command ran successfully
        if result.returncode == 0:
            # Now, let's check if "Mode:Monitor" is in the output
            # We run it again to get the actual output since we suppressed it above
            result_output = subprocess.run(
                ["iwconfig", interface],
                capture_output=True,
                text=True
            )
            if "Mode:Monitor" in result_output.stdout:
                print("\033[94mmonter mode already started.")
            else:
                print("\033[92starting monitor mode...")
                os.system("sudo iwconfig wlan0 mode monitor")
        else:
            return False
    except Exception as e:
        print(f"Error checking monitor mode for {interface}: {e}")
        return False

def show_conncted_station(interface,selcted_bssid):
    swifi = sudowifi.SudoWifi()
    stations_mac = swifi.scan_with_bssid(interface,selcted_bssid)
    stations_options=[]
    stations_options.append("All")
    for stataion in stations_mac:
        stations_options.append(stataion['Station MAC'])
    stations_options.append("re-scan")
    stations_options.append("back")
    if(len(stations_options) > 3):
        selcted_device=makeManu("Devices","Select","Select Device for Deauth Attack",stations_options).getUserinput()
        if(selcted_device == 're-scan'):
            show_conncted_station(interface,selcted_bssid)
        elif(selcted_device == 'back'):
            pass
        elif(selcted_device == 'All'):
            swifi.deauth(interface,selcted_bssid,is_all=True)
        else:
            swifi.deauth(interface,selcted_bssid,selcted_device)
    else:
        print("\033[91mNo devices found. redirct to AP manu\033[0m")
        time.sleep(3)
        networks_array=swifi.scan_wifi(interface)
        show_scan_wifi(networks_array,interface)
def show_scan_wifi(network_array,interface):
    ''' make available network to show as manu '''
    scan_result_array = network_array
    scan_option_array = []
    for networks in scan_result_array:
        scan_option_array.append(networks['ESSID'])
    scan_option_array.append("re-scan")
    scan_option_array.append("back")
    ''' show manu and get input from user of available networks '''
    user_network_input = makeManu("Access Points","Select","Select Access Point",scan_option_array)
    if(user_network_input.getUserinput() == "re-scan"):
        swifi = sudowifi.SudoWifi()
        scan_result_array = swifi.scan_wifi(interface)
        show_scan_wifi(scan_result_array,interface)
    elif(user_network_input.getUserinput() == 'back'):
        list_wifi_interfaces()
    else : 
        show_conncted_station(interface,scan_result_array[user_network_input.getUserinputIndex()]['BSSID'])
def list_wifi_interfaces():
    ''' Interface access and available interface check '''
    interface_options = []
    wifi = PyWiFi()
    interfaces = wifi.interfaces()  # Get list of Wi-Fi interfaces
    ''' read interface list and add to interface_options '''
    for i, iface in enumerate(interfaces):
        interface_options.append(f"{iface.name()}")
    ''' show interface list on manu '''
    user_input_interface = makeManu("Interfaces","Select","Select Interface",interface_options)
    ''' check and open monitor mode '''
#    checkAndChangeMode(user_input_interface.getUserinput())
    ''' scan network from selcted interface '''
    swifi = sudowifi.SudoWifi()
    scan_result_array = swifi.scan_wifi(user_input_interface.getUserinput())
    show_scan_wifi(scan_result_array,user_input_interface.getUserinput())
#List Wi-Fi interfaces
try : 
    list_wifi_interfaces()
except Exception as e:
    print(e)
    print("\033[92mNo interface found.\033[0m")
# Run the scan and print available networks
#wifi_networks = scan_wifi()
#for network in wifi_networks:
#    print(f"SSID: {network['SSID']}, Signal: {network['Signal']} dBm")

