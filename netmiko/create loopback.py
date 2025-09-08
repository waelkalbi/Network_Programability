import datetime
print("Current date and time:")
print(datetime.datetime.now())
print("connecting via SSH => IP address")
from netmiko import ConnectHandler 
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.56.101",
    port="22",
    username="cisco",
    password="cisco123!"
)
config_commands = (
        'interface Loopback1111','ip address 192.168.11.11 255.255.255.0',
    )
output=sshCli.send_config_set(config_commands)
print(output)
output=sshCli.send_command("show ip  interface brief")
print(output)


