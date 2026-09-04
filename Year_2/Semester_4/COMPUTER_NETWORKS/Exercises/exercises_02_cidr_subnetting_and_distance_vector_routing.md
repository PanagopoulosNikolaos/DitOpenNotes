# Exercises 02: CIDR Subnetting and Distance-Vector Routing

This practice problem set provides step-by-step solutions for IP address calculations, Variable-Length Subnet Masking (VLSM), route aggregation, and Bellman-Ford distance-vector routing iterations.

---

## Problem 1: VLSM Subnet Allocation

### Question
An organization is allocated the block `200.100.50.0/24`. It needs to create four distinct subnets:
- **Subnet A:** requires 60 host interfaces
- **Subnet B:** requires 28 host interfaces
- **Subnet C:** requires 12 host interfaces
- **Subnet D:** requires 2 host interfaces (point-to-point link between routers)

Allocate subnets efficiently using VLSM to minimize wasted IP address space. For each subnet, specify:
1. Subnet mask (dotted-decimal and CIDR prefix length).
2. Network address.
3. Usable host address range.
4. Directed broadcast address.

### Solution

Sort requirements in descending order of size: Subnet A (60) > Subnet B (28) > Subnet C (12) > Subnet D (2).

#### Subnet A: 60 Hosts
- Need $2^h - 2 \ge 60 \implies 2^h \ge 62 \implies h = 6$ bits ($2^6 - 2 = 62$ hosts).
- Prefix length: $32 - 6 = /26$. Subnet mask: `255.255.255.192`.
- Network Address: `200.100.50.0/26`.
- Usable Host Range: `200.100.50.1` to `200.100.50.62`.
- Broadcast Address: `200.100.50.63`.

#### Subnet B: 28 Hosts
- Next available address: `200.100.50.64`.
- Need $2^h - 2 \ge 28 \implies 2^h \ge 30 \implies h = 5$ bits ($2^5 - 2 = 30$ hosts).
- Prefix length: $32 - 5 = /27$. Subnet mask: `255.255.255.224`.
- Network Address: `200.100.50.64/27`.
- Usable Host Range: `200.100.50.65` to `200.100.50.94`.
- Broadcast Address: `200.100.50.95`.

#### Subnet C: 12 Hosts
- Next available address: `200.100.50.96`.
- Need $2^h - 2 \ge 12 \implies 2^h \ge 14 \implies h = 4$ bits ($2^4 - 2 = 14$ hosts).
- Prefix length: $32 - 4 = /28$. Subnet mask: `255.255.255.240`.
- Network Address: `200.100.50.96/28`.
- Usable Host Range: `200.100.50.97` to `200.100.50.110`.
- Broadcast Address: `200.100.50.111`.

#### Subnet D: 2 Hosts
- Next available address: `200.100.50.112`.
- Need $2^h - 2 \ge 2 \implies 2^h \ge 4 \implies h = 2$ bits ($2^2 - 2 = 2$ hosts).
- Prefix length: $32 - 2 = /30$. Subnet mask: `255.255.255.252`.
- Network Address: `200.100.50.112/30`.
- Usable Host Range: `200.100.50.113` to `200.100.50.114`.
- Broadcast Address: `200.100.50.115`.

---

## Problem 2: Bellman-Ford Distance-Vector Convergence

### Question
Consider the 3-node network below with link costs $c(X, Y) = 2$, $c(Y, Z) = 1$, and $c(X, Z) = 7$:

```
        (X)
       /   \
    2 /     \ 7
     /       \
   (Y)-------(Z)
         1
```

Show the initial distance vectors and the distance table at node $X$ after the first iteration of vector exchange.

### Solution

#### Initial State ($t = 0$)
Direct neighbor costs:
- $c(X, Y) = 2$
- $c(X, Z) = 7$
- $c(X, X) = 0$

Node $X$'s initial distance vector: $D_X = [X: 0, Y: 2, Z: 7]$.
Initial vectors received from neighbors:
- $D_Y = [X: 2, Y: 0, Z: 1]$
- $D_Z = [X: 7, Y: 1, Z: 0]$

#### Iteration 1 at Node $X$
Node $X$ computes cost to all destinations using Bellman-Ford equation:

$$
D_X(d) = \min_{v \in \{Y, Z\}} \{ c(X, v) + D_v(d) \}
$$

- For destination $Y$:
  $$\min \{ c(X, Y) + D_Y(Y), c(X, Z) + D_Z(Y) \} = \min \{ 2 + 0, 7 + 1 \} = 2 \quad (\text{via } Y)$$
- For destination $Z$:
  $$\min \{ c(X, Y) + D_Y(Z), c(X, Z) + D_Z(Z) \} = \min \{ 2 + 1, 7 + 0 \} = \min \{ 3, 7 \} = 3 \quad (\text{via } Y)$$

#### Updated Distance Vector at Node $X$
$$D_X = [X: 0, Y: 2, Z: 3]$$
Next hop for destination $Z$ changes from direct link $(X \to Z)$ to indirect path through neighbor $Y$ ($(X \to Y \to Z)$), reducing least-cost from 7 to 3.
Node $X$ announces its new distance vector $D_X$ to its neighbors.

