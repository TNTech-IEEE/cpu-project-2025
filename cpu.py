import ControlUnit
import RegisterFile
import ArithmeticLogicUnit

class CentralProcessingUnit:
    data_length = 16

    control_lines = {
        "immediate"   : 0,
        "signed ext"  : 0,
        "read ra"     : 0,
        "read rb"     : 0,
        "r writeback" : 0,
        "mem read"    : 0,
        "mem write"   : 0,
        "stack ptr"   : 0,
        "lr read"     : 0,
        "lr write"    : 0,
        "jump"        : 0,
        "alu"         : 0,
        "update flags": 0,
        "read flags"  : 0
    }

    control_unit = ControlUnit()
    registers = RegisterFile(n_gprs=8, zero_reg=True, bits=data_length)
    alu = ArithmeticLogicUnit(bits=data_length)
