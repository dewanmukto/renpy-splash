label splashscreen:
    scene black
    with Pause(1)
#PLACDEHOLDER FOR ANY AUDIO FILES TO BE PLAYED
    play music "audio/menutheme.mp3" fadeout 1

    show text "Arubis Cube presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    image splash = "splash.png"
    image spl1 = "spl1.png"
    image spl2 = "spl1.png"
    image spl3 = "spl3.png"

    scene black
    with Pause(1)


    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

#THIS IS A PLACEHOLDER FOR ANY TEXT TO BE INCLUDED AS A DIALOGUE SCREEN RIGHT BEFORE RETURNING TO THE MAIN MENU.
    "Disclaimer : This game does not contain the malware dealt with in the story. (CLICK TO CONTINUE)"

    show spl1 with dissolve
    with Pause(1)
    #show spl2
    #with Pause(0.1)
    #show spl3
    #with Pause(0.1)



    return
