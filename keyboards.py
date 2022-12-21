from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

class AnswerKeyboard:

    def __init__(self, count):
        self.count = count

        ikb = InlineKeyboardMarkup(row_width=5)
        a = iter(range(1,count+1))
        for i in range(count//5+1):
            butts = []
            for k in a:
                current = str(k)
                butts.append(InlineKeyboardButton(text=current, callback_data=current))
                if k % 5 == 0:
                    break
            ikb.row(*butts)

        self.markup = ikb
