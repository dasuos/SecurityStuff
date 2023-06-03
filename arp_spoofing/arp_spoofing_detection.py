from scapy.all import sniff
from typing import Any, Final

mapping: Final[dict[str, str]] = {}


def process_packet(packet: Any) -> str | None:
    source_ip: str = packet['ARP'].psrc
    source_mac: str = packet['Ether'].src

    if source_mac not in mapping:
        mapping[source_mac] = source_ip
        return None

    if mapping[source_mac] != source_ip:
        return '{:s} is pretending to be {:s}\n'.format(
            mapping[source_mac],
            source_ip
        )

    return None


sniff(count=0, filter='arp', store=0, prn=process_packet)
