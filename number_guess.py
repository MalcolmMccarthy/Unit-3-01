#created by malcolm mccarthy
#for ics3u
#in oct 2017
#if satement practice

import ui

CORRECT_NUMBER = 5

def check_answer_button_touch_up_inside(sender):
    #checks if constant = the number entered
    
    #input
    number_entered = int(view['number_textfield'].text)
    
    #process
    if number_entered < CORRECT_NUMBER :
    	view['answer_label'].text = "WRONG!"

view = ui.load_view()
view.present('sheet')
