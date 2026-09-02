"""Demonstrates symbolic vector calculus for electromagnetics using SymPy.

Calculates gradient, divergence, curl, and Laplacian of electric and
magnetic field vector functions in Cartesian coordinates.
"""

try:
    import sympy as sp
except ImportError:
    sp = None


def demonstrate_gradient() -> None:
    """Calculates electric field from scalar potential: E = -grad(V)."""
    x, y, z = sp.symbols('x y z')
    V = 4 * x**2 * y - 2 * y * z**2

    grad_x = sp.diff(V, x)
    grad_y = sp.diff(V, y)
    grad_z = sp.diff(V, z)

    E_x = -grad_x
    E_y = -grad_y
    E_z = -grad_z

    print("--- 1. Electric Field from Scalar Potential ---")
    print(f"Scalar Potential V(x,y,z) = {V}")
    print(f"Electric Field E = [{E_x}] x_hat + [{E_y}] y_hat + [{E_z}] z_hat")

    # Laplace operator on V
    laplacian_V = sp.diff(V, x, 2) + sp.diff(V, y, 2) + sp.diff(V, z, 2)
    print(f"Laplacian of V (div(grad V)) = {laplacian_V}")


def demonstrate_divergence_gauss() -> None:
    """Demonstrates Gauss's Law in differential form: div(D) = rho_v."""
    x, y, z = sp.symbols('x y z')
    D_x = x**2 * z
    D_y = 3 / y
    D_z = sp.Integer(0)

    div_D = sp.diff(D_x, x) + sp.diff(D_y, y) + sp.diff(D_z, z)

    print("\n--- 2. Gauss's Law Differential Divergence ---")
    print(f"Electric Flux Density D = [{D_x}] x_hat + [{D_y}] y_hat")
    print(f"Volume Charge Density rho_v = div(D) = {sp.simplify(div_D)}")


def demonstrate_curl_maxwell() -> None:
    """Calculates curl of magnetic field: curl(B)."""
    x, y, z = sp.symbols('x y z')
    # B = [-y, x, 0] / (x^2 + y^2) (magnetic field around infinite line current)
    denom = x**2 + y**2
    B_x = -y / denom
    B_y = x / denom
    B_z = sp.Integer(0)

    curl_x = sp.diff(B_z, y) - sp.diff(B_y, z)
    curl_y = sp.diff(B_x, z) - sp.diff(B_z, x)
    curl_z = sp.diff(B_y, x) - sp.diff(B_x, y)

    print("\n--- 3. Magnetic Field Curl (Ampere-Maxwell) ---")
    print(f"Magnetic Field B around line current:")
    print(f"  B_x = {B_x}")
    print(f"  B_y = {B_y}")
    print(f"curl(B) z-component (for r > 0) = {sp.simplify(curl_z)}")


def main() -> None:
    """Executes vector calculus demonstrations."""
    if sp is None:
        print("SymPy is not installed in the current Python environment.")
        print("Install it via: pip install sympy, or execute using an environment that has SymPy.")
        return
    demonstrate_gradient()
    demonstrate_divergence_gauss()
    demonstrate_curl_maxwell()


if __name__ == "__main__":
    main()
