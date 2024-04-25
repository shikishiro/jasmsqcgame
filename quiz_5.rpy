label quiz_3floor:
    with pixellate
    stop music fadeout 1.0
    play music battle fadein (1.0)
    $ questions_count_3floor = 0
    $ available_questions_3floor = questions_hard[:]

    while questions_count_3floor < 5 :
        $ renpy.random.shuffle(available_questions_3floor)
        $ q = available_questions_3floor.pop()
        call quiz_questions_3floor
        $ questions_count_3floor += 1

    
    call reveal_results_3floor

label quiz_questions_3floor:
    $ quick_menu = False
    menu:
        "Question: [q[0]]"
        "[q[1]]":
            $ selected_answer_3floor = q[1]
            jump quiz_answer_3floor
        "[q[2]]":
            $ selected_answer_3floor = q[2]
            jump quiz_answer_3floor
        "[q[3]]":
            $ selected_answer_3floor = q[3]
            jump quiz_answer_3floor
        "[q[4]]":
            $ selected_answer_3floor = q[4]
            jump quiz_answer_3floor

label quiz_answer_3floor:
    $ t1_response = ""
    if selected_answer_3floor == q[5]:
        $ t1_response = renpy.random.choice(positive_feedback)
        t1 "[t1_response]"
        $ correct_count_3floor += 1
        return
    else:
        $ t1_response = renpy.random.choice(negative_feedback)
        t1 "[t1_response]"
        return

label reveal_results_3floor:
    #"You got [correct_count] out of 5 questions correct!"
    stop music fadeout 1.0
    jump threefloor_cont