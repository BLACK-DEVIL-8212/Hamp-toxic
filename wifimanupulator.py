from scapy.all import *

# Define the interface names for the two Wi-Fi cards
normal_iface = "wlan0"
monitor_iface = "wlan1"

# Set the monitor mode on the monitor_iface
os.system("ifconfig {} down".format(monitor_iface))
os.system("iwconfig {} mode monitor".format(monitor_iface))
os.system("ifconfig {} up".format(monitor_iface))

# Sniff packets on the normal interface
def normal_packet_handler(packet):
    # Process packets on the normal interface
    print("Normal Packet:", packet.summary())

# Sniff packets on the monitor interface
def monitor_packet_handler(packet):
    # Process packets on the monitor interface
    print("Monitor Packet:", packet.summary())

# Start packet sniffing on the two interfaces
sniff(iface=normal_iface, prn=normal_packet_handler, store=0)
sniff(iface=monitor_iface, prn=monitor_packet_handler, store=0)
