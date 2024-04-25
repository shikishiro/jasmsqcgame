image gamesplash1 = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)
image gamesplash2 = "images/splashart/JASMSLogo.png"

label splashscreen:

    $ config.main_menu_music = "audio/bgm/thememusic.mp3"
    $ renpy.music.play(config.main_menu_music)
    scene whitebg with Pause(1)
    show gamesplash1 "Disclaimer:\n All characters in this game are purely fictional and their likeness is used for entertainment purposes only.\nTheir portrayal in the game does not reflect upon any real individuals. \nFurthermore, please be advised that certain visual effects may trigger photo sensitivity.\nIf you experience any discomfort, we recommend consulting a doctor and refraining from further gameplay." with Dissolve(0.5)
    $ renpy.pause(2.0, hard=True)
    hide gamesplash1 with Dissolve(0.5)
    with Pause(1)
    $ renpy.pause(1.0, hard=True)

    show gamesplash2 with Dissolve(0.5):
        xalign 0.5
        yalign 0.5
    $ renpy.pause(2.0, hard=True)
    hide gamesplash2 with Dissolve(0.5)
    with Pause(1)
    $ renpy.pause(1.0, hard=True)
    return