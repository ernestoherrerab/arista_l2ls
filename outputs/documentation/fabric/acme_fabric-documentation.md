# acme_fabric

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| dc01 | leaf | bl01a | 192.168.0.179/24 | VEOS-LAB | Provisioned | - |
| dc01 | leaf | bl01b | 192.168.0.180/24 | VEOS-LAB | Provisioned | - |
| dc01 | leaf | le01a | 192.168.0.175/24 | VEOS-LAB | Provisioned | - |
| dc01 | leaf | le01b | 192.168.0.176/24 | VEOS-LAB | Provisioned | - |
| dc01 | leaf | le02a | 192.168.0.177/24 | VEOS-LAB | Provisioned | - |
| dc01 | leaf | le02b | 192.168.0.178/24 | VEOS-LAB | Provisioned | - |
| acme_fabric | server | server17 | 192.168.0.155/24 | vEOS-LAB | Provisioned | - |
| acme_fabric | server | server18 | 192.168.0.156/24 | vEOS-LAB | Provisioned | - |
| acme_fabric | server | server19 | 192.168.0.157/24 | vEOS-LAB | Provisioned | - |
| acme_fabric | server | server20 | 192.168.0.158/24 | vEOS-LAB | Provisioned | - |
| acme_fabric | server | server21 | 192.168.0.159/24 | vEOS-LAB | Provisioned | - |
| acme_fabric | server | server22 | 192.168.0.160/24 | vEOS-LAB | Provisioned | - |
| acme_fabric | server | server23 | 192.168.0.161/24 | vEOS-LAB | Provisioned | - |
| acme_fabric | server | server24 | 192.168.0.162/24 | vEOS-LAB | Provisioned | - |
| dc01 | l3spine | sp01 | 192.168.0.173/24 | VEOS-LAB | Provisioned | - |
| dc01 | l3spine | sp02 | 192.168.0.174/24 | VEOS-LAB | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| leaf | bl01a | Ethernet1 | l3spine | sp01 | Ethernet5 |
| leaf | bl01a | Ethernet2 | l3spine | sp02 | Ethernet5 |
| leaf | bl01a | Ethernet47 | mlag_peer | bl01b | Ethernet47 |
| leaf | bl01a | Ethernet48 | mlag_peer | bl01b | Ethernet48 |
| leaf | bl01b | Ethernet1 | l3spine | sp01 | Ethernet6 |
| leaf | bl01b | Ethernet2 | l3spine | sp02 | Ethernet6 |
| leaf | le01a | Ethernet1 | l3spine | sp01 | Ethernet1 |
| leaf | le01a | Ethernet2 | l3spine | sp02 | Ethernet1 |
| leaf | le01a | Ethernet5 | server | server17 | Ethernet1 |
| leaf | le01a | Ethernet6 | server | server18 | Ethernet1 |
| leaf | le01a | Ethernet7 | server | server21 | Ethernet1 |
| leaf | le01a | Ethernet8 | server | server22 | Ethernet1 |
| leaf | le01a | Ethernet47 | mlag_peer | le01b | Ethernet47 |
| leaf | le01a | Ethernet48 | mlag_peer | le01b | Ethernet48 |
| leaf | le01b | Ethernet1 | l3spine | sp01 | Ethernet2 |
| leaf | le01b | Ethernet2 | l3spine | sp02 | Ethernet2 |
| leaf | le01b | Ethernet5 | server | server17 | Ethernet2 |
| leaf | le01b | Ethernet6 | server | server18 | Ethernet2 |
| leaf | le01b | Ethernet7 | server | server21 | Ethernet2 |
| leaf | le01b | Ethernet8 | server | server22 | Ethernet2 |
| leaf | le02a | Ethernet1 | l3spine | sp01 | Ethernet3 |
| leaf | le02a | Ethernet2 | l3spine | sp02 | Ethernet3 |
| leaf | le02a | Ethernet5 | server | server19 | Ethernet1 |
| leaf | le02a | Ethernet6 | server | server20 | Ethernet1 |
| leaf | le02a | Ethernet7 | server | server23 | Ethernet1 |
| leaf | le02a | Ethernet8 | server | server24 | Ethernet1 |
| leaf | le02a | Ethernet47 | mlag_peer | le02b | Ethernet47 |
| leaf | le02a | Ethernet48 | mlag_peer | le02b | Ethernet48 |
| leaf | le02b | Ethernet1 | l3spine | sp01 | Ethernet4 |
| leaf | le02b | Ethernet2 | l3spine | sp02 | Ethernet4 |
| leaf | le02b | Ethernet5 | server | server19 | Ethernet2 |
| leaf | le02b | Ethernet6 | server | server20 | Ethernet2 |
| leaf | le02b | Ethernet7 | server | server23 | Ethernet2 |
| leaf | le02b | Ethernet8 | server | server24 | Ethernet2 |
| l3spine | sp01 | Ethernet47 | mlag_peer | sp02 | Ethernet47 |
| l3spine | sp01 | Ethernet48 | mlag_peer | sp02 | Ethernet48 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.0.2.0/24 | 256 | 2 | 0.79 % |
| 10.248.0.0/24 | 256 | 8 | 3.13 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| acme_fabric | server17 | 10.248.0.17/32 |
| acme_fabric | server18 | 10.248.0.18/32 |
| acme_fabric | server19 | 10.248.0.19/32 |
| acme_fabric | server20 | 10.248.0.20/32 |
| acme_fabric | server21 | 10.248.0.21/32 |
| acme_fabric | server22 | 10.248.0.22/32 |
| acme_fabric | server23 | 10.248.0.23/32 |
| acme_fabric | server24 | 10.248.0.24/32 |
| dc01 | sp01 | 10.0.2.1/32 |
| dc01 | sp02 | 10.0.2.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
