label quiz_2floor:
    with pixellate
    stop music fadeout 1.0
    play music battle fadein (1.0)
    $ questions_count_2floor = 0
    $ available_questions_2floor = questions_normal2[:]

    while questions_count_2floor < 5 :
        $ renpy.random.shuffle(available_questions_2floor)
        $ q = available_questions_2floor.pop()
        call quiz_questions_2floor
        $ questions_count_2floor += 1

    
    call reveal_results_2floor

label quiz_questions_2floor:
    $ quick_menu = False
    menu:
        "Question: [q[0]]"
        "[q[1]]":
            $ selected_answer_2floor = q[1]
            jump quiz_answer_2floor
        "[q[2]]":
            $ selected_answer_2floor = q[2]
            jump quiz_answer_2floor
        "[q[3]]":
            $ selected_answer_2floor = q[3]
            jump quiz_answer_2floor
        "[q[4]]":
            $ selected_answer_2floor = q[4]
            jump quiz_answer_2floor

label quiz_answer_2floor:
    $ s2_response = ""
    if selected_answer_2floor == q[5]:
        $ s2_response = renpy.random.choice(positive_feedback)
        s2 "[s2_response]"
        $ correct_count_2floor += 1
        return
    else:
        $ s2_response = renpy.random.choice(negative_feedback)
        s2 "[s2_response]"
        return

label reveal_results_2floor:
    #"You got [correct_count] out of 5 questions correct!"
    stop music fadeout 1.0
    jump twofloor_cont