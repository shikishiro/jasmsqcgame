label start:
    $ quick_menu = False
    $ correct_count = 0
    $ correct_count_gate = 0
    $ correct_count_gfloor = 0
    $ correct_count_2floor = 0
    $ correct_count_3floor = 0
    $ correct_count_4floor = 0
    $ correct_count_5floor = 0
    $ correct_count_roof = 0
    $ correct_count_boss1 = 0
    $ correct_count_final_battle = 0
    $ config.rollback_enabled = False


label start_a:
    stop music fadeout 2.0
    scene black with dissolve
    pause (2.0)
    call screen dialog ("""
    Welcome to the JASMS QC Game!
    Before we start, we need to know your name so that we can properly address you.
    """, Return(True))

label start_loop:
    $ valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    $ max_length = 10

    $ player = renpy.input("Please enter your name.", allow=valid_chars)

    if len(player) > max_length:
        $ player = player[:max_length]

    if player == "":
        "Sorry, but we need to know your name in order to proceed."
        jump start_loop

    "Your name is [player], correct?"
    "You can still change your name if you want to."

    menu:
        "Yes, that's my name.":
            "Great! Let's get started then."
            jump start_actual
        "No, I want to change it.":
            jump start_loop

label start_actual:
    $ quick_menu = True
    $ config.allow_skipping = True

    scene clouds with Dissolve(2.0)
    play sound birds fadein (1.0)
    play music piano fadein (1.0)
    pause(2.0)
    "I opened my eyes, and I saw the sky."
    "The sun had just risen, and its light illuminated the dim streets of the city."
    "I tried to get up from where I was , but accidentally kicked up a cloud of dust in the process."
    "Good job, me."
    "After the coughing fit was over, I observed my surroundings."
    "I must've blacked out at some point, but can't remember anything that happened before that."
    "How long have I been out cold?"

    "Come to think of it, what was this place?"
    scene gate1 with dissolve
    "There were transport vehicles of sorts running down the gray roads, and I saw people walking into a variety of buildings, each with different aspirations and purposes."
    "There was little to no wildlife roaming around, and the trees were lined up between the lanes of travel."
    "And the noise."
    "Everything was so loud, yet so silent."
    "It was a cacophony of foreign sensations, threatening to wrap me in fear."
    "This whole situation was strange."
    "As I looked around the area, my eyes locked on to a nearby building that laid across my position."
    "I felt frawn to its towering shades of white, adorned with streaks of maroon running in between."
    "The plaque above the entrance read {color=#93282C}'Jose Abad Santos Memorial School'{/color}."
    "It seemed to be an academy of sorts. Maybe I can get information from there. Learned more about this town while I'm at it."
    "Perhaps it will lead to something new."

    scene gate2 with wipeleft_scene
    stop sound fadeout 1.0
    stop music fadeout 1.0
    play music kairostheme fadein (1.0)
    show kairos calm zorder 2 at f11
    u "Hello?"
    show kairos calm zorder 2 at t11
    "Before I could take a step, something entered my head. Someone, rather."
    show kairos confident zorder 2 at f11
    u "You don't remember, do you?"
    show kairos confident zorder 2 at t11
    mc "Remember what?"
    show kairos eager zorder 2 at f11
    u "Is this how you cope with your failures? By pushing them to the back of your mind until your memories cease to exist? Even here, you're still sad and pathetic."
    show kairos eager zorder 2 at t11
    mc "What failures? Who even are you?"
    show kairos annoyed zorder 2 at f11
    u "Who am I?"
    u "That's something for you to recall."
    show kairos calm zorder 2 at f11
    u "But that's not why I'm here."
    show kairos confident zorder 2 at f11
    u "I'm here to give you a little warm up."
    u "I'll present a question, and you will answer it to the best of your ability."
    u "You'll have to get to the end to see how well you did."
    show kairos annoyed zorder 2 at f11
    u "It's not how I'd usually test people, but it's a change, I supposed."
    u "Especially since there's no energy here."
    show kairos calm zorder 2 at f11
    u "Better hope you don't embarrass yourself in the first round."

    call screen dialog ("""
    Tutorial:
    Playing the JASMS Game, you will encounter a series of questions that you must answer correctly.
    There will be 5 questions in total for each encounter.
    You will be given four choices, and you must select the correct answer.
    There is no time limit, so take your time.
    """, Return(True))
    show kairos calm at thide zorder 1
    hide kairos

    call quiz_tutorial

label tutorial_cont:
    $ quick_menu = True
    play music kairostheme fadein (1.0)

    scene gate2 with pixellate
    if correct_count >= 3:
        show kairos calm zorder 2 at t11
        u "..."
        show kairos confident zorder 2 at f11
        u "Well, well."
        u "You were able to keep up."
        show kairos eager zorder 2 at f11
        u "Some of this subject matter doesn't even exist back home."
    
    else:
        show kairos calm zorder 2 at t11
        u "..."
        show kairos annoyed zorder 2 at f11
        u "Messing up this early?"
        u "You'll embarrass yourself sooner or later."
        u "Since you're still unaccustomed to this place, it's not too bad."

    show kairos calm zorder 2 at f11
    u "Well, whatever. That was just the first run, after all."
    u "You better be prepared for more."
    show kairos confident zorder 2 at f11
    u "Don't disappoint me. I'll be waiting for you."
    show kairos confident at thide zorder 1
    hide kairos
    
    "..."
    "What was that?"
    "For some reason, they felt very familiar."
    "But I don't remember why..."
    "I suppose I shouldn't dwell on it too much. Time to head to that school."
    stop music fadeout 1.0


label start_gate:
    play music piano fadein (1.0)
    scene gate1 with wipeleft_scene

    "Crossing the road has always been a tricky thing for me. I was always the type of person would charge ahead without a care in the world, even if the road wasn't safe to cross."
    "But when you risk getting injured by vehicles way faster than horses, every safety precaution becomes much more important."

    scene gate2 with wipeleft_scene
    "Now that I was closer, I could see the outside more clearly."
    "There were spaces with those weird vehicles parked, and I could see various people making their way inside."
    "Right ahead of me was a young student, hoisting a bag."
    "They were checking in with what I assume were the place's security guards"
    "The student was wearing a uniform with the same colors as the building. Perhaps those were the school's official colors."
    "With newfound curiousity, I stepped through the entrance."
    "It wasn't long before I was noticed."
    stop music
    play music awkward
    show guard1 wary zorder 2 at f22
    show student1 calm zorder 3 at s21
    g1 "Who are you? You look unfamiliar."
    show guard1 wary zorder 2 at t22
    show student1 curious zorder 3 at f21
    s1 "Are you a visitor, perhaps? I don't remember seeing you around in school before."
    show student1 curious zorder 3 at t21
    "Aha, The perfect excuse! Now I have to hope it sticks."
    mc "I'm [player], and I happen to be a traveler from abroad. I was interested in finding a place to learn, so I came here upon a recommendation as a transferee."
    "The guard turned and whispered something to another, who took their position at the entrance while the student and I were scooted off to the side."
    show guard1 wary zorder 2 at f22
    g1 "Hmm... I don't remember you being mentioned anywhere recently. The principal would surely know of any incoming students."
    show guard1 wary zorder 3 at t22
    "I hid my apprehension as best as I could, but it was already beginning to bubble within me."
    "What if I got thrown out?"
    show guard1 und zorder 2 at f22
    g1 "But a visitor with interest to learn is always welcome."
    show guard1 exp zorder 3 at f22
    g1 "Now, to be sure of your love for learning, let me give you a little test."
    show guard1 und zorder 3 at t22
    "Here we go again. At least I have an idea as to what I should expect."
    show student1 curious at thide zorder 1
    show guard1 und at thide zorder 1
    hide student1
    hide guard1

    call quiz_gate

