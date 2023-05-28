from scapy.all import sniff

MAPPING = {}

def process_packet(packet):
    source_ip = packet['ARP'].psrc
    source_mac = packet['Ether'].src

    if source_mac in MAPPING.keys():
        if MAPPING[source_mac] != source_ip:
            try:
                old_ip = MAPPING[source_mac]
            except:
                old_ip = 'unknown'
            message = (str(old_ip) + ' is pretending to be ' + str(source_ip) + '\n')
            return message
    else:
        MAPPING[source_mac] = source_ip

sniff(count=0, filter='arp', store=0, prn=process_packet)
