class Alu:
    def __init__(self, bits: int) -> None:
        self._bits = bits
        self._result = 0
        self._carry_out = 0

    def carry_in(self) -> None:
        self._result += 1
        self._carry_out = self._result & (2**self._bits)
        self._result &= 2**self._bits - 1

    def update_flags(self, flags: dict[str, int]) -> None:
        flags["positive"] = self._result > 0
        flags["zero"]     = self._result == 0
        flags["negative"] = self._result < 0
        flags["carry"]    = self._carry_out