label gate_cont:
    scene gate2 with pixellate
    play music piano fadein (1.0)
    $ quick_menu = True
    
    if correct_count_gate >= 3:
        show guard1 wary zorder 2 at t11
        g1 "..."
        show guard1 wary zorder 2 at f11
        g1 "Hmm..."
        show guard1 und zorder 2 at f11
        g1 "That wasn't too bad."
    else:
        show guard1 wary zorder 2 at t11
        g1 "..."
        show guard1 wary zorder 2 at f11
        g1 "Hmm..."
        show guard1 exp zorder 2 at f11
        g1 "Maybe there's a learning gap somewhere?"
        show guard1 und zorder 2 at f11
        g1 "Well, it's not too important."


    g1 "Alright, kid. Now that's the test is over, is there something you want to ask?"
    show guard1 und zorder 2 at t11
    mc "For a start, I'd like to learn more about this school."
    play music s1theme fadein (1.0)
    show guard1 und zorder 2 at t44
    show student1 excited zorder 3 at f11
    s1 "Oh, I can answer that!"
    show student1 excited zorder 3 at t11
    "The student from earlier piped up, looking excited."
    show student1 explaining zorder 3 at f11
    s1 "This school is an acknowledged pioneer in progressive education, and we believe learning to be free is one of the most important lesson in life."
    show student1 understanding zorder 3 at f11
    s1 "We all have one shot at life, so it's important that our childhoods are filled with love and hapiness."
    show student1 explaining zorder 3 at f11
    s1 "The school was named after one of our great patriots, who sought to liberate his people 300 years ago."
    show student1 explaining zorder 3 at t11
    mc "That's interesting. Never heard of anything like it back home."
    show student1 explaining zorder 3 at t21
    show guard1 exp zorder 2 at t22
    "The guard paused in thought for a moment before turning to the other student."

    show guard1 und zorder 2 at f22
    g1 "You know, since you look interested in this kid, why not give them a tour?"
    g1 "It's still early, you'll have lots of time to go around."
    show guard1 und zorder 2 at t22
    show student1 excited zorder 3 at f21
    s1 "You've got it!"
    show student1 understanding zorder 3 at f11
    show guard1 und at thide zorder 2
    hide guard1
    s1 "Come on, [player], let's go! We'll start here."
    "They took my hand, and we headed deeper into the school."
    show student1 understanding at thide zorder 3
    hide student1
    stop music fadeout 1.0

label ground_floor:
    scene preschool with wipeleft_scene
    play music piano fadein(1.0)
    "This place was surprisingly huge. Even if the classrooms were mostly empty, I could see the arrangements and materials inside the darkness."
    "There were tables, chairs, shelves, and large black rectangular devices. There were also a multitude of books and supplies ready to be used."
    "This student and I got to know each other a little more while we walked down the hallways. They were really pleasant to be around."
    show student1 explaining zorder 2 at f11
    s1 "-and then they had to sit in the corner for the rest of the period! They really had it coming, didn't they?"
    show student1 explaining zorder 2 at t11
    mc "Yeah, you can say that again. It was hilarious, though."
    show student1 calm zorder 2 at f11
    s1 "I've told you a lot, haven't I? Now I want to know more about you."
    show student1 curious zorder 2 at f11
    s1 "So, where do you come from? What's it like back home?"
    hide student1
    stop music
    "..."
    "Home?"
    play music sad
    "Where do I live?"
    "Where did I come from?"
    "Who am I, really?"
    "All I remember is waking up somewhere in the streets."
    "Something should've been there. Yet when I attempt to recall my origin, I see nothing."
    "I have my name, but does it mean anything when you can't remember?"
    "I cannot remember anything."
    "Nothing at all."

    show student1 curious zorder 2 at t11
    s1 "..."
    show student1 curious zorder 2 at f11
    s1 "Do you not want to talk about it? That's fine."
    show student1 understanding zorder 2 at t11
    "The sudden assurance jolted me from my thoughts, and I turned to that student, who had their hand on my shoulder."
    "Brushing away my worries, I flashed a smile towards them. Hopefully, that would uplift their spirits."
    stop music fadeout 1.0
    show student1 calm zorder 2 at f11
    s1 "I was a little worried, you know. At least everything's okay!"
    s1 "Let's start heading back to the--"
    play sound whoosh
    show student1 calm zorder 2 at hf11
    s1 "Woah!" with vpunch
    play sound paper
    show student1 calm zorder 2 at t11
    "A chilly breeze blew by, and with it, a couple of papers."
    "I picked one up. There were a bunch of questions written on them. This must be a test paper of sorts."
    show student1 excited zorder 2 at f11
    s1 "Hey, [player], I have an idea!"
    show student1 understanding zorder 2 at hf11
    s1 "How about we answer them and compare our scores?"
    show student1 understanding zorder 2 at t11
    mc "Would this not belong to somebody else, though? It would be careless to just leave it out here."
    show student1 calm zorder 2 at f11
    s1 "Well, they aren't labeled, and I certainly don't see anybody nearby. Nobody's gonna know, I swear!"
    show student1 calm zorder 2 at t11
    "I hope we don't get in trouble for this."
    show student1 calm at thide zorder 2
    hide student1

    call quiz_gfloor

label gfloor_cont:
    scene preschool with pixellate
    play music s1theme fadein (1.0)
    $ quick_menu = True

    if correct_count_gfloor >= 3:
        show student1 excited zorder 2 at f11
        s1 "You did great!"
        show student1 understanding zorder 2 at f11
        s1 "You'll do amazing in school, I just know it!"
    else:
        show student1 curious zorder 2 at f11
        s1 "You did good, but there's room for improvement!"
        show student1 calm zorder 2 at f11
        s1 "As long as you kindle the fires of passion, you'll be able to go higher!"
    
    show student1 calm zorder 2 at f11
    s1 "Alright, now that we're done, what do you wanna know?"
    show student1 explaining zorder 2 at f11
    s1 "Stuff about me, my life, or the silly stuff I get into at times?"
    show student1 explaining zorder 2 at t11
    mc "I'd like to learn more about this school's history."
    "I could practically feel the excitement radiating off my companion. It seemed they had an interesting story to share with me."
    show student1 excited zorder 2 at hf11
    s1 "Straight to the point, huh? Then buckle up!"
    show student1 excited zorder 2 at t11
    "After clearing their throat, they breathed in and began to share the school's history."
    show student1 explaining zorder 2 at f11
    s1 "JASMS serves as the basic education institution for the Philippine Women's University, and it was originally a part of it as its preschool department."
    show student1 explaining zorder 2 at hf11
    s1 "Doreen Gamboa was hired by the University President to help open the preschool department."
    show student1 understanding zorder 2 at f11
    s1 "She was of Irish descent and had been trained in psychology."
    show student1 explaining zorder 2 at f11
    s1 "She wanted to create a place where children could learn and grow happily, even if the parents were initially resistant to her teaching methods."
    show student1 calm zorder 2 at f11
    s1 "Even when the school was burnt down, she was able to persevere. And look where we are now, almost a century later."
    show student1 excited zorder 2 at f11
    s1 "This school is really a wonderful place, isn't it?"
    
    show student1 excited zorder 2 at t11
    "I agree. It's really nice to be in."
    "Even as an outsider, the positivity is infectious. I can sense the excitement and happiness in everyone here."
    "Maybe I could bring this philosophy back home."

    mc "That's impressive. I admire the dedication to her goal. That's not something you see every day."
    show student1 calm zorder 2 at f11
    s1 "It really is, isn't it? But we've done enough storytelling."
    show student1 excited zorder 2 at f11
    s1  "Now let's head to the second floor!"

label second_floor:
    stop music
    play music piano fadein (1.0)
    scene floor2a with wipeleft_scene

    show student1 excited zorder 2 at f11
    s1 "We're here!"
    show student1 explaining zorder 2 at f11
    s1 "This is the second of five floors, unless you include the rooftop! You really need to see the rooftop! We have a garden there!"
    show student1 explaining zorder 2 at t11
    mc "Sounds interesting. I'd love to see it."
    show student1 calm zorder 2 at f11
    s1 "Want to walk around for a bit before we move on?"
    s1 "Let's check out the hallway!"
    show student1 calm at thide
    hide student1
    stop music fadeout 1.5
    scene floor2b with wipeleft_scene
    "As we walked down the hallway, I had a thought. A silent, creeping thought."
    "Wasn't the guard too lenient on me?"
    "They mentioned I had no appointment with the principal or anything."
    "I didn't even have any useful identification documents on me."
    "Why was I allowed in so easily?"
    "And what was with the constant quizzes? If it's a custom, it's admittedly a peculiar one."
    "Well, it wouldn't do to focus too much on possibilities, so I pushed the thoughts out of my head."
    play music s2theme
    "Near the lockers, I saw another student flipping through their papers, looking worried."
    "They seemed to be preparing for something very important. So important that they looked close to freaking out when they almost dropped their pile of sheets."
    "The student I'm with seemed to recognize them and led me to where they were."
    show student1 calm zorder 2 at f11
    s1 "Hey! What are you up to today?"
    show student1 calm zorder 2 at t11
    "With the hushed noise of surprise, the other student turned to us, their eyes seemingly lighting up."
    show student1 calm zorder 2 at t22
    show student2 shy zorder 3 at f21
    s2 "Oh! Hello there. Who's your companion?"
    show student1 explaining zorder 2 at f22
    show student2 shy zorder 3 at t21
    s1 "This is [player]. I'm showing them around the school!"
    show student1 explaining zorder 2 at t22
    show student2 thankful zorder 3 at f21
    s2 "Hi, [player]. What's it like so far?"
    show student2 thankful zorder 3 at t21
    mc "I'd say it's pretty neat. Certainly haven't seen stuff like this before."
    show student2 thankful zorder 3 at f21
    s2 "That's nice."
    show student2 worried zorder 3 at t21
    "They shrunk back with a sigh, looking even more worried than before. There was something important plaguing their mind."
    show student2 shy zorder 3 at f21
    s2 "Now if you won't mind, I really, really, really need your help."
    show student1 excited zorder 2 at f22
    show student2 shy zorder 3 at t21
    s1 "Don't you worry! We're here to help!"
    show student1 calm zorder 2 at t22
    mc "It's alright. We'll help you as much as we can. Is there anything you need help with?"
    "The student sighed with relief upon hearing our words, and they took in another breath before they spoke."
    show student2 worried zorder 3 at hf21
    s2 "Could you help me sort out my notes? I need to prepare for an important test, and if I don't pass I'm doomed!"
    show student1 curious zorder 2 at hf22
    show student2 worried zorder 3 at t21
    s1 "Oh no! We cannot let this tragedy come to pass! Come, [player], we must help in any way we can!"
    hide student1
    hide student2

    call quiz_2floor

