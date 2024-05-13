# le02b

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [IP Domain-list](#ip-domain-list)
  - [IP Name Servers](#ip-name-servers)
  - [Clock Settings](#clock-settings)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | default | 192.168.0.178/24 | - |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | default | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   no shutdown
   ip address 192.168.0.178/24
```

### DNS Domain

DNS domain: acme.com

#### DNS Domain Device Configuration

```eos
dns domain acme.com
!
```

### IP Domain-list

#### Domains List

- acme.com

#### IP Domain-list Device Configuration

```eos
ip domain-list acme.com
!
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 10.255.0.2 | default | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf default 10.255.0.2
```

### Clock Settings

#### Clock Timezone Settings

Clock Timezone is set to **CET**.

#### Clock Device Configuration

```eos
!
clock timezone CET
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| default | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf default
      no shutdown
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| cvpadmin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
```

### AAA Authentication

#### AAA Authentication Summary

| Type | Sub-type | User Stores |
| ---- | -------- | ---------- |

Policy local allow-nopassword-remote-login has been enabled.

#### AAA Authentication Device Configuration

```eos
aaa authentication policy local allow-nopassword-remote-login
!
```

### AAA Authorization

#### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | local |

Authorization for configuration commands is disabled.

#### AAA Authorization Device Configuration

```eos
aaa authorization exec default local
!
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 192.168.0.5:9910 | default | token,/tmp/token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.0.5:9910 -cvauth=token,/tmp/token -cvvrf=default -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| le02 | Vlan4094 | 192.168.1.8 | Port-Channel47 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id le02
   local-interface Vlan4094
   peer-address 192.168.1.8
   peer-link Port-Channel47
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4094**

### Spanning Tree Device Configuration

```eos
!
no spanning-tree vlan-id 4094
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 40 | ACME-GENERAL_40 | - |
| 41 | ACME-GENERAL_41 | - |
| 50 | ACME-LAB_50 | - |
| 51 | ACME-LAB_51 | - |
| 4094 | MLAG_PEER | MLAG |

### VLANs Device Configuration

```eos
!
vlan 40
   name ACME-GENERAL_40
!
vlan 41
   name ACME-GENERAL_41
!
vlan 50
   name ACME-LAB_50
!
vlan 51
   name ACME-LAB_51
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | SP01_Ethernet4 | *trunk | *40-41,50-51 | *- | *- | 1 |
| Ethernet2 | SP02_Ethernet4 | *trunk | *40-41,50-51 | *- | *- | 1 |
| Ethernet5 | server19_Ethernet2 | *access | *- | *- | *- | 5 |
| Ethernet6 | server20_Ethernet2 | *access | *41 | *- | *- | 6 |
| Ethernet7 | server23_Ethernet2 | *access | *50 | *- | *- | 7 |
| Ethernet8 | server24_Ethernet2 | *access | *51 | *- | *- | 8 |
| Ethernet47 | MLAG_PEER_le02a_Ethernet47 | *trunk | *- | *- | *['MLAG'] | 47 |
| Ethernet48 | MLAG_PEER_le02a_Ethernet48 | *trunk | *- | *- | *['MLAG'] | 47 |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description SP01_Ethernet4
   no shutdown
   channel-group 1 mode active
!
interface Ethernet2
   description SP02_Ethernet4
   no shutdown
   channel-group 1 mode active
!
interface Ethernet5
   description server19_Ethernet2
   no shutdown
   channel-group 5 mode active
!
interface Ethernet6
   description server20_Ethernet2
   no shutdown
   channel-group 6 mode active
!
interface Ethernet7
   description server23_Ethernet2
   no shutdown
   channel-group 7 mode active
!
interface Ethernet8
   description server24_Ethernet2
   no shutdown
   channel-group 8 mode active
!
interface Ethernet47
   description MLAG_PEER_le02a_Ethernet47
   no shutdown
   channel-group 47 mode active
!
interface Ethernet48
   description MLAG_PEER_le02a_Ethernet48
   no shutdown
   channel-group 47 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | SP_Po3 | switched | trunk | 40-41,50-51 | - | - | - | - | 1 | - |
| Port-Channel5 | server19_LINK_TO_SRV19 | switched | access | - | - | - | - | - | 5 | - |
| Port-Channel6 | server20_LINK_TO_SRV20 | switched | access | 41 | - | - | - | - | - | 0000:0000:c21d:6a08:ea1e |
| Port-Channel7 | server23_LINK_TO_SRV23 | switched | access | 50 | - | - | - | - | 7 | - |
| Port-Channel8 | server24_LINK_TO_SRV24 | switched | access | 51 | - | - | - | - | 8 | - |
| Port-Channel47 | MLAG_PEER_le02a_Po47 | switched | trunk | - | - | ['MLAG'] | - | - | - | - |

##### EVPN Multihoming

####### EVPN Multihoming Summary

| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |
| --------- | --------------------------- | --------------------------- | ------------ |
| Port-Channel6 | 0000:0000:c21d:6a08:ea1e | all-active | c2:1d:6a:08:ea:1e |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description SP_Po3
   no shutdown
   switchport
   switchport trunk allowed vlan 40-41,50-51
   switchport mode trunk
   mlag 1
!
interface Port-Channel5
   description server19_LINK_TO_SRV19
   no shutdown
   switchport
   mlag 5
!
interface Port-Channel6
   description server20_LINK_TO_SRV20
   no shutdown
   switchport
   switchport access vlan 41
   evpn ethernet-segment
      identifier 0000:0000:c21d:6a08:ea1e
      route-target import c2:1d:6a:08:ea:1e
   lacp system-id c21d.6a08.ea1e
   spanning-tree portfast
!
interface Port-Channel7
   description server23_LINK_TO_SRV23
   no shutdown
   switchport
   switchport access vlan 50
   mlag 7
   spanning-tree portfast
!
interface Port-Channel8
   description server24_LINK_TO_SRV24
   no shutdown
   switchport
   switchport access vlan 51
   mlag 8
   spanning-tree portfast
!
interface Port-Channel47
   description MLAG_PEER_le02a_Po47
   no shutdown
   switchport
   switchport mode trunk
   switchport trunk group MLAG
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan4094 | MLAG_PEER | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan4094 |  default  |  192.168.1.9/31  |  -  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 1500
   no autostate
   ip address 192.168.1.9/31
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |

#### IP Routing Device Configuration

```eos
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| default | false |

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |

### VRF Instances Device Configuration

```eos
```
