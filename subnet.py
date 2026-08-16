def ip_in_subnet(ip: str, subnet: str) -> bool:
    clear_ip = ip.strip().split(".")
    if len(clear_ip) != 4:
        raise ValueError("Неверный формат IP")

    ip_part_1 = int(clear_ip[0])
    ip_part_2 = int(clear_ip[1])
    ip_part_3 = int(clear_ip[2])
    ip_part_4 = int(clear_ip[3])

    clear_subnet = subnet.strip().split("/")
    network_ip = clear_subnet[0]
    mask_subnet = int(clear_subnet[1])

    clear_mask = "1" * mask_subnet + "0" * (32 - mask_subnet)

    mask_1 = int(clear_mask[0:8], 2)
    mask_2 = int(clear_mask[8:16], 2)
    mask_3 = int(clear_mask[16:24], 2)
    mask_4 = int(clear_mask[24:32], 2)

    count_ip_1 = ip_part_1 & mask_1
    count_ip_2 = ip_part_2 & mask_2
    count_ip_3 = ip_part_3 & mask_3
    count_ip_4 = ip_part_4 & mask_4

    list_ip = [count_ip_1, count_ip_2, count_ip_3, count_ip_4]
    true_ip = ".".join(str(part) for part in list_ip)

    return true_ip == network_ip