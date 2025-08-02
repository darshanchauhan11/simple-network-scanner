from flask import Flask, render_template, request
from scapy.all import ARP, Ether, srp
import socket
from datetime import datetime

app = Flask(__name__)

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

def scan_ports(ip, port_range=(20, 100)):
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
            s.close()
        except:
            pass
    return open_ports

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        ip_range = request.form['ip_range']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("scan_results.txt", "w") as f:
            f.write(f"Scan Results - {timestamp}\n{'='*50}\n")

        devices = scan_network(ip_range)
        for device in devices:
            ports = scan_ports(device['ip'])
            results.append({
                'ip': device['ip'],
                'mac': device['mac'],
                'ports': ports
            })
            with open("scan_results.txt", "a") as f:
                f.write(f"\nIP: {device['ip']}  MAC: {device['mac']}\n")
                if ports:
                    f.write("Open Ports: " + ", ".join(map(str, ports)) + "\n")
                else:
                    f.write("No open ports found.\n")

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
