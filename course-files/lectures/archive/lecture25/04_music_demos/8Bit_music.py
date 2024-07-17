import psonic

for i in range(10):
    psonic.use_synth(psonic.SAW)
    psonic.play(38)
    psonic.sleep(0.25)
    psonic.play(50)
    psonic.sleep(0.5)

    if i % 2 == 0:
        psonic.use_synth(psonic.PROPHET)
        psonic.play(57)
        psonic.sleep(0.5)
