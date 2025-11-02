## Installing VS Code on Debian Trixie via Repository

### Step 1: Install Prerequisites

```bash
sudo apt install apt-transport-https wget gpg
```

### Step 2: Create Keyrings Directory

Create the directory for storing repository keys with the proper permissions:

```bash
sudo mkdir -m 0755 -p /etc/apt/keyrings/
```
The `/etc/apt/keyrings/` directory is the recommended location for manually managed repository keys in modern Debian systems.
### Step 3: Import Microsoft GPG Key

Download and add Microsoft's GPG signing key:

```bash
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/keyrings/microsoft-archive-keyring.gpg
rm -f microsoft.gpg
```

### Step 4: Add VS Code Repository

Add the official Microsoft VS Code repository:

```bash
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
```

### Step 5: Update and Install

Update your package cache and install VS Code:

```bash
sudo apt update
sudo apt install code
```