label twofloor_cont:
    play music s2theme fadein (1.0)
    scene floor2b with pixellate

    $ quick_menu = True

    if correct_count_2floor >= 3:
        show student2 thankful zorder 3 at f11
        s2 "Phew! Everything's crystal clear! I should be able to finish it quickly"
    else:
        show student2 worried zorder 3 at f11
        s2 "I might need a little more time to review, but I've got the important stuff down. At least I hope so."
    show student2 thankful zorder 3 at t11
    mc "Just make sure to breathe in and calm yourself, kid. It'll be over in no time."
    show student2 surprised zorder 3 at f11
    s2 "Y-you really think I can do it?"
    show student2 surprised zorder 3 at t11
    mc "I sure do."
    show student1 explaining zorder 2 at f22
    show student2 surprised zorder 3 at t21
    s1 "Yeah! You just have to believe!"
    show student1 explaining zorder 2 at t22
    show student2 thankful zorder 3 at t21
    "The student brightened up, and they smiled graciously at us."
    show student2 thankful zorder 3 at hf21
    s2 "Thank you so much, guys!"
    s2 "I'm going back to the classroom. See you later!"
    show student2 thankful zorder 3 at t21
    mc "Good luck!"
    show student1 understanding zorder 2 at f22
    s1 "You can do it!"
    show student2 at thide
    hide student2
    show student1 calm zorder 2 at t11
    "With newfound confidence, the student turned around and headed back inside their room."
    "Hopefully they'll be able to pass the test."
    show student1 explaining zorder 2 at f11
    s1 "Man, am I glad I don't have any quizzes coming up soon. Reviewing for tests is always quite stressful, even for me."
    show student1 explaining zorder 2 at t11
    mc "Admittedly, I've never paid that much attention to my studies. Doesn't help that I was pulled out earlier. At least my friends sort of help me catch up."
    show student1 curious zorder 2 at f11
    s1 "Woah, really? Now I'm curious. If you want to, you can give me all the juicy details once you've settled in."
    show student1 curious zorder 2 at t11
    mc "I sure will, but I'm also curious. How have you been doing in academics?"
    show student1 excited zorder 2 at hf11
    s1 "I'm doing great! I may not be at the top of the class, but I've been able to get through things so far."
    show student1 excited zorder 2 at t11
    mc "That's great to hear. I'm sure you can keep up until the end."
    show student1 understanding zorder 2 at hf11
    s1 "Thanks, [player]. Anyway, we're heading into the middle ground now!"
    show student1 calm zorder 2 at f11
    s1 "Let's go, [player]."
    show student1 calm at thide
    hide student1
    stop music fadeout 1.0
    "I left the area and followed the student, but the nagging feeling from earlier came back."
    "Something feels off about this."
    "But I can't figure out what."

label third_floor:
    play music piano fadein (1.0)
    scene library with wipeleft_scene
    show student1 calm zorder 2 at f11
    s1 "And this is where our library is! We can take a look inside once you've settled in."
    show student1 calm zorder 2 at t11
    mc "You have a library? How big is it?"
    show student1 curious zorder 2 at f11
    s1 "Frankly, it's not super big, but it contains a lot of books! Maybe we can read them together once you're acquianted with this place."
    show student1 calm zorder 2 at t11
    "This school wasn't as huge or intricate as the ones back home, but it still had ample space for people to learn and grow."
    "It wasn't overly extravagant or superficial. The students were simply allowed to explore the world at their own pace."
    "The classrooms were slowly filling up with students, and we could see them chatting with each other or organizing their belongings."
    "Some of the other students gave me glances as we passed by, but I paid them no mind. I couldn't afford any unnecessary distractions."
    "Up ahead, someone opened the door and stepped outside one of the rooms. They weren't in uniform and they looked older, so they were probably a teacher."
    scene floor3 with wipeleft_scene
    show student1 excited zorder 2 at f11
    s1 "Good morning, Teacher! I'm giving [player] a tour of the school!"
    stop music
    play music t1theme fadein 0.5
    show student1 excited zorder 2 at t22
    show teacher kind zorder 3 at f21
    show teacher explaining zorder 3 at f21
    t1 "Good morning to you both. If you have time, would you mind lending me a bit of assistance?"
    show teacher kind zorder 3 at f21
    t1 "I seem to have mixed in two different piles of tests together by accident, and I need help with sorting them out."
    show teacher kind zorder 3 at t21
    show student1 explaining zorder 2 at f22
    s1 "Leave it to us, Teacher!"
    scene faculty with wipeleft_scene
    show teacher kind zorder 2 at t21
    show student1 explaining zorder 2 at t22
    "With that, we headed into the teacher's room, eager to assist."
    hide teacher
    hide student1

    call quiz_3floor

label threefloor_cont:
    scene faculty with pixellate
    play music t1theme fadein (1.0)

    $ quick_menu = True

    if correct_count_3floor >= 3:
        show teacher understanding zorder 3 at f11
        t1 "Good work, [player]."
    else:
        show teacher kind zorder 3 at f11
        t1 "You have room for improvement, [player], but you're putting in your best effort."

    show teacher kind zorder 3 at f11
    t1 "Thank you both for your assistance. Is there anything you need?"
    show teacher kind zorder 3 at t11
    mc "For one, who was Jose Abad Santos? He seems important, considering the school was named after him."
    show teacher explaining zorder 3 at f11
    t1 "You're a curious one. I suppose I can entertain your request."
    show teacher explaining zorder 3 at t11
    "They motioned for us to sit down near the table. With that I learned about the school's history, I knew this was bound to be intriguing."
    show teacher kind zorder 3 at f11
    t1 "Jose 'SengSeng' Abad Santos was born on February 19, 1886, in San Fernando, Pampanga."
    show teacher explaining zorder 3 at f11
    t1 "As the seventh of ten children to Don Vicente and Doña Toribia. He was quiet, reserved, diligent, and scholarly."
    show teacher understanding zorder 3 at f11
    t1 "He was especially close to his younger brother. They enjoyed swimming in the clean Pampanga River and flying kites."
    show teacher kind zorder 3 at f11
    t1 "Unfortunately, not all good things come to last."
    t1 "During the Spanish rule, his father was jailed for supporting the Katipunan, and witnessing his ordeal fueled Jose's patriotism, influenced by his elder brother Pedro."
    show teacher explaining zorder 3 at f11
    t1 "Jose immersed himself in reading and acquiring knowledge, excelling academically and even teaching English at 16, believing in the duty to educate his fellow countrymen."
    show teacher understanding zorder 3 at f11
    t1 "He vowed to become the defender of the helpless and the powerless, and he achieved his aspiration through industry, diligence, and hard work."
    show teacher kind zorder 3 at f11
    t1 "If there's nothing else you'd like to know, I'll be returning to my classroom. Farewell."
    show teacher kind at thide zorder 3
    hide teacher

    stop music fadeout 1.0
    "With that, the teacher walked away. What an intriguing tale of patriotism."
    "Stewing in my thoughts, I failed to notice another guard approaching the two of us."
    play music g2theme fadein (1.0)
    show guard2 wary zorder 2 at f22
    show student1 calm zorder 3 at t21
    g2 "Good morning to you both. Have you observed anything unusual recently?"
    show guard2 wary zorder 2 at t22
    show student1 curious zorder 3 at f21
    s1 "What kind of strangeness?"
    show guard2 exp zorder 2 at f22
    show student1 curious zorder 3 at t21
    g2 "I would say the type of strangeness that isn't easily noticeable, but can potentially lead into something worse."
    show guard2 wary zorder 2 at hf22
    g2 "Strangess such as nonsensical ramblings, indecipherable writings, eerily vacant stares and obsessions over the most peculiar ideas."
    show guard2 wary zorder 2 at t22
    show student1 curious zorder 3 at f21
    s1 "Well I don't remember seeing anything like that, but I'll let you know if I do. What about you [player]?"
    show student1 curious zorder 3 at t21
    "..."
    show student1 curious zorder 3 at hf21
    s1 "[player]?"
    show student1 curious zorder 3 at t21
    mc "Oh, it's nothing. I was just looking through my memories."
    show guard2 wary at thide zorder 2
    show student1 curious at thide zorder 3
    hide guard2
    hide student1
    "And so, we bid farewell to the guard and headed up the stairs once more."
    "It must be a coincidence."
    "Surely, that's all that it was."
    "Right?"

