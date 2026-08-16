from ip_parser import parse_one_ipv4_header
from tcp_parser import TCPHeader
from udp_parser import UDPHeader
from icmp_parser import ICMPHeader


def parse_packet(data):
    protocol = data[9]
    result = parse_one_ipv4_header(data)

    if protocol == 1:
        result["transport"] = ICMPHeader.from_bytes(data)
    elif protocol == 6:
        result["transport"] = TCPHeader.from_bytes(data)
    elif protocol == 17:
        result["transport"] = UDPHeader.from_bytes(data)
    else:
        result["transport"] = None

    return result