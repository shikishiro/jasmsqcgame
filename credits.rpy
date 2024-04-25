label credits:
    $ config.allow_skipping = False
    image splash = Text("The JASMS QC Game", style="credit_splash", xalign=0.5, yalign=0.5)
    image cred = Text(credits_s, text_align=0.5, style="credit_splash")
    image theend = Text("The End", style="credit_splash", xalign=0.5, yalign=0.5)
    image thanks = Text("Thank you for playing!", style="credit_splash", xalign=0.5, yalign=0.5)

    $ credits_speed = 25
    scene black
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    $ renpy.pause(1.5, hard=True)
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    #with Pause(5)
    $ renpy.pause(5, hard=True)
    hide theend
    with dissolve
    with Pause(credits_speed - 5)
    $ renpy.pause(5, hard=True)
    show splash
    with dissolve
    with Pause(3)
    $ renpy.pause(5, hard=True)
    hide splash
    with dissolve
    with Pause(1)
    $ renpy.pause(5, hard=True)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    $ renpy.pause(4, hard=True)
    hide thanks
    with dissolve
    $ renpy.full_restart()

init python:
    credits = ('Story and Dialogue', 'Zophie Marie Ong'), ('Questions and Research', 'Benedict Leto Machica'), ('Music', 'Christian Guillermo'), ('Music', 'Kevin MacLeod'), ('Programming, Logic and UI', 'Teacher Melqui Amparo'), ('Character Sprites', 'NietoRiel'), ('Backgrounds', 'Benedict Leto Machica'), ('Backgrounds', 'Christian Guillermo'), ('Backgrounds', 'Rafael Tolentino'), ('Backgrounds', 'Teacher Melqui Amparo')
    credits_s = "{size=40}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1 = c[0]
    credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()