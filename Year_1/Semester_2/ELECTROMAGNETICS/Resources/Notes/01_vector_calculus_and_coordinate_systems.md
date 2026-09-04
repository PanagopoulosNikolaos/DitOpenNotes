# Vector Calculus and Coordinate Systems for Electromagnetics

## Overview
Electromagnetic field theory is formulated mathematically using vector calculus across three orthogonal curvilinear coordinate systems: Cartesian $(x, y, z)$, Cylindrical $(\rho, \phi, z)$, and Spherical $(r, \theta, \phi)$.

---

## 1. Differential Vector Operators

### 1.1 Gradient ($\nabla V$)
The gradient of a scalar potential field $V$ represents the maximum spatial rate of increase and its direction:
* **Cartesian**:
  $$\nabla V = \frac{\partial V}{\partial x} \hat{\mathbf{a}}_x + \frac{\partial V}{\partial y} \hat{\mathbf{a}}_y + \frac{\partial V}{\partial z} \hat{\mathbf{a}}_z$$
* **Cylindrical**:
  $$\nabla V = \frac{\partial V}{\partial \rho} \hat{\mathbf{a}}_\rho + \frac{1}{\rho}\frac{\partial V}{\partial \phi} \hat{\mathbf{a}}_\phi + \frac{\partial V}{\partial z} \hat{\mathbf{a}}_z$$
* **Spherical**:
  $$\nabla V = \frac{\partial V}{\partial r} \hat{\mathbf{a}}_r + \frac{1}{r}\frac{\partial V}{\partial \theta} \hat{\mathbf{a}}_\theta + \frac{1}{r\sin\theta}\frac{\partial V}{\partial \phi} \hat{\mathbf{a}}_\phi$$

### 1.2 Divergence ($\nabla \cdot \mathbf{A}$)
The divergence represents the net outward flux of a vector field per unit volume:
* **Cartesian**:
  $$\nabla \cdot \mathbf{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}$$
* **Cylindrical**:
  $$\nabla \cdot \mathbf{A} = \frac{1}{\rho}\frac{\partial (\rho A_\rho)}{\partial \rho} + \frac{1}{\rho}\frac{\partial A_\phi}{\partial \phi} + \frac{\partial A_z}{\partial z}$$
* **Spherical**:
  $$\nabla \cdot \mathbf{A} = \frac{1}{r^2}\frac{\partial (r^2 A_r)}{\partial r} + \frac{1}{r\sin\theta}\frac{\partial (\sin\theta A_\theta)}{\partial \theta} + \frac{1}{r\sin\theta}\frac{\partial A_\phi}{\partial \phi}$$

### 1.3 Curl ($\nabla \times \mathbf{A}$)
The curl measures the rotational circulation density of a vector field:
* **Cartesian**:
  $$\nabla \times \mathbf{A} = \begin{vmatrix} \hat{\mathbf{a}}_x & \hat{\mathbf{a}}_y & \hat{\mathbf{a}}_z \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ A_x & A_y & A_z \end{vmatrix}$$

---

## 2. Integral Theorems

### 2.1 Divergence Theorem (Gauss's Theorem)
Relates the surface flux of a vector field over a closed boundary to the volume integral of its divergence:
$$\oint_S \mathbf{A} \cdot d\mathbf{S} = \int_V (\nabla \cdot \mathbf{A}) \, dv$$

### 2.2 Stokes' Theorem
Relates the line integral of a vector field along a closed contour to the surface flux of its curl:
$$\oint_C \mathbf{A} \cdot d\mathbf{l} = \int_S (\nabla \times \mathbf{A}) \cdot d\mathbf{S}$$

### 2.3 Fundamental Null Identities
1. The curl of any gradient field is identically zero (conservative field):
   $$\nabla \times (\nabla V) = \mathbf{0}$$
2. The divergence of any curl field is identically zero (solenoidal field):
   $$\nabla \cdot (\nabla \times \mathbf{A}) = 0$$

