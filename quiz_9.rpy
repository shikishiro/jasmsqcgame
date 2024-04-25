label quiz_boss1:
    with pixellate
    stop music fadeout 1.0
    play music battle fadein (1.0)
    $ questions_count_boss1 = 0
    $ available_questions_boss1 = questions_boss1[:]

    while questions_count_boss1 < 5 :
        $ renpy.random.shuffle(available_questions_boss1)
        $ q = available_questions_boss1.pop()
        call quiz_questions_boss1
        $ questions_count_boss1 += 1

    
    call reveal_results_boss1

label quiz_questions_boss1:
    $ quick_menu = False
    menu:
        "Question: [q[0]]"
        "[q[1]]":
            $ selected_answer_boss1 = q[1]
            jump quiz_answer_boss1
        "[q[2]]":
            $ selected_answer_boss1 = q[2]
            jump quiz_answer_boss1
        "[q[3]]":
            $ selected_answer_boss1 = q[3]
            jump quiz_answer_boss1
        "[q[4]]":
            $ selected_answer_boss1 = q[4]
            jump quiz_answer_boss1

label quiz_answer_boss1:
    $ k_response = ""
    if selected_answer_boss1 == q[5]:
        $ k_response = renpy.random.choice(positive_feedback)
        k "[k_response]"
        $ correct_count_boss1 += 1
        return
    else:
        $ k_response = renpy.random.choice(negative_feedback)
        k "[k_response]"
        return

label reveal_results_boss1:
    #"You got [correct_count] out of 5 questions correct!"
    stop music fadeout 1.0
    jump boss1_cont