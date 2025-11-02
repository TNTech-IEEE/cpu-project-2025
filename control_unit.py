class ControlUnit:
    def __init__(self, i_bits: int, isa_fname: str) -> None:
        self._i_bits = i_bits

    def decode(self, instruction: int, control_lines: dict[str, int]) -> None:
        pass