label fourth_floor:
    scene floor4 with wipeleft_scene

    show student1 explaining zorder 2 at f11
    s1 "Whew! The tour is past the halfway point. I'm certain you'll fit in here really well, [player]!"
    show student1 explaining zorder 2 at t11
    mc "I hope so. You're truly kind. People like you are rarer than they should be."
    show student1 excited zorder 2 at hf11
    s1 "Aw, that's so sweet! Thanks, [player]!"
    show student1 calm zorder 2 at t11
    mc "You're welcome. I'm sure you'll be able to achieve great things in li--"
    stop music
    play music kairostheme fadein (1.0)
    hide student1
    show kairos calm zorder 2 at f11
    u "Hello."
    show kairos calm zorder 2 at t11
    "..."
    show kairos confident zorder 2 at f11
    u "You're getting used to this, aren't you?"
    show kairos eager zorder 2 at f11
    u "You don't need to worry about big things. You can just become a normal member of society."
    show kairos confident zorder 2 at f11
    u "You've already been able to blend in, after all."
    show kairos eager zorder 2 at f11
    u "This world is very different. It's all so familiar, yet so alien."
    show kairos confident zorder 2 at f11
    u "Don't you think so, too?"
    show student1 curious zorder 3 at f21
    show kairos calm zorder 2 at t22
    s1 "Hey, [player], are you okay? You were spacing out for a while."
    show student1 curious zorder 3 at t21
    mc "Y-yeah, I'll just head to the bathroom for a bit."

    scene cr4 with wipeleft_scene
    hide student1
    show kairos confident zorder 2 at f11
    u "You've figured it out, haven't you?"
    show kairos eager zorder 2 at f11
    u "Still as sharp as ever. Your wits have always been a thorn in my side."
    show kairos calm zorder 2 at f11
    u "But you'll never get anywhere by running away from your problems."
    show kairos manic zorder 2 at f11
    u "Wouldn't it be great if you could just stay here forever? It's clear that this place can be your home."
    u "Don't worry. You already like it here. You'll love it in no time."
    show kairos manic zorder 2 at t11
    mc "Why?"
    mc "Why are you doing this?"
    show kairos confident zorder 2 at f11
    u "You don't need to know yet."
    u "Just answer my questions."
    show kairos eager zorder 2 at f11
    u "Do you really believe you'll be able to go home?"
    hide kairos

    call quiz_4floor

label fourfloor_cont:
    scene cr4 with pixellate
    play music kairostheme fadein (1.0)

    $ quick_menu = True

    if correct_count_4floor >= 3:
        show kairos calm zorder 2 at t11
        u "..."
        show kairos calm zorder 2 at f11
        u "Hmm..."
        show kairos confident zorder 2 at f11
        u "I see you're getting the hang of this."
    else:
        show kairos calm zorder 2 at t11
        u "..."
        show kairos annoyed zorder 2 at f11
        u "Your skills are still lackluster at this point..."
        u "How embarrassing."

    show kairos confident zorder 2 at f11
    u "We'll be meeting soon. I hope you're prepared."
    show kairos eager zorder 2 at f11
    u "See you later."
    show kairos manic at thide
    hide kairos

    "..."
    "Why did it feel so personal?"
    "There are still gaps within my recollection, but I feel a sense of familiarity."
    "Anyhow, I've spent enough time moping around. Hopefully that student didn't wander off too far."
    stop music fadeout 0.5

    scene floor4 with wipeleft_scene
    mc "Hey, I'm back..."
    "..."
    "Huh?"
    "I glanced at the clock. It was 7:08. Perhaps they had been summoned back to their classroom?"
    "But there was still ample time before the start of class. Maybe there was something really urgent."
    "Shaking off my worries, I walked around the halls, calling out for a response."
    mc "Hey? Are you there?"
    play music sus fadein (1.0)
    scene gr11ar with wipeleft_scene
    "Amidst my whirling thoughts, I took a glance at the nearest classroom."
    "The tables were neatly arranged in rows of 5, and the bags were placed next to their respective chairs."
    "The shelves hosted various handmade projects of sorts, and the boards had written reminders of important deadlines and upcoming assignments."
    "By all accounts, it was a perfectly normal classroom."
    "..."
    "But it was empty."
    "Painfully empty."
    "..."
    "Trying to keep my cool, I went over to the room right next to it."
    "Surely, they had just gone somewhere else when I wasn't looking. I was just being paranoid."
    "That had to be it."
    "Steeling myself, I looked inside."
    scene gr12aq with wipeleft_scene
    "It was practically identical to the previous room."
    "I checked another room. Then another. And another."
    "It was the same result everytime."
    "There was nothing."
    scene black
    "Nothing."
    "Not even a speck of dust."
    "It was like everyone had vanished in the blink of an eye."
    scene floor4 with dissolve
    "Someone was pulling the strings. And I had to fix this situation as soon as possible."
    "Without hesitation, I scampered up the stairs to the fifth floor."
    "Surely, there must be someone else in here."
    "Right?"
    stop music fadeout 1.0
label fifth_floor:
    play music sus2 fadein (1.0)
    scene gym with wipeleft_scene
    "The first place I looked was the large court area. It was colored in shades of maroon, and there were line markings on the floor."
    "Within the field were multiple pieces of sport equipment, such as balls, rackets and nets. I wonder what kind of sports they play here."
    "But it was empty. Just like the rest of the rooms."
    "Taking one last look at the gymnasium, I turned around and walked down the halls."
    "I took a glance inside the laboratory. There were beakers and vials carefully arranged inside the cabinets, and various manuals were kept on the shelves."
    scene chemlab1 with wipeleft_scene
    "Bits of experimental residue were spread across the tables, a sign of recent activity."
    "But the rooms were empty."
    "The school was empty."
    scene floor5 with wipeleft_scene
    "I hope everyone is okay. I really do."
    "Even when I was a complete stranger, that student was kind and welcoming."
    "And it's just that student. Everyone I've met was so sincere. And now..."
    stop music fadeout 1.0
    play music kairostheme fadein 0.5

    show kairos calm zorder 2 at f11
    u "Hm?"
    show kairos confident zorder 2 at f11
    u "You're worried about them aren't you? How typical."
    show kairos eager zorder 2 at f11
    u "You still can't let go of your mindset even when you're stranded in an alien world."
    show kairos eager zorder 2 at t11
    mc "You..."
    mc "Just what did you do to them?"
    show kairos calm zorder 2 at f11
    u "I promise I didn't lay a finger on them. I just put time in a sort of temporary stasis."
    show kairos confident zorder 2 at f11
    u "I didn't even bother with something advanced. It's very easy to fix this, you know."
    show kairos eager zorder 2 at f11
    u "All you have to do is remember."
    hide kairos

    call quiz_5floor

