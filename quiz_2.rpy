label quiz_gate:
    with pixellate
    stop music fadeout 1.0
    play music battle fadein (1.0)
    $ questions_count_gate = 0
    $ available_questions_gate = questions_easy[:]

    while questions_count_gate < 5 :
        $ renpy.random.shuffle(available_questions_gate)
        $ q = available_questions_gate.pop()
        call quiz_questions_gate
        $ questions_count_gate += 1

    
    call reveal_results_gate

label quiz_questions_gate:
    $ quick_menu = False
    menu:
        "Question: [q[0]]"
        "[q[1]]":
            $ selected_answer_gate = q[1]
            jump quiz_answer_gate
        "[q[2]]":
            $ selected_answer_gate = q[2]
            jump quiz_answer_gate
        "[q[3]]":
            $ selected_answer_gate = q[3]
            jump quiz_answer_gate
        "[q[4]]":
            $ selected_answer_gate = q[4]
            jump quiz_answer_gate

label quiz_answer_gate:
    $ g1_response = ""
    if selected_answer_gate == q[5]:
        $ g1_response = renpy.random.choice(positive_feedback)
        g1 "[g1_response]"
        $ correct_count_gate += 1
        return
    else:
        $ g1_response = renpy.random.choice(negative_feedback)
        g1 "[g1_response]"
        return

label reveal_results_gate:
    #"You got [correct_count] out of 5 questions correct!"
    stop music fadeout 1.0
    jump gate_cont
