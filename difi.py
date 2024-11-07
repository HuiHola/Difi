import time
from modules import sudowifi
from pywifi import PyWiFi, const, Profile
from modules import showbanner
import climanu
import subprocess
import os
import csv

Error = "[ \033[91mERROR\033[0m ]"
Info = "[ \033[92mINFO\033[0m ]"
Worn = "[ \033[93mWorn\033[0m ]"
banner=showbanner.showbanner()
""" this function create manu to show on terminal """
def makeManu(title, console_text,context,option):
    try :
        os.system("clear")
        banner.showbanner()
        mymanu=climanu.SimpleManu()
        mymanu.setManu(options=option,title=title,console_text=console_text,context=context)
        mymanu.showManu()
    except KeyboardInterrupt:
        print("\033[91mexit...\033[0m")
        #os.system("rm -rf *.csv")
    return mymanu

""" show all connected Devices from selected_bssid """
def show_conncted_station(interface,selcted_bssid):
    swifi = sudowifi.SudoWifi() # All function are created on sudowifi
    stations_mac = swifi.scan_with_bssid(interface,selcted_bssid) # this scan all devices which is connected to selcted bssid
    stations_options=[] # create empty array to append manu option
    stations_options.append("All") # app first option
    ''' here we grab (station mac/connected devices mac) and iner to manu option '''
    for stataion in stations_mac:
        stations_options.append(stataion['Station MAC'])
    stations_options.append("re-scan")
    stations_options.append("back")
    
    ''' check if no devices is connected and not in manu if devices is 0 or note then it's redirct to past manu '''
    if(len(stations_options) > 3):
        selcted_device=makeManu("Devices","Select","Select Device for Deauth Attack",stations_options).getUserinput()
        if(selcted_device == 're-scan'):
            show_conncted_station(interface,selcted_bssid) # run rescan command
        elif(selcted_device == 'back'):
            networks_array=swifi.scan_live_networks(interface)
            show_scan_wifi(networks_array,interface)
        elif(selcted_device == 'All'):
            swifi.deauth(interface,selcted_bssid,is_all=True)
        else:
            swifi.deauth(interface,selcted_bssid,selcted_device)
    else:
        print("\033[91mNo devices found. redirct to AP manu\033[0m")
        time.sleep(3)
        networks_array=swifi.scan_live_networks(interface)
        show_scan_wifi(networks_array,interface)
''' this function show scan wifi '''
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
        scan_result_array = swifi.scan_live_networks(interface)
        show_scan_wifi(scan_result_array,interface)
    elif(user_network_input.getUserinput() == 'back'):
        list_wifi_interfaces()
    else : 
        show_conncted_station(interface,scan_result_array[user_network_input.getUserinputIndex()]['BSSID'])


''' it grep and show how many interface available and ask to select one '''
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
    scan_result_array = swifi.scan_live_networks(user_input_interface.getUserinput())
    show_scan_wifi(scan_result_array,user_input_interface.getUserinput())

def start():
    banner.showbanner()
    list_wifi_interfaces()
#List Wi-Fi interfaces
try : 
    start()
except Exception as e:
    if(e.args[0]==2):
        print(f"\033[0m{Worn} \033[93mNo interface found.\033[0m")
        print(f"{Info} \033[92mPlug the wifi Adapter.")