label fivefloor_cont:
    play music kairostheme fadein (1.0)
    scene floor5 with pixellate

    $ quick_menu = True

    if correct_count_5floor >= 3:
        show kairos confident zorder 2 at f11
        u "You're doing rather well. But it begs the question..."
    else:
        show kairos annoyed zorder 2 at f11
        u "...you still need some work."
    
    show kairos confident zorder 2 at f11
    u "Have you even learned something?"
    show kairos confident zorder 2 at t11
    mc "I've learned a lot, actually."
    mc "I heard a tale of compassion, bravery and freedom, told by the honest and hardworking members of this pioneering institute."
    mc "I've gained so much knowledge, both familiar and unfamiliar, and I was able to experience the joys of companionship once more."
    mc "I have seen countless wonders on my journey, but there are still remarkable things I never thought existed."
    mc "Indeed, we are different in every way, yet kindness and passion can create bonds that last until the end of time."
    mc "And that is the true beauty of life."

    show kairos calm zorder 2 at t11
    u "..."
    show kairos annoyed zorder 2 at hf11
    u "...ha"
    show kairos manic zorder 2 at f11
    u "Still fixated on giving the most contrived speeches in desperate times. You'll never change."
    u "Even if you were to forge everlasting friendships, you'd leave them behind evetually."
    u "Do you know of the life you led before you came to this place?"
    u "Do you truly know of the wonders you say you've seen on your journey?"
    show kairos annoyed zorder 2 at f11
    u "Do you remember?"
    u "Do you remember??"
    show kairos eager zorder 2 at f11
    u "Can you even remember?"
    hide kairos
    scene black
    stop music
    "..."
    mc "I..."
    mc "I can't..."
    mc "I can't remember anything."
    mc "Why can't I remember?"
    mc "Why can't I remember anything?"
    u "Ha!"
    u "You didn't question until now, did you? You were so wrapped in the illusion of peace that you failed to realize the truth of the situation."
    u "You were babbling about your epic journey of self-realization, but you can't even remember why you started it!"
    u "You say your home is as wonderful as this place, but if you can't remember, do you even have one?"
    u "You've lost your skills. You've lost your strength."
    u "You've even lost your semblance of self!"
    u "I never thought I'd ever see you in such a state. Perhaps I should leave you like this. They'll never know what became of you."
    u "You'll be alone. Forgotten. You'll be lost to time."
    u "You have a name, but without your memories, that's all you have."
    u "Who are you?"
    mc "Who... am I?"
    mc "Who am I?"
    mc "Who am I? Who am I? Who am I?"
    mc "{cps=350}Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I? Who am I?{/cps}{nw}"
    with dissolve
    $ renpy.pause(1.0)
    play music sad fadein (1.0)
    "..."
    u2 "Hey, [player], you good? You blacked out in the middle of the fight and □□□□□ was so worried!"
    scene moon with open_eyes
    "I opened my eyes, and I saw the sky."
    "The moon illuminated the starry sky, and the trees shifted amidst the cool breeze."
    "I was on someone's lap. I couldn't remember their face. I couldn't remember who they were."
    "But I felt warm. Content. Happy."
    u4 "[player], do you see how the stars twinkle in the midnight sky?"
    u4 "Even in the darkest of nights, there will always be a light that shines the path to salvation."
    u4 "And it is our duty to be that light, for the sake of the world."
    scene black
    "I could see images flash through my head. I could see towns, caverns, castles, and dungeons. I could see people."
    scene moon with dissolve
    u3 "[player], y-you really want to tend to the flowers with me?"
    u3 "S-sorry, I didn't think you'd be interested in helping me. But I appreciate it. I really do."
    scene black
    "People I cared for. People I fought for. People I cherished."
    scene moon with dissolve
    u5 "Oi, [player]. You wanna go race with me down the road? Just you wait, I bet I'll get my winning streak back."
    scene black
    "I couldn't remember them. But they remembered me."

    u3 "[player], you've worked so hard for all of our sakes."
    u4 "[player], I know that we'll be able to do this together."
    u5 "[player], you may be stubborn as a mule, but I'll stick with you until the end."
    u2 "[player], let's get over there and show them who's boss, yeah?"

    "And still... there was one more."

    u6 "[player], I would be lying if I said I wasn't worried, but I know we can do it. We've been able to succeed many times before."
    u6 "This may be our toughest battle, but we can celebrate with everyone afterwards. Maybe we'll get our own statues in the capital to commemorate our achievements."
    u6 "When all of this is over, let's settle down in the countryside. It'll just br the two of us, looking over the city."
    u6 "When our adopted children yearn to explore the world, we can tell them a story."
    u6 "A story of hardship, friendship, and heroism."
    u6 "We can tell them our story."

    "..."
    scene floor5 with dissolve
    play music will1 fadein (1.0)
    mc "I..."
    mc "I remember."
    mc "I remember now."
    mc "I can't remember everything. But I can remember their voices. Their smiles. Their happiness."
    mc "I remember the times we've spent together, racing down the countryside or exploring the ancient ruins."
    mc "I can remember some of accomplishments, my achievements, which wouldn't have been possible without them."
    mc "I remember my home, my friends, my life."
    mc "I remember why I began my journey. And why I'll do anything to finish it."
    mc "I'll come back. I'll find a way. And nothing you say will stop me."
    show kairos confident zorder 2 at f11
    u "Oh?"
    show kairos eager zorder 2 at f11
    u "You remember now, don't you?"
    u "I was worried I broke you by accident. That wouldn't have been fun at all."
    u "You already know where to go. I'll see you there."
    u "Hopefully your skills haven't rusted too much."
    show kairos manic at thide
    hide kairos

    "With a newfound rush of determination, I raced up the stairs to the rooftop."
    "I can do this. I have to."
    "I just hope everything will be okay."

label rooftop:
    stop music
    play music solo fadein (1.0)
    scene fishtank with wipeleft_scene

    "Unlike the other floor, the sixth floor lacked any expansive hallways on wide corridors, but there was still ample room to move around in."
    "Ahead of me was a pathway that led to a pair rooms. Since this area was usually restricted, it would be not to snoop around."
    "To my right was a duty table, and on it was a rectangular glass container filled with water, plants and sand. There were a couple of fish swimming around, waiting for their next batch of food."
    "Good thing there was a food bottle nearby."
    "I picked the bottle up. There wasn't a lot of food left. Hopefully a smaller serving would be enough until fresh stock comes around."
    "But before I could feed the fish, a cloud of smoke permeated the room."
    "When the smoke cleared, I could see a person. Their mask stood out against the darkness of their coveralls, and numerous weapons and gadgets were hooked to their belt."
    "Whenever they appeared in my adventures, it usually meant their master was involved in some dastardly plan of theirs."
    "I couldn't let myself harbor any feelings. I couldn't let myself get riled up. Not since..."
    stop music fadeout 1.0
    play music mid fadein (0.5)
    show midnight back_turned zorder 2 at f11
    u7 "You have finally arrived."
    show midnight back_turned zorder 2 at t11
    mc "Yeah, yeah. You really haven't changed, Midnight."
    mc "Couldn't you have popped up somewhere less stuffy? It's quite cramped here for the fight, you know."
    show midnight prepared zorder 2 at f11
    md "You are lot more confident in yourself than before, [player]. I suppose you've been able to regain your memories."
    show midnight prepared zorder 2 at t11
    mc "Wait, you've been observing me since I got here?"
    show midnight anticipating zorder 2 at f11
    md "I have my ways. Your concerns matters not."
    show midnight prepared zorder 2 at f11
    md "My objective is to delay you with a flurry of queries, for my master has almost finished their preparations."
    show midnight prepared zorder 2 at t11
    mc "And my objective is to make sure their plans don't come to fruition."
    hide midnight

    call quiz_rooftop

label rooftop_cont:
    play music mid fadein (1.0)
    scene fishtank with pixellate

    if correct_count_roof >= 3:
        show midnight prepared zorder 2 at f11
        md "So you are indeed learning well..."
    else:
        show midnight back_turned zorder 2 at f11
        md "...hm"

    show midnight anticipating zorder 2 at f11
    md "Regardless of your expertise, I have successfully completed my task. They have already gotten all they need."
    mc "What have they obtained? What exactly are they trying to accomplish?"
    md "It would be best for you to make your way towards the garden."
    show midnight back_turned zorder 2 at f11
    md "They have been waiting for your arrival since your awakening."

    show midnight back_turned zorder 2 at t11
    "I had many questions swirling through my head. Questions about the truth of the situation."
    "Questions about these otherworldly circumstances. Questions about the fate of this world."
    "But there was one hanging by the tip of my tongue. I need to know."
    "I needed to know."
    "I had to know."

    mc "Wait."
    mc "I need to ask you something."
    show midnight prepared zorder 2 at f11
    md "Very well. You may ask a single question."
    show midnight prepared zorder 2 at t11
    mc "Everything that was built up, everything that was cherished..."
    mc "Was it all...a lie?"

    "..."
    show midnight back_turned zorder 2 at f11
    md "I have made my choice. Now, you must make yours."
    show midnight back_turned at thide
    hide midnight

    "With that, they disappeared in a puff of smoke, just like how they appeared in front of me."
    "I still had many unanswered questions. Many worrying thoughts. Many uncertain beliefs."
    "But I couldn't focus on them now. Not when I was so close to the end."
    "It was time for the final confrontation."

