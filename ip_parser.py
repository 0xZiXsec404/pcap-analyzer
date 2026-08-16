def parse_one_ipv4_header(data):
    version = data[0] >> 4
    ihl = data[0] & 0x0F

    header_length = ihl * 4
    total_length = int.from_bytes(data[2:4], byteorder="big")

    protocol = data[9]

    src_ip = ".".join(str(byte) for byte in data[12:16])
    dst_ip = ".".join(str(byte) for byte in data[16:20])

    return {
        "version": version,
        "ihl": ihl,
        "header_length": header_length,
        "total_length": total_length,
        "protocol": protocol,
        "src_ip": src_ip,
        "dst_ip": dst_ip
    }