1
1
#!/usr/bin/env bash
NS1="NS1"
NS2="NS2"
NODE_IP="195.140.146.105"
TO_NODE_IP="212.57.126.254"
#`ip -4 addr show ens3 |grep -oP '(?<=inet\s)\d+(\.\d+){3}'`
TUNNEL_IP="172.16.0.100"
BRIDGE_IP="172.16.0.1"
IP1="172.16.0.2"
IP2="172.16.0.3"

TO_TUNNEL_IP="172.16.1.100"
TO_BRIDGE_IP="172.16.1.1"
TO_IP1="172.16.1.2"
TO_IP2="172.16.1.3"


#2- On "ubuntu2" run:
nohup socat UDP:$NODE_IP:9000,bind=$TO_NODE_IP:9000 TUN:$TO_TUNNEL_IP/16,tun-name=tundudp,iff-no-pi,tun-type=tun,iff-up &