label bossbattle:
    stop music fadeout 1.0
    play music kairostheme fadein (1.5)
    scene rooftopa with wipeleft_scene

    "The garden area was probably the main highlight of the rooftop."
    "There were many small plants resting in the soil, and some of them were labeled in carefully arrange pots."
    "I could see the wispy clouds drifting across the pale blue sky, shielding the bright sun from my eyes."
    "A flock of birds flew acress in harmony with the wind, journeying to who knows where."
    "In the center of the area stood a person. Their back was turned to me, but I knew who it was as soon as I laid my eyes upon them."
    "As if on cue, they turned around. Their hood outlined their smug face, and their coat was as billowy as ever."
    "We had clased many times in the past, but these circumstances were still rather unique to me."

    show kairos confident zorder 2 at f11
    u "Congratulation for your timely arrival. I was starting to wonder if you got lost in a ditch somewhere."
    show kairos confident zorder 2 at t11
    mc "Well, unlike the schools back in our home, this one is rather easy to navigate, so that probably isn't the best insult you could've used."
    mc "Have you lost your sharp tongue, Kairos?"
    show kairos annoyed zorder 2 at f11
    k "You've gotten snarkier, haven't you?"
    show kairos manic zorder 2 at hf11
    k "I'm already starting to miss your empty self. You were just going along with the flow when you first got here."
    show kairos annoyed zorder 2 at t11
    mc "What can I say? With this surge of memories, I can finally reclaim my true identity. And now, I'll make sure to stop you before anything happens to this world."
    show kairos eager zorder 2 at hf11
    k "Ha!"
    k "I'm not planning to do anything, per se."
    show kairos confident zorder 2 at f11
    k "I've already gotten what I need. Perhaps I should just leave you here, stranded forever, in a world not meant for you."
    show kairos confident zorder 2 at t11
    mc "You already seem certain of the outcome. I wouldn't let my hopes skyrocket if I were you."
    mc "Besides, what do you even want from this world?"
    mc "There's no magic to be found, and half of this technology can't be replicated in our current age."
    stop music fadeout 1.0
    play music hype fadein (1.0)
    show kairos eager zorder 2 at t11
    "Kairos snapped back to attention upon hearing my question. With a confident smile, they locked their eyes onto mine."
    show kairos eager zorder 2 at f11
    k "You see, it's actually rather simple."
    k "I only wanted to test a theory."
    k "One I've had for a very long time."
    show kairos confident zorder 2 at f11
    k "I thought it was nothing more than a coincidence, but I realized I couldn't have been more wrong."
    show kairos confident zorder 2 at t11
    "..."
    "Just a theory?"
    "I've seen them do things no sane man would for their confirmation bias, but coming to another world for it? That's on another level."
    "Why was going to a different dimension important? They could've done their experiment in our home world, but why wouldn't they..."
    "Oh..."
    "Oh no..."
    "I desperately hoped that I was just being paranoid, that I was merely assuming the worst, but the satisfied smirk on their face said it all."
    mc "You wouldn't dare!" with vpunch
    show kairos manic zorder 2 at hf11
    k "I did."
    k "The results were not what I expecting, but it was still a fruitful experiment, don't you think?"
    show kairos manic zorder 2 at t11
    mc "I knew you were crazy, but this is a whole new low, even for you!"
    mc "Do you fully realize the implications?"
    show kairos confident zorder 2 at f11
    k "I must thank you for your honesty. I'm flattered."
    k "I never thought you had it in you."
    show kairos eager zorder 2 at f11
    k "But rest assured, I don't plan on altering this world in any significant way. This was all just a means to an end."
    show kairos eager zorder 2 at t11
    mc "Why, you--"
    "Before I could rush and knock the air out of them, I felt a mysterious force locking me in place."
    mc "You--what is this? Is this--"
    show kairos confident zorder 2 at f11
    k "Ha!"
    show kairos eager zorder 2 at f11
    k "I wish. I can't directly access it here, but I can simulate it to a certain degree. It's quite a convenient power, I must say."
    k "As much as I would prefer settling things the traditional way, that's not what this game is about, isn't it?"
    show kairos manic zorder 2 at f11
    k "You've gotten guite used to these unorthodox methods, so I'd like to test your expertise in person."
    show kairos manic zorder 2 at t11
    mc "So that's how you want to go about this, huh? You better not make this too easy."
    show kairos manic zorder 2 at f11
    k "We'll see about that, [player]."
    hide kairos

    call quiz_boss1

label boss1_cont:
    play music kairostheme fadein (1.0)
    scene rooftopa with pixellate

    if correct_count_boss1 >= 3:
        show kairos eager zorder 2 at f11
        k "Good, good. You haven't lost your touch!"
    else:
        show kairos annoyed zorder 2 at f11
        k "After all this time? Truly laugable."
    
    show kairos calm zorder 2 at t11
    mc "Is this the best you've got? I'm starting to think this wouldn't get as hype as you said it would."
    mc "You want to just get it over with and open a portal back home? Maybe that way it woudn't feel so easy."
    show kairos eager zorder 2 at f11
    k "Ha! It's far too easy to rile you up with that fake confidence of yours."
    k "Let's see how long it will last."
    show kairos manic zorder 2 at f11
    k "You lead your party with your bravery and charisma, but once that mask of your shatters, what do you think you'll be left with?"
    show kairos manic zorder 2 at t11
    mc "You're one to talk. You've been relentlessly pursuing your fruitless goals and preventing yourself from truly appreciating the beauty of life."
    mc "You've even dragged people from an entirely different world into this!"
    show kairos annoyed zorder 2 at f11
    k "Still trying to talk down to me, I see."
    show kairos annoyed zorder 2 at t11
    "As I racked my brain for a witty comeback, a crackle of thunder interrupted my train of thought."
    "I looked up, and I saw the sky begin to darken. The windes howled with a tempestuous fury, and the trickle of rain turned into a frigid downpour that dripped down an invisible forcefield."
    show kairos eager zorder 2 at f11
    k "Don't delude yourself, [player]."
    show kairos eager zorder 2 at t11
    "A faint smile was beginning to form, and their eyes glistened with a creepy glint."
    show kairos manic zorder 2 at hf11
    k "We're just getting started."

label final_phase:
    stop music fadeout 1.0
    play music finalhype fadein (1.0)
    scene rooftopb with wipeleft_scene

    "The two of us stood on opposing ends amidst the raging storm. The eerie emptiness in the school was filled with the fragments of a fierce calamity in the making."
    "The wind picked up with a freezing gust of air. I steeled myself and braced for the chilling sensation coming over me, yet my opponent still adorned a mocking leer."
    mc "You..."
    mc "What did you do?"
    show kairos confident zorder 2 at f11
    k "Weather manipulation really isn't as hard as people make it out to be. Once you've got the basics down, it becomes a breeze to control."
    show kairos confident zorder 2 at t11
    mc "You said you wouldn't lay a finger on this world!."
    show kairos manic zorder 2 at hf11
    k "Does it really count if it's only meager matters such as this? At least nobody else can get in the way of our duel!"
    show kairos manic zorder 2 at t11
    mc "What exactly did you do the people here? Did you whisk them away into a realm of nothingness?"
    show kairos manic zorder 2 at hf11
    k "This place is merely a figment within this plane of existence, where all the bystanders are in a state of slumber. I simply tampered a bit with reality."
    show kairos manic zorder 2 at t11
    mc "Jeez, how hard is it to simplify things? Is it because you want to sound more sensible? Or is it because you want to sound like a--"
    show kairos annoyed zorder 2 at f11
    k "How rude. I honestly thought we would finally get along for once. But it doesn't matter."
    show kairos annoyed zorder 2 at t11
    "As if on cue, a whirlpool of energy appeared in the sky, sucking up any particles it could find."
    "The storm only grew more intense, and the lightning strikes became much more frequent."
    "The howling wind rang in my ears, and the otherworldly sight above me was burned into my eyes."
    mc "What in the world are you doing?"
    "They met my eyes upon my query, and I almost wished I didn't ask. Their calm, yet eerie expression sent shivers down my spine, and their warm smile certainly matched the look."
    show kairos confident zorder 2 at f11
    k "I'm setting the atmosphere, of course. It may be overkill with the kind of duels we're having, but it's intimidating, don't you think?"
    "With a light chuckle, they began to pace around the garden, their footsteps clear. The swirling tempest roared above us, threatening to encompass the entire area."
    show kairos eager zorder 2 at f11
    k "The dam of energy is about to burst, and this discordant harmony only highlights this imminent surge of power."
    show kairos manic zorder 2 at f11
    k "The discoveries from this reckoning will surely revitalize how we view the possibilities of fate."
    show kairos calm zorder 2 at f11
    k "I was planning on holding back here, I truly was."
    show kairos annoyed zorder 2 at f11
    k "Unfortunately, I could not tolerate your antics any longer."
    show kairos eager zorder 2 at f11
    k "This theory had me racking my brain for any potential solutions, yet I could not have expected the resulting enigma in my wildest dreams."
    k "I thought I had already delved into the abyss, yet the way below runs deeper than I could've ever imagined."
    show kairos manic zorder 2 at f11
    k "And now, with you here, I can relish the day that my grandest delusions were proved to be the awakening of a new age."
    show kairos manic zorder 2 at t11
    "When those words left their mouth, Kairos stopped their pacing and looked me straight in the eye. I could feel their gaze burn into my very being as they took a step closer."
    show kairos eager zorder 2 at f11
    k "[player], this is the last show of this act. The grand finale of our current chapter."
    show kairos manic zorder 2 at hf11
    k "And your performance better not disappoint me."
    hide kairos

    call quiz_final_battle

