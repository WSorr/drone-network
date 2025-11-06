import pytest
from drone_network.drone import GenesisDrone


def test_proto_drone_creation():
    genesis = GenesisDrone()
    proto = genesis.create_proto_drone()
    assert proto.starters == genesis.starters
