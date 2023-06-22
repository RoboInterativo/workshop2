NS1="NS1"
NS2="NS2"
NODE_IP="192.168.0.10"
BRIDGE_SUBNET="172.16.0.0/24"
BRIDGE_IP="172.16.0.1"
IP1="172.16.0.1"
IP2="172.16.0.2"

TO_NODE_IP="192.168.0.10"
TO_BRIDGE_SUBNET="172.16.0.0/24"
TO_BRIDGE_IP="172.16.0.1"
TO_IP1="172.16.0.1"
TO_IP2="172.16.0.2"

ip netns add $NS1
ip netns add $NS1
ip netns show

ip link add veth10 type peer name veth11
ip link add veth20 type peer name veth21
ip link show type veth

ip netns exec $NS1 ip addr add $IP1/24 veth11
ip netns exec $NS2 ip addr add $IP2/24 veth21

ip netns exec $NS1 ip link set dev veth11 up
ip netns exec $NS2 ip link set dev veth21 up
