import pytest

from engineering_toolkit.structures import bending_stress


def test_bending_stress():
    stress = bending_stress(
        moment=1000,
        distance=0.05,
        inertia=0.0001,
    )

    assert stress == pytest.approx(500000)


def test_invalid_inertia():
    with pytest.raises(ValueError):
        bending_stress(
            moment=1000,
            distance=0.05,
            inertia=0,
        )
