import numpy as np

U64 = np.uint64

ZERO = U64(0)
ONE = U64(1)

class Bitboard:
    @staticmethod
    def set_bit(bb: U64, square: int) -> U64:
        return bb | (ONE << U64(square))
    
    @staticmethod
    def clear_bit(bb: U64, square: int) -> U64:
        return bb & ~(ZERO << U64(square))
    
    @staticmethod
    def get_bit(bb: U64, square: int) -> bool:
        return bool(bb & (ONE << U64(square)))

    @staticmethod
    def print_bb(bb: U64, label: str = "") -> None:
        if label:
            print(f"── {label} ──")
        for rank in range(7, -1, -1):
            row = ""
            for file in range(8):
                row += "■ " if Bitboard.get_bit(bb, rank * 8 + file) else "· "
            print(f"{rank + 1} | {row}")
        print("    a b c d e f g h\n")