label final_battle_cont:
    play music sus2 fadein (1.0)
    scene rooftopb with pixellate

    if correct_count_final_battle >= 3:
        show kairos eager zorder 2 at f11
        k "Well, well, well. We're so close to the end."
        k "Might as well put in your all. It wouldn make for a splendid send off to our audience."
    else:
        show kairos annoyed zorder 2 at f11
        k "Still failing short near the finish line?"
        k "I expected better of you. I pray the audience will not boot you off the stage."

    show kairos eager zorder 2 at t11
    mc "What audience? Who can even see us from here?"
    show kairos confident zorder 2 at f11
    k "[player], oh, [player]. You couldn't hope to understand."
    show kairos confident zorder 2 at t11
    mc "Then enlighten me. Is this all a play to you?"
    show kairos calm zorder 2 at f11
    k "This is all just a game to them. They merely observe what is happening before us, what is happening to us. And even the strongest being couldn't hope to touch them."
    show kairos calm zorder 2 at t11
    mc "...Is this your attempt at intimidating me?"
    show kairos confident zorder 2 at f11
    k "And what if it was?"
    show kairos confident zorder 2 at t11
    mc "Well, what else do you have up your sleeve? You can only do so much without your true strenght."
    show kairos eager zorder 2 at f11
    k "That's where you're wrong, [player]."
    show kairos eager zorder 2 at t11
    "Normally, I'd brush off one of their usual grins, but this one was different. They were always sure their pans would work, but this time..."
    "But this time, they sounded so certain, so confident that I had to suppress my emerging panic. This couldn't be good."
    "They slipped one hand inside their coat and reacher in for something. I had no idea what it could be, but I learned to trust my guy feeling in my many adventures."
    "After a couple of minutes, they pulled their hand out and held it towards me."
    stop music fadeout 1.0
    show kairos confident zorder 2 at f11
    k "I have this."
    play music sus fadein (1.0)
    show kairos confident zorder 2 at t11
    "..."
    "There's no way..."
    mc "H-how did you--"
    show kairos eager zorder 2 at f11
    k "You see, [player], while you were lounging around with that party of yours, I studied the ancient relics of forgetten civilizations!"
    show kairos calm zorder 2 at f11
    k "It took me months of gathering information from the lost text, but I was finally able to pinpoint its location!"
    show kairos eager zorder 2 at t11
    mc "It was shattered into a million pieces! How did you reform it?"
    show kairos confident zorder 2 at f11
    k "That's thanks to my second ace-in-the-hole! It was able to make a near perfect replica, and the only differences are nearly too small to even be seen!"
    show kairos confident zorder 2 at t11
    mc "You're lying...not even she could detect it..."
    show kairos eager zorder 2 at f11
    k "Hm? Really? That's rather surprising. I thought she would notice it, so I prepared a backup plan, but it seems she didn't. Well, it doesn't matter at this point."
    show kairos confident zorder 2 at f11
    k "[player], you fought well in all these years. But it's time to end this scuffle of ours."
    show kairos eager zorder 2 at t11
    "I desperately tried to break out of my invisible bindings, hoping to smack the relic out their hand, but it was no use."
    "Kairos only smiled as they activate their wild card, causing the maelstorm of electricity to surge. The winds only grew louder than before, and the breezes they carried became gales of fury."
    "The rain pounded on the barrier with a ferocity that could drown a world in sorrow."
    "I blinked rapidly, feeling my thoughts become foggy. I tried to reach out, to curse those above, but I felt my vision slipping away from my grasp."
    stop music
    hide kairos
    scene black

    "I heard a rattling noise from above us the ringing in my ears only intensified. The cacophony of noise threatened to burst my eardrums, and I had to hold on as best as I could."

    "I could  see their faces flashing in my mind. They were gone so fast I couldn't properly process each memory, but I felt a distinct sense of relief every time they popped up."

    "Was this how things would end?"
    "Stuck in an unfamiliar world, with no chance of being found?"

    "I..."

    "I was..."

    "Falling..."

    "..."
    
    "Wait."

    "I felt something... a gap in the barrier..."
    "There!"

    "I could sense a gap. It was so small, and it felt like it could disappear at any moment. But it was all I needed."
    "Thinking quickly, I broke out of it, and I could see particles fizzling out. Then I started running."
    "Running towards Kairos. Running so they'd turn their head and look."
    "I saw their eyes widen. Whether it was in shock or fear, I did not know."
    k "How did you--"
    "In their shock, they accidentally let go of the relic."
    "It dropped to the ground, shattering into a million pieces. The dormant power was finally free, and the resulting shockwave knocked both of us away."
    play sound bigboom
    scene black with dissolve
    $ renpy.pause(2.0, hard=True)
    scene white with dissolve
    play sound ouch
    "A blinding light burned into my eyes, forcing me to shield my eyes."
    "An ear-splitting roar resounded through the air, and the sensations creeping up my body threatened to overtake me."
    "The latent energy burst into the sky, and the brewing storm slowly fizzled out into nothingness."
    "The sky began to clear up, returning to its morning vibrancy while streaks of light faded into the distance."
    "I couldn't tell what was happening. I couldn't tell if everything would be okay."

    scene black

    "But I knew it was over."

