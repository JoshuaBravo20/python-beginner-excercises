def sing():
    song = ""
    l = 'let it be,\n'
    w =  "whisper words of wisdom, let it be, let it be,\n"
    t = "there will be an answer, let it be"

    for x in range(0,4):
        song = song + l
    song = song + w
    for x in range(0,3):
        song = song + l
    song = song + t

    print(song)
        

sing()



    




