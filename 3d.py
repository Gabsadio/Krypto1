# Gibt Liste mit den moeglichen Inputs fuer die S-Box i mit Output output:
def S(i, output):
    inputs = []
    s_box = [
        # S1
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
        ],
        # S2
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],
        # S3
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],
        # S4
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
        ],
        # S5
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        ],
        # S6
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
        ],
        # S7
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
        ],
        # S8
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
        ],
    ]
    for row in range(4):
        for col in range(16):
            if s_box[i][row][col] == output:
                inputs.append(
                    [int(b) for b in f"{(row//2)%2}" + f"{col:04b}" + f"{row%2}"]
                )
    return inputs


# Gegebene Klartext-Chiffrat-Paare:
x1 = 0xE349EDBF2E8A749D
y1 = 0x2E8A749D1045F2BA
x2 = 0x1349114115611E91
y2 = 0x15611E919329E839

# Wandle in Listen von Bits um:
x1 = [int(b) for b in f"{x1:064b}"]
y1 = [int(b) for b in f"{y1:064b}"]
x2 = [int(b) for b in f"{x2:064b}"]
y2 = [int(b) for b in f"{y2:064b}"]

# Berechne Output der f-Funktion:
output1 = [y1[32:][i] ^ x1[:32][i] for i in range(32)]
output2 = [y2[32:][i] ^ x2[:32][i] for i in range(32)]

# Wende P^-1 auf Output an:
PInv = [
    9,
    17,
    23,
    31,
    13,
    28,
    2,
    18,
    24,
    16,
    30,
    6,
    26,
    20,
    10,
    1,
    8,
    14,
    25,
    3,
    4,
    29,
    11,
    19,
    32,
    12,
    22,
    7,
    5,
    27,
    15,
    21,
]
inv1 = [output1[PInv[i] - 1] for i in range(32)]
inv2 = [output2[PInv[i] - 1] for i in range(32)]

# Berechne Ausgaenge der S-Boxen:
SOut1 = [int("".join(map(str, inv1[4 * i : 4 * (i + 1)])), base=2) for i in range(8)]
SOut2 = [int("".join(map(str, inv2[4 * i : 4 * (i + 1)])), base=2) for i in range(8)]

# Bestimme die moeglichen Eingaben in die S-Boxen:
SIn1 = [S(i, SOut1[i]) for i in range(8)]
SIn2 = [S(i, SOut2[i]) for i in range(8)]

# Berechne den Ausgang der Expansions-Funktion:
E = [
    32,
    1,
    2,
    3,
    4,
    5,
    4,
    5,
    6,
    7,
    8,
    9,
    8,
    9,
    10,
    11,
    12,
    13,
    12,
    13,
    14,
    15,
    16,
    17,
    16,
    17,
    18,
    19,
    20,
    21,
    20,
    21,
    22,
    23,
    24,
    25,
    24,
    25,
    26,
    27,
    28,
    29,
    28,
    29,
    30,
    31,
    32,
    1,
]
OutE1 = [x1[32:][E[i] - 1] for i in range(48)]
OutE2 = [x2[32:][E[i] - 1] for i in range(48)]

# Konstruiere mit beiden Paaren Schluessel und breche ab, wenn sie uebereinstimmen:
keys1 = [None] * (4**8)
keys2 = [None] * (4**8)
for i in range(4**8):
    choice = [int(f"{i:016b}"[2*j : 2*(j+1)], base=2) for j in range(8)]
    key1 = []
    key2 = []
    for j in range(8):
        key1.extend(SIn1[j][choice[j]])
        key2.extend(SIn2[j][choice[j]])
    keys1[i] = [key1[j] ^ OutE1[j] for j in range(48)]
    keys2[i] = [key2[j] ^ OutE2[j] for j in range(48)]

for i in range(4**8):
    if keys1[i] in keys2:
        key = keys1[i]
        break

key = "".join(map(str,key))
print(f"Der gesuchte Rundenschluessel lautet: key = 0x{int(key, base=2):012x}")
