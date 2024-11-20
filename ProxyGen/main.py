# Credits : Xolo/@efenatuyo
# Notice : this code aswell as "Tor.exe" is not part of our Lisence.

import os
import subprocess
import psutil

class ServiceInstaller:
    def __init__(self, total_ips):
        self.total_ips = total_ips
        self.stop_tor_windows()

    def _generate_ips_file(self, file_path2):
        ips = b"HTTPTunnelPort 9080"
        for i in range(self.total_ips - 1):
            ips += f"\nHTTPTunnelPort {9081 + i}".encode()
        with open(file_path2, 'wb') as f:
            f.write(ips)

    def install_service(self):
        file_path = "tor.exe"
        file_path2 = "config"
        self._generate_ips_file(file_path2)

        process = subprocess.Popen(f"{file_path} -nt-service -f {file_path2}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            line = process.stdout.readline().decode().strip()
            print(line)
            if "Bootstrapped 100% (done): Done" in line:
                break
            
    def stop_tor_windows(self):
        for proc in psutil.process_iter():
            try:
                if proc.name() == "tor.exe":
                    proc.terminate()
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

def make(total_ips):
    ServiceInstaller(total_ips).install_service()
    return [f"http://127.0.0.1:{9080 + i}" for i in range(total_ips)]

ips = make(200)
input(f"\nPROXIES GENERATED:\n{ips}\n\nPress enter to terminate the proxies...")