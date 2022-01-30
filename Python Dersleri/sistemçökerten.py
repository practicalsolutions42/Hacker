import random

for i in range(5):
    açılacak_dosya = open("sil" + str(i) + ".txt", "w")

    for a in range (50):
        açılacak_dosya.write(str(random.randint(5846437694797869673,674874669269832952)))