from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import config

class AnswerInlineKeyboard(InlineKeyboardMarkup):

    def __init__(self, row_width, count):
        self.count = count
        super().__init__(self, row_width)

    def make_buttons(self):
        a = iter(range(1,self.count+1))
        for i in range(self.count//5+1):
            butts = []
            for k in a:
                current = str(k)
                butts.append(InlineKeyboardButton(text=current, callback_data=current))
                if k % 5 == 0:
                    break
            self.row(*butts)



class SubjectsReplyKeyboard(ReplyKeyboardMarkup):
    
    def __init__(self, subjects, resize_keyboard=None, one_time_keyboard=None):
        self.subjects = subjects
        super().__init__(resize_keyboard=resize_keyboard, one_time_keyboard=one_time_keyboard)

    def make_buttons(self):

        buttons = [KeyboardButton(text=subject) for subject in self.subjects]
        while len(buttons) >= 3:
            self.row(*buttons[0:3:])
            buttons = buttons[3::]
        if len(buttons) != 0:
            self.row(*buttons)
