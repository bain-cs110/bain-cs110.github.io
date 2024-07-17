import psonic
import random

number_of_pieces = 8

while True:
    # sample starts at 0.0 and finishes at 1.0
    for i in range(16):
        s = random.randrange(0, number_of_pieces) / number_of_pieces
        f = s + (1.0 / number_of_pieces)
        psonic.sample(psonic.LOOP_AMEN, beat_stretch=2, start=s, finish=f)
        psonic.sleep(2.0 / number_of_pieces)
