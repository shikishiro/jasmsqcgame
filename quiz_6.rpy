label quiz_4floor:
    with pixellate
    stop music fadeout 1.0
    play music battle fadein (1.0)
    $ questions_count_4floor = 0
    $ available_questions_4floor = questions_hard2[:]

    while questions_count_4floor < 5 :
        $ renpy.random.shuffle(available_questions_4floor)
        $ q = available_questions_4floor.pop()
        call quiz_questions_4floor
        $ questions_count_4floor += 1

    
    call reveal_results_4floor

label quiz_questions_4floor:
    $ quick_menu = False
    menu:
        "Question: [q[0]]"
        "[q[1]]":
            $ selected_answer_4floor = q[1]
            jump quiz_answer_4floor
        "[q[2]]":
            $ selected_answer_4floor = q[2]
            jump quiz_answer_4floor
        "[q[3]]":
            $ selected_answer_4floor = q[3]
            jump quiz_answer_4floor
        "[q[4]]":
            $ selected_answer_4floor = q[4]
            jump quiz_answer_4floor

label quiz_answer_4floor:
    $ u2_response = ""
    if selected_answer_4floor == q[5]:
        $ u2_response = renpy.random.choice(positive_feedback)
        u "[u2_response]"
        $ correct_count_4floor += 1
        return
    else:
        $ u2_response = renpy.random.choice(negative_feedback)
        u "[u2_response]"
        return

label reveal_results_4floor:
    #"You got [correct_count] out of 5 questions correct!"
    stop music fadeout 1.0
    jump fourfloor_cont