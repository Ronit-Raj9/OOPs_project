with open('database_addr.txt', 'r') as file:
    lines = file.readlines()

    host_addr = lines[0].strip()
    port_no = int(lines[1].strip())

    print("Host address:", host_addr, " Port no:", port_no)