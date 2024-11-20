# Credits : Xolo/@efenatuyo
# Notice : this code aswell as "Tor.exe" is not part of our Lisence.

import os, subprocess, psutil, time

class ServiceInstaller:
    def __init__(self, amount, proxy_start_port):
        self.amount = amount
        self.proxy_start_port = proxy_start_port
        self.stop_tor_windows()

    def _generate_ips_file(self, config_path):
        tor_config = f"SOCKSPort {self.proxy_start_port}\n"
        # tor_config += "ExitNodes {fr},{de},{nl}\nExcludeExitNodes {us},{cn},{ru}\n" download geoip files if u wanna use this
        tor_config += "BandwidthRate 1GB\nBandwidthBurst 1GB\n"
        for i in range(self.amount):
            tor_config += f"HTTPTunnelPort {self.proxy_start_port + i+1}\n"
        with open(config_path, 'w') as f:
            f.write(tor_config)

    def install_service(self):
        exe_path = "src\\tor\\tor.exe"
        config_path = "src\\tor\\config"
        self._generate_ips_file(config_path)

        process = subprocess.Popen(f"{exe_path} -nt-service -f {config_path}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while 1:
            line = process.stdout.readline().decode().strip()
            # time.sleep(0.05) # Comment this out and add "import time" for debugging
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

def Make_Proxies(amount, proxy_start_port):
    ServiceInstaller(amount, proxy_start_port).install_service()
    print("Tor Succesfully inited")
    return