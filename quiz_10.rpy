label quiz_final_battle:
    with pixellate
    stop music fadeout 1.0
    play music battle fadein (1.0)
    $ questions_count_final_battle = 0
    $ available_questions_final_battle = questions_final_battle[:]

    while questions_count_final_battle < 5 :
        $ renpy.random.shuffle(available_questions_final_battle)
        $ q = available_questions_final_battle.pop()
        call quiz_questions_final_battle
        $ questions_count_final_battle += 1

    
    call reveal_results_final_battle

label quiz_questions_final_battle:
    $ quick_menu = False
    menu:
        "Question: [q[0]]"
        "[q[1]]":
            $ selected_answer_final_battle = q[1]
            jump quiz_answer_final_battle
        "[q[2]]":
            $ selected_answer_final_battle = q[2]
            jump quiz_answer_final_battle
        "[q[3]]":
            $ selected_answer_final_battle = q[3]
            jump quiz_answer_final_battle
        "[q[4]]":
            $ selected_answer_final_battle = q[4]
            jump quiz_answer_final_battle

label quiz_answer_final_battle:
    $ k_response = ""
    if selected_answer_final_battle == q[5]:
        $ k_response = renpy.random.choice(positive_feedback)
        k "[k_response]"
        $ correct_count_final_battle += 1
        return
    else:
        $ k_response = renpy.random.choice(negative_feedback)
        k "[k_response]"
        return

label reveal_results_final_battle:
    #"You got [correct_count] out of 5 questions correct!"
    stop music fadeout 1.0
    jump final_battle_cont