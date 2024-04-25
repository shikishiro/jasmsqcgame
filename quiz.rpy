init python:
    renpy_menu = menu

    def menu(items):
        items = list(items)
        renpy.random.shuffle(items)
        return renpy_menu(items)

label quiz_tutorial:
    with pixellate
    stop music fadeout 1.0
    play music battle fadein (1.0)
    $ questions_count = 0
    $ available_questions = tutorial_questions[:]

    while questions_count < 5 :
        $ renpy.random.shuffle(available_questions)
        $ q = available_questions.pop()
        call quiz_questions_tutorial
        $ questions_count += 1

    
    call reveal_results

label quiz_questions_tutorial:
    $ quick_menu = False
    menu:
        "Question: [q[0]]"
        "[q[1]]":
            $ selected_answer = q[1]
            jump quiz_answer
        "[q[2]]":
            $ selected_answer = q[2]
            jump quiz_answer
        "[q[3]]":
            $ selected_answer = q[3]
            jump quiz_answer
        "[q[4]]":
            $ selected_answer = q[4]
            jump quiz_answer

label quiz_answer:
    $ tutorial_response = ""
    if selected_answer == q[5]:
        $ tutorial_response = renpy.random.choice(positive_feedback)
        u "[tutorial_response]"
        $ correct_count += 1
        return
    else:
        $ tutorial_response = renpy.random.choice(negative_feedback)
        u "[tutorial_response]"
        return

label reveal_results:
    #"You got [correct_count] out of 5 questions correct!"
    stop music fadeout 1.0
    jump tutorial_cont
