from telegram.ext.updater import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

updater = Updater('5192566556:AAGkSw2h6tK7YXn4DsKA1R5qtSAh6CpVB7k', use_context=True)

Answers=[]
class questioncounter:
      i=0
##Hello
############################### Bot ############################################
print("Bot Started...")
def start(update, context):
  update.message.reply_text(main_welcome(),reply_markup=main_menu_keyboard())
  
def main_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=main_welcome(),reply_markup=main_menu_keyboard())

def first_menu(update,context):
  Answers.clear()
  questioncounter.i=0
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=first_question(),reply_markup=first_menu_keyboard())

def about(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=abouttext(),reply_markup=back())

def nvm(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=nvmtext(),reply_markup=Nothing())
############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Start the chat🏁', callback_data='start')],
              [InlineKeyboardButton('About the bot🤷', callback_data='about')],
              [InlineKeyboardButton('Nevermind❌', callback_data='Nevermind')]]
  return InlineKeyboardMarkup(keyboard)

def back():
  keyboard = [[InlineKeyboardButton('Back ⬅️', callback_data='Main')],]
  return InlineKeyboardMarkup(keyboard)

def Nothing():
  keyboard = [[InlineKeyboardButton('✌🏼', callback_data='Main')],]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Sciences', callback_data='Science')],
              [InlineKeyboardButton('Mathematics', callback_data='Math')],
              [InlineKeyboardButton('mathematical technique', callback_data='Math Tech')],
              [InlineKeyboardButton('Literature and Philosophy', callback_data='Literature and Philosophy')],
              [InlineKeyboardButton('Foreign languages', callback_data='Foreign languages')],
              [InlineKeyboardButton('Management and Economy', callback_data='Management and Economy')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('10-11', callback_data='10-11')],
              [InlineKeyboardButton('11-12', callback_data='11-12')],
              [InlineKeyboardButton('12-13', callback_data='12-13')],
              [InlineKeyboardButton('13-14', callback_data='13-14')],
              [InlineKeyboardButton('14-15', callback_data='14-15')],
              [InlineKeyboardButton('15-16', callback_data='15-16')],
              [InlineKeyboardButton('16-17', callback_data='16-17')],
              [InlineKeyboardButton('17-18', callback_data='17-18')],
              [InlineKeyboardButton('18-19', callback_data='18-19')],
              [InlineKeyboardButton('19+', callback_data='19+')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def third_menu_keyboard():
  keyboard = [
    [InlineKeyboardButton('Less than 10', callback_data='G<10')],
    [InlineKeyboardButton('Between 10 and 14', callback_data='10<G<14')],
    [InlineKeyboardButton('14 or more', callback_data='G>14')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def forth_menu_keyboard():
  keyboard = [
    [InlineKeyboardButton('Less than 10', callback_data='G<10')],
    [InlineKeyboardButton('Between 10 and 14', callback_data='10<G<14')],
    [InlineKeyboardButton('14 or more', callback_data='G>14')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def fifth_menu_keyboard():
  keyboard = [
    [InlineKeyboardButton('Less than 10', callback_data='G<10')],
    [InlineKeyboardButton('Between 10 and 12', callback_data='10<G<12')],
    [InlineKeyboardButton('12 or more', callback_data='G>12')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)
############################Specialities########################################

def save(update,context):
  print(questioncounter.i)
  query = update.callback_query
  context.bot.sendMessage(chat_id=query.message.chat_id,text="🤖:Your answer was {}.".format(query.data))
  Answers.append(str(query.data))
  questioncounter.i+=1
  print(Answers)
  redirect(query,questioncounter.i)

################################### Menu's######################################
def redirect(query,i):
  if(i==0):
    query.edit_message_text(text=first_question(),reply_markup=first_menu_keyboard())
  if(i==1):
    query.edit_message_text(text=second_question(),reply_markup=second_menu_keyboard())
  if(i==2):
    query.edit_message_text(text=third_question(),reply_markup=third_menu_keyboard())
  if(i==3):
    query.edit_message_text(text=forth_question(),reply_markup=forth_menu_keyboard())
  if(i==4):
    if(Answers[0] != "Literature and Philosophy" and Answers[0] != "Foreign languages"):
      query.edit_message_text(text=fifth_question(),reply_markup=fifth_menu_keyboard())
    else:
      questioncounter.i+=1
      redirect(query,questioncounter.i)
  if(i==5):
    print("coming soon!...")

############################# Messages #########################################
def main_welcome():
  return 'Hi how can i help you?'

def abouttext():
  return "I'm a Bot created by three Computer Science students. My job is to help you decide your future, i will give you a choice that might fits you but always remember 'Choose what you like not what others like'"

def nvmtext():
  return 'Alright you can reach me anytime using " /start " have a great day 😄 '

def first_question():
  return 'What is your major in baccalaureate?'

def second_question():
  return 'What was your score in BAC?'

def third_question():
  return 'What is your grade average in English?'

def forth_question():
  return 'What is your grade average in French?'

def fifth_question():
  return 'What is your grade average in Math?'
############################# Handlers #########################################
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('about', about))

updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='start'))
updater.dispatcher.add_handler(CallbackQueryHandler(about, pattern='about'))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='Main'))
updater.dispatcher.add_handler(CallbackQueryHandler(nvm, pattern='Nevermind'))

updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Science'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Math'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Math Tech'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Literature and Philosophy'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Foreign languages'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Management and Economy'))

updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='10-11'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='11-12'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='12-13'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='13-14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='14-15'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='15-16'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='16-17'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='17-18'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='18-19'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='19+'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='G<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<G<14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='G>14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<G<12'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='G>12'))


updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='good'))
updater.start_polling()