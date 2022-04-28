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

def score_keyboard():
  keyboard = [[InlineKeyboardButton('10 To less than 12', callback_data='10-12')],
              [InlineKeyboardButton('12 To less than 14', callback_data='12-14')],
              [InlineKeyboardButton('More than 14', callback_data='14+')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
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

def Math_keyboard():
  keyboard = [
    [InlineKeyboardButton('I cant do math (Less than 10)', callback_data='BadatMath')],
    [InlineKeyboardButton('Not bad (10 to less than 12)', callback_data='GoodatMath')],
    [InlineKeyboardButton('al-Khwarizmi 👳 (12+)', callback_data='GreatatMath')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def Physics_keyboard():
  keyboard = [
    [InlineKeyboardButton('Bad at Physics (Less than 10)', callback_data='BadatPhysics')],
    [InlineKeyboardButton('Not bad (10 to less than 12)', callback_data='GoodatPhysics')],
    [InlineKeyboardButton('I\'m a good physician (12+)', callback_data='GreatatPhysics')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def English_keyboard():
  keyboard = [
    [InlineKeyboardButton('Bad "Less than 10"', callback_data='BadatEnglish')],
    [InlineKeyboardButton('Good "10 to less than 14"', callback_data='GoodatEnglish')],
    [InlineKeyboardButton('Great "14 or more"', callback_data='GreatatEnglish')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def French_keyboard():
  keyboard = [
    [InlineKeyboardButton('Bad (Less than 10) "I mean what is French?" ', callback_data='BadatFrench')],
    [InlineKeyboardButton('Good (10 to less than 14) "comment tu tappelles 🥐🥖?"', callback_data='GoodatFrench')],
    [InlineKeyboardButton('Great "14 or more"', callback_data='GreatatFrench')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def Science_keyboard():
  keyboard = [
    [InlineKeyboardButton('Less than 10 ', callback_data='BadatScience')],
    [InlineKeyboardButton('10 to less than 12', callback_data='GoodatScience')],
    [InlineKeyboardButton('12 or more"', callback_data='GreatatScience')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def Islamic_keyboard():
  keyboard = [[InlineKeyboardButton('Less than 10', callback_data='BadatISL')],
              [InlineKeyboardButton('10 to less than 14', callback_data='GoodatISL')],
              [InlineKeyboardButton('14 or more', callback_data='GreatatISL')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def His_Geo_keyboard():
  keyboard = [[InlineKeyboardButton('Less than 10', callback_data='BadatHG')],
              [InlineKeyboardButton('10 to less than 14', callback_data='GoodatHG')],
              [InlineKeyboardButton('14 or more', callback_data='GreatatHG')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def Philo_keyboard():
  keyboard = [
    [InlineKeyboardButton('I\'m not into philosophy (less than 10)', callback_data='BadatPhilo')],
    [InlineKeyboardButton('I\'m quiet Good (10 to less than 14)', callback_data='GoodatPhilo')],
    [InlineKeyboardButton('I\'m the new Socrates🤔 (14+)', callback_data='GreatatPhilo')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def Technologie_keyboard():
  keyboard = [[InlineKeyboardButton('Less than 10', callback_data='BadatTech')],
              [InlineKeyboardButton('10 to less than 14', callback_data='GoodatTech')],
              [InlineKeyboardButton('14 or more', callback_data='GreatatTech')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def Management_keyboard():
  keyboard = [[InlineKeyboardButton('Less than 10', callback_data='BadatMG')],
              [InlineKeyboardButton('10 to less than 14', callback_data='GoodatMG')],
              [InlineKeyboardButton('14 or more', callback_data='GreatatMG')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def Economy_keyboard():
  keyboard = [[InlineKeyboardButton('Less than 10', callback_data='BadatEC')],
              [InlineKeyboardButton('10 to less than 14', callback_data='GoodatEC')],
              [InlineKeyboardButton('14 or more', callback_data='GreatatEC')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def Arabic_keyboard():
  keyboard = [
    [InlineKeyboardButton('Less than 10  ', callback_data='BadatArabic')],
    [InlineKeyboardButton('Good (10 to 14)🙋🏻‍♂️ مرحبا"', callback_data='GoodatArabic')],
    [InlineKeyboardButton('Great "14+"', callback_data='GreatatArabic')],
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

def score_question():
  return 'What was your score in BAC?'

def Speciality_question():
  return 'What is your major in baccalaureate?'

def Math_question():
  return 'What best describes your Math📐 grades ?'

def Physics_question():
  return 'What best describes your Physics🌡️ grades?'

def English_question():
  return 'What best describes your English🇬🇧 grades?'

def French_question():
  return 'What best describes your French🇫🇷 grades?'

def Science_question():
  return 'What best describes your Sciences🔬 grades?'

def ISL_question():
  return 'What best describes your Islamic Law ☪️ grades?'

def His_Geo_question():
  return 'What best describes your History and Geography🗾📜 grades?'

def Philosophy_question():
  return 'What best describes your Philosophy grades?'

def Tech_question():
  return 'What best describes your Technology grades?'

def Management_question():
  return 'What best describes your Management grades?'

def Economy_question():
  return 'What best describes your Economy grades?'

def Arabic_question():
  return 'What best describes your Arabic🇩🇿 grades?'

############################# Handlers #########################################
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('about', about))

updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='start'))
updater.dispatcher.add_handler(CallbackQueryHandler(about, pattern='about'))
updater.dispatcher.add_handler(CallbackQueryHandler(nvm, pattern='Nevermind'))

updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Science'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Math'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Math Tech'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Literature and Philosophy'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Foreign languages'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Management and Economy'))

updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='10-12'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='12-14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='14+'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='BadatEnglish'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='GoodatEnglish'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='GreatatEnglish'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='BadatFrench'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='GoodatFrench'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='GreatatFrench'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='BadatMath'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='GoodatMath'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='GreatatMath'))

updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='Main'))

updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='good'))
updater.start_polling()