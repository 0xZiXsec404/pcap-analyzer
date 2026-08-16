def filter_user():
    """Фильтрация ввода пользователя"""
    
    PROTOCOL_NAMES = {
        "TCP": 6,
        "UDP": 17,
        "ICMP": 1,
    }

    protocol = input("Введите протокол: ")
    if len(protocol) == 0:
        true_protocol = None
    elif str(protocol):
        new_protocol = protocol.upper()
        true_protocol = PROTOCOL_NAMES.get(new_protocol)
        if true_protocol is None:
            print("Такого протокола пока что нет")
            raise ValueError
    else: raise ValueError

    dst_port = input("Введите порт:")
    if len(dst_port) == 0:
            tru_dst_port = None
    elif int(dst_port) and (0 < int(dst_port) <= 65535):
        tru_dst_port = int(dst_port)
    else: raise ValueError

    dst_ip = input("Введите IP:")
    if len(dst_ip) == 0:
        dst_ip = None
    else:
        clear_dst_ip = dst_ip.strip().split(".")
        dst_ip = dst_ip.strip()
        if len(clear_dst_ip) != 4:
            raise ValueError
        for i in range(0, 4):
            if int(clear_dst_ip[i]) < 0 or int(clear_dst_ip[i]) > 255:
                raise ValueError

    return true_protocol, tru_dst_port, dst_ip
    

def filter_packet(parsed, filter_protocol=None, filter_port=None, filter_ip=None):
    if filter_protocol is not None and parsed["protocol"] != filter_protocol:
        return None

    if filter_ip is not None and parsed["dst_ip"] != filter_ip:
        return None

    if filter_port is not None:
        transport = parsed["transport"]
        if transport is None or not hasattr(transport, "dst_port"):
            return None
        if transport.dst_port != filter_port:
            return None

    return parsed