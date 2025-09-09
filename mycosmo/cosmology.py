"""Cosmology.

This module implements various cosmology routines.

"""

import numpy as np

from .constants import G, Mpc

"""
Hubble Parameter (H(z)) as a function of redshift in a matter-dominated universe
"""

# Hard-coded cosmological parameters
"""
def hubble(redshift):
    hubble_const = 0.7
    matter = 0.3 * (1 + redshift) ** 3
    curvature = 0.0 * (1 + redshift) ** 2
    dark_energy = 0.7

    return np.sqrt(hubble_const**2 * (matter + curvature + dark_energy))
"""


# Dictionary object as an argument
# better : add the function to a class and make these constants class attributes
def hubble(redshift, cosmo_dict):
    r"""Hubble Parameter.

    Calculate the Hubble parameter at a given redshift using the cosmological parameter values provided.

    Parameters
    ----------
    redshift : float or numpy.ndarray
        Redshift(s) at which the Hubble parameter should be calculated
    cosmo_dict : dict
        Dictionary of cosmological constants. Must contain the following keys:

        * ``H0``: The Hubble parameter value at redshift zero.
        * ``omega_m_0``: The matter density at redshift zero.
        * ``omega_k_0``: The curvature density at redshift zero.
        * ``omega_lambda_0``: The dark energy density at redshift zero.

    Returns
    -------
    float or numpy.ndarray
    Value of the Hubble parameter (km s⁻¹ Mpc⁻¹) at the specified redshift(s) for a given cosmology.

    Notes
    -----
    This function implements the calculation of the Hubble parameter as follows:

    .. math::
        H(z) = \sqrt{H_0^2 (\Omega_{m,0}(1+z)^3 + \Omega_{k,0}(1+z)^2 +
            \Omega_{\Lambda,0})}

    Example
    -------
    >>> from mycosmo.cosmology import hubble
    >>> cosmo_dict = {"H0": 70, "omega_m_0": 0.3, "omega_k_0": 0.0, "omega_lambda_0": 0.7}
    >>> hubble(0.0, cosmo_dict)
    70.0

    """

    hubble_const = cosmo_dict["H0"]
    matter = cosmo_dict["omega_m_0"] * (1 + redshift) ** 3
    curvature = cosmo_dict["omega_k_0"] * (1 + redshift) ** 2
    dark_energy = cosmo_dict["omega_lambda_0"]

    return np.sqrt(hubble_const**2 * (matter + curvature + dark_energy))


def critical_density(redshift, cosmo_dict):
    r"""Critical density.

    Calculate the critical density of the Universe at a given redshift using the cosmological parameter values provided.

    Parameters
    ----------
    redshift : float or numpy.ndarray
        Redshift(s) at which the Hubble parameter should be calculated
    cosmo_dict : dict
        Dictionary of cosmological constants. Must contain the following keys:

        * ``H0``: The Hubble parameter value at redshift zero.
        * ``omega_m_0``: The matter density at redshift zero.
        * ``omega_k_0``: The curvature density at redshift zero.
        * ``omega_lambda_0``: The dark energy density at redshift zero.

    Returns
    -------
    float or numpy.ndarray
    Value of the critical density (kg m⁻³) at the specified redshift(s) for a given cosmology.

    Notes
    -----
    This function implements the calculation of the critical density as follows:

    .. math::
        \rho(z) = \frac{3 H(z)^2}{8 \pi G}

    Example
    -------
    >>> from mycosmo.cosmology import critical_density
    >>> cosmo_dict = {"H0": 70, "omega_m_0": 0.3, "omega_k_0": 0.0, "omega_lambda_0": 0.7}
    >>> critical_density(0.0, cosmo_dict)
    9.20e-27

    """

    H_z_si = hubble(redshift, cosmo_dict) * 1e3 / Mpc

    return (3.0 * H_z_si**2) / (8.0 * np.pi * G)
