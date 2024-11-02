import subprocess
import time
import os
import signal

def run_airodump(interface, bssid=None, channel=None, duration=10):
    command = [
        "sudo", "airodump-ng", interface,
        "--write-interval", "1", "--output-format", "csv", "--write", "scan_output"
    ]
    if bssid:
        command.extend(["--bssid", bssid])
    if channel:
        command.extend(["--channel", str(channel)])

    # Start the airodump-ng process
    process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for the specified duration
    time.sleep(duration)

    # Terminate the process after the duration
    process.send_signal(signal.SIGINT)
    process.wait()  # Ensure the process exits before proceeding
    print("Scan completed. Parsing results...")

def parse_csv_output():
    networks = []
    try:
        with open("scan_output-01.csv", "r") as file:
            lines = file.readlines()

        # Parse networks from the CSV file
        for line in lines[2:]:  # Skip header rows
            fields = line.split(',')
            if len(fields) >= 14 and fields[0].strip():  # Check if it's a valid BSSID line
                network_info = {
                    "BSSID": fields[0].strip(),
                    "First Seen": fields[1].strip(),
                    "Last Seen": fields[2].strip(),
                    "Channel": fields[3].strip(),
                    "Speed": fields[4].strip(),
                    "Privacy": fields[5].strip(),
                    "Cipher": fields[6].strip(),
                    "Authentication": fields[7].strip(),
                    "Power": fields[8].strip(),
                    "ESSID": fields[13].strip(),
                }
                networks.append(network_info)

    except FileNotFoundError:
        print("Output file not found. Ensure airodump-ng is producing output.")

    return networks

# Run the scan and parse results
run_airodump("wlan0", duration=10)  # Adjust duration as needed
network_results = parse_csv_output()

# Print results
for network in network_results:
    print(f"BSSID: {network['BSSID']}, ESSID: {network['ESSID']}, Channel: {network['Channel']}, "
          f"Privacy: {network['Privacy']}, Power: {network['Power']}")

