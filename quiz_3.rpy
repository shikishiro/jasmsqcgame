label quiz_gfloor:
    with pixellate
    stop music fadeout 1.0
    play music battle fadein (1.0)
    $ questions_count_gfloor = 0
    $ available_questions_gfloor = questions_normal[:]

    while questions_count_gfloor < 5 :
        $ renpy.random.shuffle(available_questions_gfloor)
        $ q = available_questions_gfloor.pop()
        call quiz_questions_gfloor
        $ questions_count_gfloor += 1

    
    call reveal_results_gfloor

label quiz_questions_gfloor:
    $ quick_menu = False
    menu:
        "Question: [q[0]]"
        "[q[1]]":
            $ selected_answer_gfloor = q[1]
            jump quiz_answer_gfloor
        "[q[2]]":
            $ selected_answer_gfloor = q[2]
            jump quiz_answer_gfloor
        "[q[3]]":
            $ selected_answer_gfloor = q[3]
            jump quiz_answer_gfloor
        "[q[4]]":
            $ selected_answer_gfloor = q[4]
            jump quiz_answer_gfloor

label quiz_answer_gfloor:
    $ s1_response = ""
    if selected_answer_gfloor == q[5]:
        $ s1_response = renpy.random.choice(positive_feedback)
        s1 "[s1_response]"
        $ correct_count_gfloor += 1
        return
    else:
        $ s1_response = renpy.random.choice(negative_feedback)
        s1 "[s1_response]"
        return

label reveal_results_gfloor:
    #"You got [correct_count] out of 5 questions correct!"
    stop music fadeout 1.0
    jump gfloor_cont