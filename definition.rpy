## Characters

define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = Character("[player]", ctc="ctc", ctc_position="fixed")
define k = Character("Kairos", who_color= "#a6a6ed", ctc="ctc", ctc_position="fixed")
define u = Character("???", who_color= "#a6a6ed", ctc="ctc", ctc_position="fixed")
define u2 = Character("???", who_color= "#800000", ctc="ctc", ctc_position="fixed")
define u3 = Character("???", who_color= "#c4c402", ctc="ctc", ctc_position="fixed")
define u4 = Character("???", who_color= "#006700", ctc="ctc", ctc_position="fixed")
define u5 = Character("???", who_color= "#2c80ff", ctc="ctc", ctc_position="fixed")
define u6 = Character("???", who_color= "#ff87eb", ctc="ctc", ctc_position="fixed")
define u7 = Character("???", who_color= "#ff8000", ctc="ctc", ctc_position="fixed")
define md = Character("Midnight", who_color= "#ff8000", ctc="ctc", ctc_position="fixed")
define g1 = Character("Guard 1", who_color="#f04040", ctc="ctc", ctc_position="fixed")
define g2 = Character("Guard 2", who_color="#bb1313", ctc="ctc", ctc_position="fixed")
define s1 = Character("Student 1", who_color="#108310", ctc="ctc", ctc_position="fixed")
define s2 = Character("Student 2", who_color="#838302", ctc="ctc", ctc_position="fixed")
define t1 = Character("Teacher 1", who_color="#B95CF4", ctc="ctc", ctc_position="fixed")
define sk = Character("Teacher Mel", who_color="#B95CF4", ctc="ctc", ctc_position="fixed")

## Images
image whitebg = "images/splashart/whitebg.png"

# Characters

# Guard1
image guard1 exp = "images/sprites/guarda/Guard A_Explaining.png"
image guard1 und = "images/sprites/guarda/Guard A_Understanding.png"
image guard1 wary = "images/sprites/guarda/Guard A_Wary.png"

# Guard2
image guard2 exp = "images/sprites/guardb/Guard B_Explaining.png"
image guard2 und = "images/sprites/guardb/Guard B_Understanding.png"
image guard2 wary = "images/sprites/guardb/Guard B_Wary.png"

# Student1
image student1 calm = "images/sprites/studenta/Student A_Calm.png"
image student1 curious = "images/sprites/studenta/Student A_Curious.png"
image student1 excited = "images/sprites/studenta/Student A_Excited.png"
image student1 explaining = "images/sprites/studenta/Student A_Explaining.png"
image student1 understanding = "images/sprites/studenta/Student A_Understanding.png"

# Student2
image student2 shy = "images/sprites/studentb/Student B_Shy.png"
image student2 surprised = "images/sprites/studentb/Student B_Surprised.png"
image student2 thankful = "images/sprites/studentb/Student B_Thankful.png"
image student2 worried = "images/sprites/studentb/Student B_Worried.png"

# Teacher
image teacher explaining = "images/sprites/teacher/Teacher_Explaining.png"
image teacher kind = "images/sprites/teacher/Teacher_Kind.png"
image teacher understanding = "images/sprites/teacher/Teacher_Understanding.png"

# Kairos
image kairos alarmed = "images/sprites/kairos/Kairos_Alarmed.png"
image kairos annoyed = "images/sprites/kairos/Kairos_Annoyed.png"
image kairos calm = "images/sprites/kairos/Kairos_Calm.png"
image kairos confident = "images/sprites/kairos/Kairos_Confident.png"
image kairos eager = "images/sprites/kairos/Kairos_Eager.png"
image kairos manic = "images/sprites/kairos/Kairos_Manic.png"
image kairos surprised = "images/sprites/kairos/Kairos_Surprised.png"

# Midnight
image midnight anticipating = "images/sprites/midnight/Midnight_Anticipating.png"
image midnight back_turned = "images/sprites/midnight/Midnight_Back Turned.png"
image midnight prepared = "images/sprites/midnight/Midnight_Prepared.png"

## Backgrounds
image admin = "images/backgrounds/admin.png"
image chemlab1 = "images/backgrounds/chemlab1.png"
image chemlab2 = "images/backgrounds/chemlab2.png"
image clouds = "images/backgrounds/clouds.png"
image cr4 = "images/backgrounds/cr4.png"
image faculty = "images/backgrounds/faculty.png"
image fishtank = "images/backgrounds/fishtank.png"
image floor2a = "images/backgrounds/floor2a.png"
image floor2b = "images/backgrounds/floor2b.png"
image floor3 = "images/backgrounds/floor3.png"
image floor4 = "images/backgrounds/floor4.png"
image floor5 = "images/backgrounds/floor5.png"
image gate1 = "images/backgrounds/gate1.png"
image gate2 = "images/backgrounds/gate2.png"
image gr11ar = "images/backgrounds/gr11ar.png"
image gr12aq = "images/backgrounds/gr12aq.png"
image gym = "images/backgrounds/gym.png"
image library = "images/backgrounds/library.png"
image moon = "images/backgrounds/moon.png"
image preschool = "images/backgrounds/preschool.png"
image rooftopa = "images/backgrounds/rooftopa.png"
image rooftopb = "images/backgrounds/rooftopb.png"
image white = "images/backgrounds/white.png"

## Gameover ##
default gameover_meaning = ""

## Flags and Scores ##


## Configs ##
define config.allow_skipping = False

## SFX ##
define -2 gui.hover_sound = "audio/sfx/hover.ogg"
define -2 gui.activate_sound = "audio/sfx/click.ogg"

#FX
define audio.birds = "audio/sfx/birds.mp3"
define audio.whoosh = "audio/sfx/whoosh.mp3"
define audio.paper = "audio/sfx/paper.mp3"
define audio.bigboom = "audio/sfx/boom.mp3"
define audio.ouch = "audio/sfx/ouch.mp3"
define audio.portal = "audio/sfx/portal.mp3"

#Music
define audio.ending = "audio/bgm/thememusic.mp3"
define audio.piano = "audio/bgm/A Very Brady Special.mp3"
define audio.kairostheme = "audio/bgm/Vanishing.mp3"
define audio.battle = "audio/bgm/INTENSE BATTLE MUSIC.mp3"
define audio.awkward = "audio/bgm/Sneaky Adventure.mp3"
define audio.s1theme = "audio/bgm/Cheery Monday.mp3"
define audio.sad = "audio/bgm/Mana Two - Part 1.mp3"
define audio.s2theme = "audio/bgm/Doobly Doo.mp3"
define audio.t1theme = "audio/bgm/Past Sadness.mp3"
define audio.g2theme = "audio/bgm/With a Creation.mp3"
define audio.sus = "audio/bgm/Crypto.mp3"
define audio.sus2 = "audio/bgm/I Can Feel it Coming.mp3"
define audio.will1 = "audio/bgm/Tempting Secrets.mp3"
define audio.solo = "audio/bgm/Lone Harvest.mp3"
define audio.mid = "audio/bgm/Southern Gothic.mp3"
define audio.hype = "audio/bgm/Killers.mp3"
define audio.finalhype = "audio/bgm/Undaunted.mp3"

# 
init python:
    _game_menu_screen = "history" 