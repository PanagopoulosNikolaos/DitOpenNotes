# Computer Networks: HomeWork 3

---

## Scenario
Use the network provided to you in **Cisco Packet Tracer** to investigate the operation of **PDUs** (Protocol Data Units). 
The devices are already configured. You will gather PDU information in **Simulation Mode** and answer a series of questions regarding the data you collect. 

---

## Part 1: Examine an ARP Request

### Step 1: Create ARP requests by pinging 172.16.31.3 from 172.16.31.2.

- **a.** Click on the PC with IP `172.16.31.2` and open the **Command Prompt**.
- **b.** Enter the following command to clear the ARP table:
  ```bash
  arp -d
  ```
- **c.** Switch to **Simulation Mode** (usually located in the lower right part of the screen) in Packet Tracer and enter the command:
  ```bash
  ping 172.16.31.3
  ```
  > **Note:** Two PDUs will be created. The ping command cannot complete the ICMP packet without knowing the destination MAC address. Thus, the PC sends an ARP broadcast frame to find the destination MAC address.
- **d.** Click the **Capture/Forward** button once.
  The ARP PDU moves to `Switch1`, while the ICMP PDU disappears, waiting for the ARP reply. Open the PDU by clicking on the colored box in the GUI and record the destination MAC address.
  > **Question d:** Is this address listed in the table above?
- **e.** Click **Capture/Forward** to move the PDU to the next device.
  > **Question e:** How many copies of the PDU did Switch1 create?
- **f.** Remaining in the same state, check the receiving device:
  > **Question f:** What is the IP address of the device that accepted the PDU?
- **g.** Open the PDU and examine Layer 2 under the *Inbound/Outbound PDU Details* tab.
  > **Question g:** What do you observe regarding the source and destination MAC addresses?
- **h.** Click **Capture/Forward** continuously until the PDU returns to `172.16.31.2`.
  > **Question h:** How many copies of the PDU did the switch create during the ARP reply?

<br>

### Step 2: Examine the ARP table

- **a.** Note that the ICMP packet reappears. Open the PDU and examine the MAC addresses.
  > **Question a:** Do the source and destination MAC addresses agree with their IP addresses?
- **b.** Return to **Realtime** mode and let the ping complete.
- **c.** Click on `172.16.31.2` and enter the command:
  ```bash
  arp -a
  ```
  > **Question c:** Which IP address does the MAC address entry correspond to?
- **d.**
  > **Question d:** In general, when does an end device issue an ARP request?

---

## Part 2: Examine a Switch MAC Address Table

### Step 1: Generate additional traffic to populate the switch MAC address table

- **a.** From address `172.16.31.2`, enter the command:
  ```bash
  ping 172.16.31.4
  ```
- **b.** Click on the device with IP `10.10.10.2` and open the **Command Prompt**.
- **c.** Enter the command:
  ```bash
  ping 10.10.10.3
  ```
  > **Question c:** How many replies were sent and received?

<br>

### Step 2: Examine the MAC address table on the switches

- **a.** Click on `Switch1` and then on the **CLI** tab. Enter the following command:
  ```cisco
  show mac-address-table
  ```
  > **Question a:** Do the entries correspond to those in the table above?
- **b.** Click on `Switch0` and then on the **CLI** tab. Enter privileged EXEC mode (by typing `enable`) and enter the command:
  ```cisco
  show mac-address-table
  ```
  > **Question b:** Do the entries correspond to those in the table above?
- **c.**
  > **Question c:** Why are two MAC addresses associated with a single port?

---

## Part 3: Examine the ARP process in Remote Communications

### Step 1: Generate traffic to produce ARP traffic

- **a.** Click on `172.16.31.2` and open the command prompt.
- **b.** Enter the command:
  ```bash
  ping 10.10.10.1
  ```
- **c.** Type:
  ```bash
  arp -a
  ```
  > **Question c:** What is the IP address of the new ARP table entry?
- **d.** Type `arp -d` to clear the ARP table and switch back to **Simulation Mode**.
- **e.** Repeat the ping to address `10.10.10.1`.
  > **Question e:** How many PDUs appear?
- **f.** Click **Capture/Forward**. Click on the PDU currently at `Switch1`.
  > **Question f:** What is the target destination IP address of the ARP request?
- **g.**
  > **Question g:** The destination IP address is not `10.10.10.1`. Why?

<br>

### Step 2: Examine the ARP table on the router (Router1)

- **a.** Switch to **Realtime** mode. Click on `Router1` and then on the **CLI** tab.
- **b.** Enter privileged EXEC mode (type `enable`) and then type:
  ```cisco
  show mac-address-table
  ```
  > **Question b:** How many MAC addresses are in the table? Why?
- **c.** Enter the command:
  ```cisco
  show arp
  ```
  > **Question c:** Is there an entry for `172.16.31.2`?
- **d.**
  > **Question d:** What happens on the first ping in case the router answers the ARP request?

---
> **ATTENTION:** All the above answers (Questions **a**, **b**, **c**, etc.) must be completed in the answer file: `AM_HW3Answers_Sheet.txt`.