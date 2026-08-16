from tcp_parser import TCPHeader
from udp_parser import UDPHeader
from icmp_parser import ICMPHeader

def format_packet(parsed: dict) -> str:

    src_ip = parsed["src_ip"]
    dst_ip = parsed["dst_ip"]

    if isinstance(parsed["transport"], TCPHeader):
        tcp = parsed["transport"]

        src_port = tcp.src_port
        dst_port = tcp.dst_port
        flags_list = tcp.flags_list

        return f"{src_ip} -> {dst_ip} TCP {flags_list} src_port={src_port} dst_port={dst_port}"

    if isinstance(parsed["transport"], UDPHeader):
        udp = parsed["transport"]

        udp_length = udp.udp_length
        src_port = udp.src_port
        dst_port = udp.dst_port

        return f"{src_ip} -> {dst_ip} UDP {udp_length} src_port={src_port} dst_port={dst_port}"

    if isinstance(parsed["transport"], ICMPHeader):
        icmp = parsed["transport"]

        icmp_type = icmp.icmp_type

        return f"{src_ip} -> {dst_ip} ICMP [{icmp_type}]"

    if parsed["transport"] is None:

        return f"{src_ip} -> {dst_ip} unknown"