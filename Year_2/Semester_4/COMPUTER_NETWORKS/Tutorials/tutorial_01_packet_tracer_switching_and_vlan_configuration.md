# Tutorial 01: Cisco Packet Tracer Switching and VLAN Configuration

This tutorial provides a step-by-step practical laboratory guide for configuring Ethernet switches, creating Virtual Local Area Networks (VLANs), assigning access ports, and establishing IEEE 802.1Q trunk links in Cisco Packet Tracer.

---

## 1. Laboratory Topology

The network consists of two Cisco Catalyst 2960 switches connected via GigabitEthernet interfaces, serving four client PCs across two departments:

```
[ PC-1: 192.168.10.10/24 ]               [ PC-3: 192.168.10.20/24 ]
     (VLAN 10 - Sales)                        (VLAN 10 - Sales)
            | Fa0/1                                  | Fa0/1
    +---------------+   Trunk: Gi0/1 - Gi0/1   +---------------+
    |   Switch-1    |==========================|   Switch-2    |
    +---------------+                          +---------------+
            | Fa0/2                                  | Fa0/2
[ PC-2: 192.168.20.10/24 ]               [ PC-4: 192.168.20.20/24 ]
     (VLAN 20 - Eng)                          (VLAN 20 - Eng)
```

---

## 2. Cisco IOS Command Line Configuration

### 2.1 Switch-1 Configuration

Open the CLI console of `Switch-1` and enter privileged EXEC mode:

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname Switch-1
```

Create VLANs and assign descriptive names:

```text
Switch-1(config)# vlan 10
Switch-1(config-vlan)# name Sales
Switch-1(config-vlan)# exit

Switch-1(config)# vlan 20
Switch-1(config-vlan)# name Engineering
Switch-1(config-vlan)# exit
```

Configure access ports for end-host connections:

```text
Switch-1(config)# interface FastEthernet 0/1
Switch-1(config-if)# switchport mode access
Switch-1(config-if)# switchport access vlan 10
Switch-1(config-if)# no shutdown
Switch-1(config-if)# exit

Switch-1(config)# interface FastEthernet 0/2
Switch-1(config-if)# switchport mode access
Switch-1(config-if)# switchport access vlan 20
Switch-1(config-if)# no shutdown
Switch-1(config-if)# exit
```

Configure the inter-switch trunk link:

```text
Switch-1(config)# interface GigabitEthernet 0/1
Switch-1(config-if)# switchport mode trunk
Switch-1(config-if)# switchport trunk allowed vlan 10,20
Switch-1(config-if)# no shutdown
Switch-1(config-if)# end
Switch-1# copy running-config startup-config
```

### 2.2 Switch-2 Configuration

Repeat the corresponding commands on `Switch-2`:

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname Switch-2

Switch-2(config)# vlan 10
Switch-2(config-vlan)# name Sales
Switch-2(config-vlan)# exit

Switch-2(config)# vlan 20
Switch-2(config-vlan)# name Engineering
Switch-2(config-vlan)# exit

Switch-2(config)# interface FastEthernet 0/1
Switch-2(config-if)# switchport mode access
Switch-2(config-if)# switchport access vlan 10
Switch-2(config-if)# no shutdown
Switch-2(config-if)# exit

Switch-2(config)# interface FastEthernet 0/2
Switch-2(config-if)# switchport mode access
Switch-2(config-if)# switchport access vlan 20
Switch-2(config-if)# no shutdown
Switch-2(config-if)# exit

Switch-2(config)# interface GigabitEthernet 0/1
Switch-2(config-if)# switchport mode trunk
Switch-2(config-if)# switchport trunk allowed vlan 10,20
Switch-2(config-if)# no shutdown
Switch-2(config-if)# end
Switch-2# copy running-config startup-config
```

---

## 3. Verification and Diagnostics

### 3.1 Verifying VLAN Membership
Execute `show vlan brief` on `Switch-1`:

```text
Switch-1# show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/3, Fa0/4, Fa0/5...
10   Sales                            active    Fa0/1
20   Engineering                      active    Fa0/2
```

### 3.2 Verifying Trunk Status
Execute `show interfaces trunk`:

```text
Switch-1# show interfaces trunk

Port        Mode             Encapsulation  Status        Native vlan
Gi0/1       on               802.1q         trunking      1

Port        Vlans allowed on trunk
Gi0/1       10,20
```

### 3.3 End-to-End Connectivity Testing
1. From `PC-1` (`192.168.10.10`), ping `PC-3` (`192.168.10.20`):
   ```text
   PC> ping 192.168.10.20
   Pinging 192.168.10.20 with 32 bytes of data:
   Reply from 192.168.10.20: bytes=32 time<1ms TTL=128
   Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
   ```
   **Result:** Successful. Frames carry 802.1Q tag across `Gi0/1` and arrive at `PC-3`.

2. From `PC-1` (`192.168.10.10`), ping `PC-2` (`192.168.20.10`):
   ```text
   PC> ping 192.168.20.10
   Request timed out.
   Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)
   ```
   **Result:** Traffic dropped by switch isolation. Inter-VLAN communication requires a Layer 3 routing device.

