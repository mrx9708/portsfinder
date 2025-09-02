import socket
def scan_ports(target,ports):
    print(f"scanning targets {target}")
    for ports in ports:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(4)
        result=sock.connect_ex((target,ports))
        if result==0:
            print(f"port {ports} is open")
        else:
            print(f"port {ports} is closed")
        sock.close()


if __name__=="__main__":
    target=input("Enter target to scan: ")
    port_range=range(10,1025)
    scan_ports(target,port_range)