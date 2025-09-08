import datetime
print("Current date and time:")
print(datetime.datetime.now())
print("connecting via SSH => delete LOOPBACK")
from netmiko import ConnectHandler 
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.56.101",
    port="22",
    username="cisco",
    password="cisco123!"
)
config_commands = (
        'no interface Loopback11',
    )
output=sshCli.send_config_set(config_commands)
output=sshCli.send_command("show ip  interface brief")
print(output)


