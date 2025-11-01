class RegisterFile:
    def __init__(self, n_gprs: int, zero_reg: bool) -> None:
        """
        Args:
        n_gprs  : int       The number of general purpose registers
        zero_reg: bool      True if there is a zero register False otherwise

        Attributes:
        lr      : int       The link register value
        sp      : int       The stack pointer value
        """
        self._zero_reg = zero_reg
        self._gprs = [0] * n_gprs

        self.lr = 0
        self.sp = 0

    def read(self, reg_a: int, reg_b: int = 0) -> tuple[int, int]:
        """Reads values from register a and register b"""
        return (self._gprs[reg_a], self._gprs[reg_b])

    def write(self, reg: int, val: int) -> None:
        """Writes value to register"""
        if reg == 0 and self._zero_reg: # cannot write to zero register
            return

        self._gprs[reg] = val
