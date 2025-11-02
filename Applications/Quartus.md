# Installing Intel Quartus Prime Lite 20.1 on Linux

Version **20.1** is the most stable Quartus release for Linux systems (at least in my opinion).

***

## Prerequisites

### Download Required Files

Navigate to the official Intel download page and obtain the installation archive:

**Download URL:** `https://www.intel.com/content/www/us/en/software-kit/661017/intel-quartus-prime-lite-edition-design-software-version-20-1-for-linux.html`

**File:** `Quartus-lite-20.1.0.711-linux.tar`

***

## Installation Process

### Step 1: Enable 32-bit Architecture

Quartus Prime requires 32-bit libraries. Configure your system to support them:

```bash
sudo dpkg --add-architecture i386
sudo apt update
```

### Step 2: Install Core Dependencies

Install essential 32-bit libraries and development tools:

```bash
sudo apt install libc6:i386 libncurses6:i386 libxtst6:i386 libxft2:i386 \
libstdc++6:i386 lib32z1 libbz2-1.0:i386 libx11-6:i386 libxau6:i386 \
libxdmcp6:i386 libxext6:i386 libxrender1:i386 libxt6:i386 libexpat1:i386 \
fontconfig:i386 libfreetype6:i386 libice6:i386 libsm6:i386
```

### Step 3: Install Development Tools

Required for ModelSim simulation support :

```bash
sudo apt install gcc-multilib g++-multilib build-essential
```

### Step 4: Optional GTK+ Libraries

Improves GUI compatibility:

```bash
sudo apt install libgtk-3-0:i386 libcanberra0:i386
```

### Step 5: Update System

Ensure all packages are current:

```bash
sudo apt update
sudo apt upgrade
```

### Step 6: Extract and Install Quartus

Extract the downloaded archive and run the installer :

```bash
tar -xvf Quartus-lite-20.1.0.711-linux.tar
chmod u+x install.sh
./install.sh
```

**Recommended:** Reboot after installation completes:

```bash
sudo reboot
```

***

## Advanced Configuration

### Only for Non-20.1 Versions or ModelSim Edge Cases

These fixes address compatibility issues.

#### ModelSim vco Script Fix

The vco script searches for incorrect directories on Debian systems. Apply this fix if ModelSim fails to launch:

```bash
chmod u+w ~/intelFPGA_lite/20.1/modelsim_ase/vco
nano ~/intelFPGA_lite/20.1/modelsim_ase/vco
```

**Change line 13 from:**
```
mode=${MTI_VCO_MODE:-""}
```

**to:**
```
mode=${MTI_VCO_MODE:-"32"}
```

**Change line 211 from:**
```
*) vco="linux_rh60" ;;
```

**to:**
```
*) vco="linux" ;;
```

#### Permission Fix for ModelSim

The tcl.fs cache file requires read permissions :

```bash
chmod -R +r ~/intelFPGA_lite/20.1/modelsim_ase/
```

#### EDA Tool Path Configuration

Set ModelSim path in Quartus if automatic detection fails :

Navigate to: **Tools → Options → EDA Tool Options**

Set path to: `~/intelFPGA_lite/20.1/modelsim_ase/bin`

#### libncurses5 Symlink

Debian Trixie and newer use libncurses6 by default :

```bash
sudo ln -s /lib/i386-linux-gnu/libncurses.so.6 /lib/i386-linux-gnu/libncurses.so.5
```

#### libpng12 Legacy Support

Compile from source or obtain a usr-merge compatible package.

#### Freetype 2.4.12 for ModelSim

Only needed if encountering `libfreetype.so.6: cannot open shared object file` errors :

```bash
wget https://sourceforge.net/projects/freetype/files/freetype2/2.4.12/freetype-2.4.12.tar.bz2
tar xjf freetype-2.4.12.tar.bz2
cd freetype-2.4.12/
./configure --build=i686-pc-linux-gnu "CFLAGS=-m32" "CXXFLAGS=-m32" "LDFLAGS=-m32"
make
sudo make install
```

Copy compiled libraries to ModelSim directory:

```bash
mkdir ~/intelFPGA_lite/20.1/modelsim_ase/lib32
cp objs/.libs/libfreetype.so* ~/intelFPGA_lite/20.1/modelsim_ase/lib32/
```

***

## Verification

Launch Quartus from terminal to verify installation:

```bash
~/intelFPGA_lite/20.1/quartus/bin/quartus
```