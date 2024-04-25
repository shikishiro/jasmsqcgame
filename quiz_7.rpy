label quiz_5floor:
    with pixellate
    stop music fadeout 1.0
    play music battle fadein (1.0)
    $ questions_count_5floor = 0
    $ available_questions_5floor = questions_hard3[:]

    while questions_count_5floor < 5 :
        $ renpy.random.shuffle(available_questions_5floor)
        $ q = available_questions_5floor.pop()
        call quiz_questions_5floor
        $ questions_count_5floor += 1

    
    call reveal_results_5floor

label quiz_questions_5floor:
    $ quick_menu = False
    menu:
        "Question: [q[0]]"
        "[q[1]]":
            $ selected_answer_5floor = q[1]
            jump quiz_answer_5floor
        "[q[2]]":
            $ selected_answer_5floor = q[2]
            jump quiz_answer_5floor
        "[q[3]]":
            $ selected_answer_5floor = q[3]
            jump quiz_answer_5floor
        "[q[4]]":
            $ selected_answer_5floor = q[4]
            jump quiz_answer_5floor

label quiz_answer_5floor:
    $ u3_response = ""
    if selected_answer_5floor == q[5]:
        $ u3_response = renpy.random.choice(positive_feedback)
        u "[u3_response]"
        $ correct_count_5floor += 1
        return
    else:
        $ u3_response = renpy.random.choice(negative_feedback)
        u "[u3_response]"
        return

label reveal_results_5floor:
    #"You got [correct_count] out of 5 questions correct!"
    stop music fadeout 1.0
    jump fivefloor_cont