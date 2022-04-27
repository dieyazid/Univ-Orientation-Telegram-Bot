from telegram.ext.updater import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, User
import pickle

from expert import getdata

updater = Updater('5192566556:AAGkSw2h6tK7YXn4DsKA1R5qtSAh6CpVB7k', use_context=True)

Answers=[]
Users=[]
class counter():
      user=0
token=[]
qcounter=[]
############################### Bot ############################################
print("Bot Started...")
def start(update, context):
  chat_id=update.message.chat_id
  if chat_id not in Users:
    Users.append(chat_id)
    token.append([])
    token[counter.user].append(chat_id)
    token[counter.user].append(counter.user)
    counter.user+=1
    Answers.append([])
    qcounter.append(0)
  else:
      Clear(chat_id)
  print(token)
  update.message.reply_text(main_welcome(),reply_markup=main_menu_keyboard())
  
def main_menu(update,context):
  query = update.callback_query
  chat_id=query.message.chat_id
  Clear(chat_id)
  query.answer()
  query.edit_message_text(text=main_welcome(),reply_markup=main_menu_keyboard())

def Clear(chatid):
  for e in range (0,len(token)):
    if chatid==token[e][0]:
      case = token[e][1]
      Answers[case].clear()
      qcounter[case]=0
  with open('objs.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump([token], f)
  
def first_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=score_question(),reply_markup=score_keyboard())

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

def Speciality_keyboard():
  keyboard = [[InlineKeyboardButton('Sciences', callback_data='Science')],
              [InlineKeyboardButton('Mathematics', callback_data='Math')],
              [InlineKeyboardButton('mathematical technique', callback_data='Math Tech')],
              [InlineKeyboardButton('Literature and Philosophy', callback_data='Literature and Philosophy')],
              [InlineKeyboardButton('Foreign languages', callback_data='Foreign languages')],
              [InlineKeyboardButton('Management and Economy', callback_data='Management and Economy')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def score_keyboard():
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

def English_keyboard():
  keyboard = [
    [InlineKeyboardButton('Bad "Less than 10"', callback_data='BadatEnglish')],
    [InlineKeyboardButton('Good "10 to 14"', callback_data='GoodatEnglish')],
    [InlineKeyboardButton('Great "14+"', callback_data='GreatatEnglish')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def French_keyboard():
  keyboard = [
    [InlineKeyboardButton('Bad (Less than 10) "I mean what is French?" ', callback_data='BadatFrench')],
    [InlineKeyboardButton('Good (10 to 14) "comment tu tappelles 🥐🥖?"', callback_data='GoodatFrench')],
    [InlineKeyboardButton('Great "14+"', callback_data='GreatatFrench')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def Math_keyboard():
  keyboard = [
    [InlineKeyboardButton('I cant do math (Less than 10)', callback_data='BadatMath')],
    [InlineKeyboardButton('Not bad (10 to 12)', callback_data='GoodatMath')],
    [InlineKeyboardButton('al-Khwarizmi 👳 (12+)', callback_data='GreatatMath')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)
############################Specialities########################################

def save(update,context):
  query = update.callback_query
  chat_id=query.message.chat_id
  context.bot.sendMessage(chat_id=query.message.chat_id,text="🤖:Your answer was {}.".format(query.data))
  for e in range (0,len(token)):
    if chat_id==token[e][0]:
      case = token[e][1]
      Answers[case].append(str(query.data))

  qcounter[case]+=1
  print(Answers)
  redirect(query,qcounter[case],case,context)

################################### Menu's######################################
def redirect(query,i,case,context):
  if(i==0):
    query.edit_message_text(text=score_question(),reply_markup=score_keyboard())
  if(i==1):
    query.edit_message_text(text=Speciality_question(),reply_markup=Speciality_keyboard())
  if(i==2):
    query.edit_message_text(text=English_question(),reply_markup=English_keyboard())
  if(i==3):
    query.edit_message_text(text=French_question(),reply_markup=French_keyboard())
  if(i==4):
    if(Answers[case][0] != "Literature and Philosophy" and Answers[case][0] != "Foreign languages"):
      query.edit_message_text(text=Math_question(),reply_markup=Math_keyboard())
    else:
      qcounter[case]+=1
      redirect(query,qcounter[case],case,context)
  if(i==5):
    message=getdata(Answers[case])
    print(message)
    context.bot.sendMessage(chat_id=query.message.chat_id,text="🤖:Your {}.".format(message))
    
############################# Messages #########################################
def main_welcome():
  return 'Hi how can i help you?'

def abouttext():
  return "I'm a Bot created by three Computer Science students. My job is to help you decide your future, i will give you a choice that might fits you but always remember 'Choose what you like not what others like'"

def nvmtext():
  return 'Alright you can reach me anytime using " /start " have a great day 😄 '

def Speciality_question():
  return 'What is your major in baccalaureate?'

def score_question():
  return 'What was your score in BAC?'

def English_question():
  return 'What best describes your English🇬🇧 grades?'

def French_question():
  return 'What best describes your French🇫🇷 grades?'

def Math_question():
  return 'What best describes your Math📐 grades ?'

def Arabic_question():
  return 'What best describes your Arabic🇩🇿 grades?'

def Physics_question():
  return 'What best describes your Physics🌡️ grades?'

def Science_question():
  return 'What best describes your Sciences🔬 grades?'
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

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='BadatEnglish'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='GoodatEnglish'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='GreatatEnglish'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='BadatFrench'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='GoodatFrench'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='GreatatFrench'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='BadatMath'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='GoodatMath'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='GreatatMath'))


updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='good'))
updater.start_polling()