label ending:
    scene rooftopa with dissolve
    
    "When I came to, I heard the plants sway in the gently breeze. Above me, a flock of birds flew in formation, journeying to their nesting area."
    "The sky was blue once more, and the sun was no longer hidden behind the silver clouds."
    "The relic's fragments lay across the ground, and it would be nearly impossible to put it back together."
    "Kairos was waiting for me to get back up"
    play music piano fadein (2.0)
    mc "Kairos?"
    show kairos calm zorder 2 at f11
    k "Well, well, well. You've done it again. Always a persistent thorn in my side. Staining a perfect canvas when it is so close to completion."
    show kairos calm zorder 2 at t11
    mc "What are you going to do now? Pull another artifact out of nowhere? Go on a rant how we'll never truly understand each other?"
    show kairos annoyed zorder 2 at f11
    k "Hmph. You really think so little of me."
    show kairos calm zorder 2 at f11
    k "Since I've already gotten what I need, I might as well wrap up this little adventure."
    show kairos confident zorder 2 at f11
    k "The loss is unfortunate, but I had thankfully prepared dozen replicas beforehand."
    show kairos confident zorder 2 at t11
    mc "Ha... still as meticulous as ever."
    show kairos calm zorder 2 at f11
    k "Although the conclusion wasn't what I had hoped, the performance was still a resounding success. This neat little game of ours was certainly worth it, don't you think?"
    show kairos calm zorder 2 at t11
    mc "It depends on your definition of worth, but I did enjoy my time here."
    show kairos confident zorder 2 at f11
    k "Would you want to stay here, then?"
    show kairos confident zorder 2 at t11
    play audio portal
    $ renpy.pause(1.5, hard=True)
    "I heard a noise. It sounded like a space was being torn into."
    "Behind Kairos was a portal back into our homeworld. It shimmered with a captivating glow, drawing my attention to the intricate patterns."
    show kairos eager zorder 2 at f11
    k "You mentioned enjoying your time here. Wouldn't it be nice to stay here?"
    show kairos confident zorder 2 at f11
    k "You don't have to worry about your party's funds or the latest monster sighting. You can just leave the big things to those in charge."
    show kairos calm zorder 2 at f11
    k "You can live a normal life for once."
    show kairos calm zorder 2 at t11
    "I had already gotten up, brushing the dust off my clothes. I couldn't let my reservations get to me."
    show kairos eager zorder 2 at f11
    k "Oh, are you scared? Are you scared of being normal? Has the life of an adventurer gotten to you?"
    show kairos eager zorder 2 at t11
    mc "You'll never know... you'll never know how they breathe, how they smile, how they live..."
    show kairos confident zorder 2 at f11
    k "Did you really like your experiences here that much? We'll, it's not too strange, coming from you. You often get attached to strangers you never see again."
    show kairos confident zorder 2 at t11
    mc "They're not strangers, they're people who have seen and appreciated more life than you ever will."
    show kairos calm zorder 2 at f11
    k "That's rather harsh, don't you think? I simply show my appreciation of life in a different way."
    show kairos confident zorder 2 at f11
    k "Why, it was only thanks to my dedication to unravelling the unknown that I even got this far."
    show kairos confident zorder 2 at t11
    mc "You say those are your achievements, but you've never really stepped back and enjoyed the small things in life."
    show kairos eager zorder 2 at f11
    k "It doesn't matter in the end, does it? We simply have vastly different perspectives. It is rather pointless to waste time on petty things."
    show kairos eager zorder 2 at t11
    mc "It doesn't really sound convincing coming from you."
    show kairos confident zorder 2 at f11
    k "I believe I have delayed myself enough."
    show kairos confident zorder 2 at t11
    "The portal simmered with the intensity of a star, and the vociferous rumbling made itself known."
    "Kairos, still as smug as always, took a couple steps toward it."
    show kairos calm zorder 2 at f11
    k "I supposed this is the curtain call of this game. We will return to our original world, and what happens next is up to fate. So what will be your choice, [player]?"
    show kairos calm zorder 2 at t11
    "My choice?"
    "Stay here or return home?"
    "If I stayed here, I could learn more about this world. Discover things that were never documented back home. Gain knowledge that is unfamiliar to me. Befriend the many good people this world has to offer."
    "But I have to duty to complete. A journey I must see through to the end."
    "And so, I started walking."
    mc "We still have unfinished business, Kairos. Do you really think I'll let you slip thought unnoticed?"
    show kairos confident zorder 2 at f11
    k "You've made your choice, but what about them? You were eagerly talking about the wonderful findings here much earlier, and now you're willing to leave them behind?"
    show kairos confident zorder 2 at t11
    mc "I'll carry the memories with me. I'll share the knowledge I've gained, the stories I've heard. Just like I always have."
    show kairos calm zorder 2 at f11
    k "If this is what you want, then so be it."
    show kairos calm zorder 2 at t11 
    "With those words, Kairos walked until they almost at the portal, glancing at me with smile."
    "The portal began to close faster than expected."
    "I picked up the pace. I couldn't risk it. I couldn't"
    "I could make it. I knew I could. I knew I could get back to them."
    "Kairos stepped into the portal, and prepared to take another. I braced myself and dashed forward, aiming to leap inside."
    show kairos eager zorder 2 at f11
    k "Ha. This was truly a fascinating experiment. I wonder when I'll get the next opportunity like this."
    show kairos confident zorder 2 at f11
    k "I'll see you there, [player]."
    show kairos confident at thide
    hide kairos
    stop music
    scene black
    play audio portal
    $ renpy.pause(1.0)

    "I should've known I wouldn't just be dropped back in with my party by my side."
    "Being stranded in the middle of nowhere without any companions or supplies will certainly be tough, but I'm sure I can make it."
    "It reminds me of the old times, before I had a party. It was just me and my family."
    "When I was young, my father told me that you must always savor each and every moment you spend with other people."
    "I asked him why, and he told me it's because you'll never know if it'll be the last time you see them."
    "Life is never predictable, and things can veer into a completely different direction without warning."
    "So it's important to cherish everything you have."
    "I never bid that one student farewell. I never told them about my life story. But they are a true and honest soul."
    "I'll also never know if that other student passed the test or not. But I'm certain they did."
    "I'll never see any of them again. And maybe it's for the better. We are from two completely different dimensions, and the gap between them is huge."
    "But we were able to light a spark."
    "We got to exchange information about each other. I got to learn the history behind one of many academic institutions. And even then, it was unique, unlike anything I had heard before."
    "I wonder what my companions are doing right now? Are they booking for me? Worrying about me? Or are they wandering aimlessly across the plains?"
    "I wonder what's going through Midnight's mind. Why they made the choice they did, perhaps I'll never know. But it's all in the past now."
    "I wonder what the true goal of Kairos is. We may never see eye-to-eye, but their dedication is admittedly remarkable."
    "However, I shouldn't dwell on this now. I should focus on getting back to my home."
    play music thememusic
    "When I reunite with my party, I can tell them a story as we sit by the campfire."
    "A story of kindness, compassion, and perseverance. A story of loyalty, bravery and patriotism. A story of hospitality, sincerity and humility."
    "My journey back home... well, that is a story for another time."
    "But I hope you enjoyed listening to this one."
    $ quick_menu = False

    $ secret_ending = correct_count + correct_count_gate + correct_count_gfloor + correct_count_2floor + correct_count_3floor + correct_count_4floor + correct_count_5floor + correct_count_roof + correct_count_boss1 + correct_count_final_battle

    call screen dialog ("""
    Your final score is
    [secret_ending] out of 50.
    """, Return(True))

    call screen dialog ("""
    Tutorial = [correct_count]
    Gate = [correct_count_gate]
    Ground Floor = [correct_count_gfloor]
    Second Floor = [correct_count_2floor]
    Third Floor = [correct_count_3floor]
    Fourth Floor = [correct_count_4floor]
    Fifth Floor = [correct_count_5floor]
    Rooftop = [correct_count_roof]
    Boss Battle = [correct_count_boss1]
    Final Phase = [correct_count_final_battle]
    """, Return(True))    

    if secret_ending >= 45:
        stop music fadeout 1.0
        scene black with dissolve
        play music t1theme fadein (1.0)
        $ renpy.pause(1.0)

        show teacher kind zorder 2 at f11
        t1 "Now that's everyone is gone and enjoyed a good ending."
        t1 "And before you ask, yes this is a Secret Ending that I prepared."
        t1 "It's time for me to introduced myself."
        show teacher explaining zorder 2 at f11
        sk "My name is Teacher Mel, the ICT Teacher for SY 2023-2024."
        sk "If you are reading this you either probably either cheated or really smart to know all the answers that Leto has prepared for you."
        show teacher understanding zorder 2 at f11
        sk "Still I am amazed."
        show teacher kind zorder 2 at f11
        sk "I hope that you learned a lot from this game, not just because of the story but all the lessons as well the code for this game."
        sk "It's not the most complex game in the world, but it's something I made out of love."
        show teacher understanding zorder 2 at hf11
        sk "And hey, I just started this game around a week ago and I was able to finish it under 1 week."
        sk "Imagine the things that you can do if you put your mind to it."
        show teacher kind zorder 2 at f11
        sk "To the future ICT Student or even Coding students that are passionate about game development."
        show teacher explaining zorder 2 at f11
        sk "Please, create a sequel or even a game that is better than this."
        show teacher kind zorder 2 at f11
        sk "That is your goal. To be better than me."
        sk "To be better than the previous generation."
        sk "To improve and innovate."
        sk "It's easy to forget sleep when you are working on something cool."
        sk "So you'll work as hard as you can but still there isn't enough time."
        sk "So essentially, you have to let go."
        show teacher explaining zorder 2 at f11
        sk "That's a quote from my mentor and it's deeper than you think."
        sk "And it's not what you think, and as I said before, it's deeper than you think."
        show teacher kind zorder 2 at f11
        sk "I think I should stop rambling now and let you enjoy the rest of the credits."
        sk "I hope we all see each other again."
        sk "Thank you so much for playing our game."
        sk "Thank you so much for the opportunity."
        sk "Thank you so much JASMS for the opportunity."
        sk "My code will be available on the game's page."
        sk "It's your turn now to make something great."
        sk "Good luck and Godspeed."
        show teacher understanding zorder 2 at hf11
        sk "Goodbye."
        hide teacher
        stop music fadeout 1.0
        scene black with dissolve
        jump credits

    else:
        with dissolve
        jump credits
