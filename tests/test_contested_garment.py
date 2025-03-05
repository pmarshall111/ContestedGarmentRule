import pytest
from src.contested_garment import contested_garment

@pytest.mark.parametrize("demand,supply,expected", [
    ([100,200,300], 100, [33.333,33.333,33.333]),
    ([100,200,300], 200, [50,75,75]),
    ([100,200,300], 300, [50,100,150]),
    ([100,200,300], 400, [50,125,225]),
    ([100,200,300], 500, [66.667,166.667,266.667]),
    ([100,200,300], 600, [100,200,300]),
])
def test_contested_garment(demand, supply, expected):
    allocs = contested_garment(demand, supply)
    assert allocs == pytest.approx(expected, rel=0.1)