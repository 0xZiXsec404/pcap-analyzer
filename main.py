from io_utils import read_file_to_bytes
from dispatcher import parse_packet
from format_packet import format_packet
from filter_packet import filter_user, filter_packet
import socket


def parse_ipv4_file(path, limit=None):
    count = 0

    for packet in read_file_to_bytes(path):
        if limit is not None and count >= limit:
            break

        yield parse_packet(packet)
        count += 1


def main():

    HOST = socket.gethostbyname(socket.gethostname())

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((HOST, 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        filter_protocol, filter_port, filter_ip = filter_user()
    except ValueError:
        print("Некорректный ввод фильтра, показываю все пакеты")
        filter_protocol, filter_port, filter_ip = None, None, None

    try:
        while True:
            raw_data, addr = s.recvfrom(65535)
            try:
                parsed = parse_packet(raw_data)
            except (ValueError, IndexError) as e:
                print(f"Пропущен пакет, не удалось распарсить: {e}")
                continue

            matched = filter_packet(parsed, filter_protocol, filter_port, filter_ip)
            if matched is not None:
                print(format_packet(matched))
    except KeyboardInterrupt:
        print("Остановлено пользователем")
    finally:
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


if __name__ == "__main__":
    main()