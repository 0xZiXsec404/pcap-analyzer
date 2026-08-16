def hex_acsii_dump(payload: bytes) -> str:
    lines = []

    for data in range(0, len(payload), 16):
        chunk = payload[data:data + 16]
        hex_parts = [f"{byte:02x}" for byte in chunk]
        ascii_parts = [chr(byte) if 32 <= byte <= 126 else "." for byte in chunk]

        str_data = " ".join(hex_parts) + " " + "".join(ascii_parts)
        lines.append(str_data)

    return "\n".join(lines)

def try_decode_text(payload: bytes) -> str:

    try:
        return payload.decode("ascii")
    except UnicodeDecodeError: 
        return None

def hex_and_acsii(payload: bytes) -> str:

    hex_and_acsii_result = hex_acsii_dump(payload)
    only_acsii_result = try_decode_text(payload)

    return f"Ручной первод hex и acsii: {hex_and_acsii_result}\n С помощью decode: {only_acsii_result}"