import pywifi
import time
from pywifi import const

def scan_available_networks(interface_name='wlan0'):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Use the first wireless interface, change if needed
    
    iface.scan()
    scan_results = iface.scan_results()

    networks = []
    for result in scan_results:
        ssid = result.ssid
        bssid = result.bssid
        signal_strength = result.signal
        networks.append((ssid, bssid, signal_strength))
    
    return networks

def connect_to_wifi(ssid, password, interface_name='wlan0'):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Use the first wireless interface, change if needed
    iface.disconnect()
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    # iface.remove_all_network_profiles()
    temp_profile = iface.add_network_profile(profile)
    iface.connect(temp_profile)
    # Wait for connection to establish (adjust as needed)
    connected = False
    for _ in range(10):
        if iface.status() == const.IFACE_CONNECTED:
            connected = True
            break
        # pywifi.sleep(1)
        time.sleep(1)
    return connected

# def main():
#     available_networks = scan_available_networks()
#     print("Available networks:")
#     for ssid, bssid, signal_strength in available_networks:
#         print(f"SSID: {ssid}, BSSID: {bssid}, Signal Strength: {signal_strength} dBm")
#     ssid = input("Enter the WiFi SSID: ")
#     password = input("Enter the WiFi password: ")
#     if connect_to_wifi(ssid, password):
#         print("Connected to WiFi successfully!")
#     else:
#         print("Failed to connect to WiFi.")

# if __name__ == "__main__":
#     main()