from dataclasses import dataclass

@dataclass
class ICMPHeader:
    icmp_type: int
    code: int
    checksum: int
    payload: bytes
    identifier: int | None = None
    sequence_number: int | None = None
    rest_of_header: int | None = None

    @classmethod
    def from_bytes(cls, data: bytes) -> "ICMPHeader":
        ip_ihl = data[0] & 0x0F
        ip_header_length = ip_ihl * 4
        icmp_data = data[ip_header_length:]

        if len(icmp_data) < 8:
            raise ValueError("ICMP header is too short")

        icmp_type = icmp_data[0]
        code = icmp_data[1]
        checksum = int.from_bytes(icmp_data[2:4], byteorder="big")
        payload = icmp_data[8:]

        if icmp_type in (0, 8):
            identifier = int.from_bytes(icmp_data[4:6], byteorder="big")
            sequence_number = int.from_bytes(icmp_data[6:8], byteorder="big")
            return cls(icmp_type=icmp_type, code=code, checksum=checksum,
                       payload=payload, identifier=identifier,
                       sequence_number=sequence_number)
        else:
            rest_of_header = icmp_data[4:8]
            return cls(icmp_type=icmp_type, code=code, checksum=checksum,
                       payload=payload, rest_of_header=rest_of_header)