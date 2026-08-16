from dataclasses import dataclass

@dataclass
class UDPHeader():

    src_port: int
    dst_port: int
    udp_length: int
    checksum: int
    payload: bytes

    @classmethod
    def from_bytes(cls, data: bytes) -> "UDPHeader":
        ip_ihl = data[0] & 0x0F
        ip_header_length = ip_ihl * 4
        udp_data = data[ip_header_length:]

        if len(udp_data) < 8:
            raise ValueError("UDP header is too short")

        src_port = int.from_bytes(udp_data[0:2], byteorder="big")
        dst_port = int.from_bytes(udp_data[2:4], byteorder="big")
        udp_length = int.from_bytes(udp_data[4:6], byteorder="big")
        checksum = int.from_bytes(udp_data[6:8], byteorder="big")
        payload = udp_data[8:]

        return cls(src_port = src_port,
                   dst_port = dst_port, udp_length = udp_length,
                   checksum = checksum, payload = payload)