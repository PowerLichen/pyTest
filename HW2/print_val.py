# Print integer
"""
  Project: Print integer
  Author: Minsu Choe
  Date of last update: Mar. 12, 2021
"""

# print init column
print("===print int for DEC, BIN, OCT, HEX===")
print("{:^10s}|{:^10s}|{:^10s}|{:^10s}".format("DEC","BIN","OCT","HEX"))
print("="*43)

# print integer to DEC, BIN, OCT, HEX
for i in range(0, 256):
    print("{0:10d}|{0:10b}|{0:10o}|{0:10x}".format(i))

