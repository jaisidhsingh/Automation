import subprocess

proc = subprocess.Popen(["ping", ip_network],stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    if not line:
        break
    if line:
        connected_ip = line.decode('utf-8').split()
        if len(connected_ip) != 0:
            if connected_ip[0] == "Reply":
                connected_ip = str(connected_ip[2]).split(sep=":")[0]
                break
    
if ip_device =  connected_ip:
    print("pc1 has joined")
