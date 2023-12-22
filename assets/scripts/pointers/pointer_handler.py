from ...typing import Address

from ctypes import cast, py_object

def from_address(address: Address) -> py_object:
    # split the address
    return cast(address, py_object).value

# Path: assets/scripts/pointers/from_address.py