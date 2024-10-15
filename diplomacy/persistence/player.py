from __future__ import annotations

from typing import TYPE_CHECKING

from diplomacy.persistence import order

if TYPE_CHECKING:
    from diplomacy.persistence import province
    from diplomacy.persistence import unit


class Player:
    def __init__(
        self,
        name: str,
        color: str,
        vscc: int,
        iscc: int,
        centers: set[province.Province],
        units: set[unit.Unit],
    ):
        self.name: str = name
        self.color: str = color

        # victory supply center count (we assume VSCC scoring)
        self.vscc: int = vscc
        # initial supply center count
        self.iscc: int = iscc

        self.centers: set[province.Province] = centers
        self.units: set[unit.Unit] = units

        self.build_orders: set[order.PlayerOrder] = set()

    def __str__(self):
        return self.name

    def score(self):
        return (len(self.centers) - self.iscc) / (self.vscc - self.iscc)
