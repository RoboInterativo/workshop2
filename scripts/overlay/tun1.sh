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


nohup socat UDP:$TO_NODE_IP:9000,bind=$NODE_IP:9000 TUN:$TUNNEL_IP/16,tun-name=tundudp,iff-no-pi,tun-type=tun &
#***Note that I removed "iff-up" switch from command on "ubuntu1" because I was getting an error.

2- On "ubuntu2" run:
nohup socat UDP:192.168.0.10:9000,bind=192.168.0.11:9000 TUN:172.16.1.100/16,tun-name=tundudp,iff-no-pi,tun-type=tun,iff-up &

3- Return to "ubuntu1" and run
ip link set dev tundudp up


#Check routes in container1
sudo ip netns exec $NS1 ip route

#Examine what route the route to reach one of the container on Ubuntu2
ip route get TO_IP1

#Ping a container hosted on Ubuntu2 from a container hosted on this server(Ubuntu1)
sudo ip netns exec NS1 ping -c 4 172.16.1.2
