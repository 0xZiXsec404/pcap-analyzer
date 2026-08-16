from dataclasses import dataclass

@dataclass
class TCPHeader():

    src_port: int
    dst_port: int
    seq_num: int
    ack_num: int
    data_offset: int
    flags: int
    window_size: int
    checksum: int
    urgent_pointer: int
    options: bytes
    payload: bytes

    @classmethod
    def from_bytes(cls, data: bytes) -> "TCPHeader":
        ip_ihl = data[0] & 0x0F
        ip_header_length = ip_ihl * 4

        tcp_data = data[ip_header_length:]

        if len(tcp_data) < 20:
            raise ValueError("TCP header is too short")

        src_port = int.from_bytes(tcp_data[0:2], byteorder="big")
        dst_port = int.from_bytes(tcp_data[2:4], byteorder="big")
        seq_num = int.from_bytes(tcp_data[4:8], byteorder="big")
        ack_num = int.from_bytes(tcp_data[8:12], byteorder="big")

        data_offset = (tcp_data[12] >> 4) * 4  # длина TCP-заголовка в байтах
        flags = tcp_data[13]

        window_size = int.from_bytes(tcp_data[14:16], byteorder="big")
        checksum = int.from_bytes(tcp_data[16:18], byteorder="big")
        urgent_pointer = int.from_bytes(tcp_data[18:20], byteorder="big")

        options = tcp_data[20:data_offset] if data_offset > 20 else b""
        payload = tcp_data[data_offset:]

        return cls(src_port = src_port, dst_port = dst_port,
                   seq_num = seq_num, ack_num = ack_num,
                   data_offset = data_offset, flags = flags,
                   window_size = window_size, checksum = checksum,
                   urgent_pointer = urgent_pointer, options = options,
                   payload = payload)

    @property
    def flags_list(self) -> list[str]:
        list_tcp_flags = []

        if self.flags & 0x01:
            list_tcp_flags.append("FIN")
        if self.flags & 0x02:
            list_tcp_flags.append("SYN")
        if self.flags & 0x04:
            list_tcp_flags.append("RST")
        if self.flags & 0x08:
            list_tcp_flags.append("PSH")
        if self.flags & 0x10:
            list_tcp_flags.append("ACK")
        if self.flags & 0x20:
            list_tcp_flags.append("URG")
        if self.flags & 0x40:
            list_tcp_flags.append("ECE")
        if self.flags & 0x80:
            list_tcp_flags.append("CWR")

        return list_tcp_flags