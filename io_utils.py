from pathlib import Path

PATH_SAMPLE_HEX = Path("sample_packet.hex")


def ensure_sample_file():
    """Создаёт тестовый hex-файл с одним пакетом, если его ещё нет."""
    if not PATH_SAMPLE_HEX.exists():
        PATH_SAMPLE_HEX.write_text(
            "450000280000400040060000c0a80001c0a80002\n",
            encoding="utf-8"
        )


def read_file_to_bytes(path):
    """Построчно читает hex-файл и отдаёт каждую строку как bytes одного пакета."""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            packet = bytes.fromhex(line)

            if len(packet) < 20:
                raise ValueError("IPv4 header is too short")

            yield packet