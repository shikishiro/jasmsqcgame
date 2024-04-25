label quiz_rooftop:
    with pixellate
    stop music fadeout 1.0
    play music battle fadein (1.0)
    $ questions_count_roof = 0
    $ available_questions_roof = questions_difficult[:]

    while questions_count_roof < 5 :
        $ renpy.random.shuffle(available_questions_roof)
        $ q = available_questions_roof.pop()
        call quiz_questions_roof
        $ questions_count_roof += 1

    
    call reveal_results_roof

label quiz_questions_roof:
    $ quick_menu = False
    menu:
        "Question: [q[0]]"
        "[q[1]]":
            $ selected_answer_roof = q[1]
            jump quiz_answer_roof
        "[q[2]]":
            $ selected_answer_roof = q[2]
            jump quiz_answer_roof
        "[q[3]]":
            $ selected_answer_roof = q[3]
            jump quiz_answer_roof
        "[q[4]]":
            $ selected_answer_roof = q[4]
            jump quiz_answer_roof

label quiz_answer_roof:
    $ md_response = ""
    if selected_answer_roof == q[5]:
        $ md_response = renpy.random.choice(positive_feedback)
        md "[md_response]"
        $ correct_count_roof += 1
        return
    else:
        $ md_response = renpy.random.choice(negative_feedback)
        md "[md_response]"
        return

label reveal_results_roof:
    #"You got [correct_count] out of 5 questions correct!"
    stop music fadeout 1.0
    jump rooftop_cont