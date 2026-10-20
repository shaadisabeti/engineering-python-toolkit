def bending_stress(
    moment: float,
    distance: float,
    inertia: float,
) -> float:
    """
    Calculate normal bending stress in a beam.

    Parameters
    ----------
    moment : float
        Bending moment [N*m].
    distance : float
        Signed distance from neutral axis [m].
    inertia : float
        Second moment of area [m^4].

    Returns
    -------
    float
        Bending stress [Pa].
    """
    if inertia <= 0:
        raise ValueError("Second moment of area must be positive.")

    return moment * distance / inertia
