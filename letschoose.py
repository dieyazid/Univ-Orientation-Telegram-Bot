from telegram.ext.updater import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, User
from datetime import datetime
#Hello
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
  now = datetime.now()

  current_time = now.strftime("%H:%M:%S")
  print("Current Time   =", current_time)
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

def Thanks():
  keyboard = [[InlineKeyboardButton('Thank you for interacting with me.Hope that i helped you🙋', callback_data='Main')],]
  return InlineKeyboardMarkup(keyboard)

def score_keyboard():
  keyboard = [[InlineKeyboardButton('10 To less than 12', callback_data='10<=Bac<12')],
              [InlineKeyboardButton('12 To less than 14', callback_data='12<=Bac<14')],
              [InlineKeyboardButton('More than 14', callback_data='Bac>=14')],
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
    [InlineKeyboardButton('I cant do math (Less than 10)', callback_data='Math<10')],
    [InlineKeyboardButton('Not bad (10 to less than 12)', callback_data='10<=Math<12')],
    [InlineKeyboardButton('al-Khwarizmi 👳 (12+)', callback_data='Math>=12')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def Physics_keyboard():
  keyboard = [
    [InlineKeyboardButton('Bad at Physics (Less than 10)', callback_data='Physics<10')],
    [InlineKeyboardButton('Not bad (10 to less than 12)', callback_data='10<=Physics<12')],
    [InlineKeyboardButton('I\'m a good physician (12+)', callback_data='Physics>=12')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def English_keyboard():
  keyboard = [
    [InlineKeyboardButton('Bad "Less than 10"', callback_data='English<10')],
    [InlineKeyboardButton('Good "10 to less than 14"', callback_data='10<=English<14')],
    [InlineKeyboardButton('Great "14 or more"', callback_data='English>=14')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def French_keyboard():
  keyboard = [
    [InlineKeyboardButton('Bad (Less than 10) "I mean what is French?" ', callback_data='French<10')],
    [InlineKeyboardButton('Good (10 to less than 14) "comment tu tappelles 🥐🥖?"', callback_data='10<=French<14')],
    [InlineKeyboardButton('Great "14 or more"', callback_data='French>=14')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def Science_keyboard():
  keyboard = [
    [InlineKeyboardButton('Less than 10 ', callback_data='Science<10')],
    [InlineKeyboardButton('10 to less than 12', callback_data='10<=Science<12')],
    [InlineKeyboardButton('12 or more"', callback_data='Science>=12')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def ISL_keyboard():
  keyboard = [[InlineKeyboardButton('Less than 10', callback_data='ISL<10')],
              [InlineKeyboardButton('10 to less than 14', callback_data='10<=ISL<14')],
              [InlineKeyboardButton('14 or more', callback_data='ISL>=14')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def His_Geo_keyboard():
  keyboard = [[InlineKeyboardButton('Less than 10', callback_data='HG<10')],
              [InlineKeyboardButton('10 to less than 14', callback_data='10<=HG<14')],
              [InlineKeyboardButton('14 or more', callback_data='HG>=14')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def Philo_keyboard():
  keyboard = [
    [InlineKeyboardButton('I\'m not into philosophy (less than 10)', callback_data='Philo<10')],
    [InlineKeyboardButton('I\'m quiet Good (10 to less than 14)', callback_data='10<=Philo<14')],
    [InlineKeyboardButton('I\'m the new Socrates🤔 (Bac>=14)', callback_data='Philo>=14')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def Tech_keyboard():
  keyboard = [[InlineKeyboardButton('Less than 10', callback_data='Tech<10')],
              [InlineKeyboardButton('10 to less than 14', callback_data='10<=Tech<14')],
              [InlineKeyboardButton('14 or more', callback_data='Tech>=14')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def Management_keyboard():
  keyboard = [[InlineKeyboardButton('Less than 10', callback_data='MG<10')],
              [InlineKeyboardButton('10 to less than 14', callback_data='10<=MG<14')],
              [InlineKeyboardButton('14 or more', callback_data='MG>=14')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def Economy_keyboard():
  keyboard = [[InlineKeyboardButton('Less than 10', callback_data='EC<10')],
              [InlineKeyboardButton('10 to less than 14', callback_data='10<=EC<14')],
              [InlineKeyboardButton('14 or more', callback_data='EC>=14')],
              [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]]
  return InlineKeyboardMarkup(keyboard)

def Arabic_keyboard():
  keyboard = [
    [InlineKeyboardButton('Less than 10  ', callback_data='Arabic<10')],
    [InlineKeyboardButton('Good (10 to 14)🙋🏻‍♂️ مرحبا"', callback_data='10<=Arabic<14')],
    [InlineKeyboardButton('Great "Bac>=14"', callback_data='Arabic>=14')],
    [InlineKeyboardButton('Main menu⬅️', callback_data='Main')]
              ]
  return InlineKeyboardMarkup(keyboard)
############################Specialities########################################

def save(update,context):
  query = update.callback_query
  chat_id=query.message.chat_id
  # context.bot.sendMessage(chat_id=query.message.chat_id,text="🤖:Your answer was {}.".format(query.data))
  for e in range (0,len(token)):
    if chat_id==token[e][0]:
      case = token[e][1]
      Answers[case].append(str(query.data))

  qcounter[case]+=1
  # print(Answers)
  redirect(query,qcounter[case],case,context)

################################### Menu's######################################
def redirect(query,i,case,context):
  if(i==0):
    query.edit_message_text(text=score_question(),reply_markup=score_keyboard())
  if(i==1):
    query.edit_message_text(text=Speciality_question(),reply_markup=Speciality_keyboard())
  if(i==2):
    if(Answers[case][1] != "Literature and Philosophy" and Answers[case][1] != "Foreign languages"):
      query.edit_message_text(text=Math_question(),reply_markup=Math_keyboard())
    else:
      qcounter[case]+=1
      redirect(query,qcounter[case],case,context)
  if(i==3):
    if(Answers[case][1] != "Literature and Philosophy" and Answers[case][1] != "Foreign languages" and Answers[case][1] != "Management and Economy"):
      query.edit_message_text(text=Physics_question(),reply_markup=Physics_keyboard())
    else:
      qcounter[case]+=1
      redirect(query,qcounter[case],case,context)
  if(i==4):
    query.edit_message_text(text=English_question(),reply_markup=English_keyboard())
  if(i==5):
    query.edit_message_text(text=French_question(),reply_markup=French_keyboard())
  if(i==6):
    if(Answers[case][1] == "Math" or Answers[case][1] == "Science"):
      query.edit_message_text(text=Science_question(),reply_markup=Science_keyboard())
    else:
      qcounter[case]+=1
      redirect(query,qcounter[case],case,context)
  if(i==7):
    query.edit_message_text(text=ISL_question(),reply_markup=ISL_keyboard())
  if(i==8):
    query.edit_message_text(text=His_Geo_question(),reply_markup=His_Geo_keyboard())
  if(i==9):
    query.edit_message_text(text=Philo_question(),reply_markup=Philo_keyboard())
  if(i==10):
    if(Answers[case][1]=="Math Tech"):
      query.edit_message_text(text=Tech_question(),reply_markup=Tech_keyboard())
    else:
      qcounter[case]+=1
      redirect(query,qcounter[case],case,context)
  if(i==11):
    if(Answers[case][1] == "Management and Economy"):
      query.edit_message_text(text=Management_question(),reply_markup=Management_keyboard())
    else:
      qcounter[case]+=1
      redirect(query,qcounter[case],case,context)
  if(i==12):
    if(Answers[case][1] == "Management and Economy"):
      query.edit_message_text(text=Economy_question(),reply_markup=Economy_keyboard())
    else:
      qcounter[case]+=1
      redirect(query,qcounter[case],case,context)
  if(i==13):
    message=getdata(Answers[case])
    # print(message)
    # context.bot.sendMessage(chat_id=query.message.chat_id,text="🤖: {}. ".format(message))
    query.edit_message_text(text="🤖: {}. ".format(message),reply_markup=Thanks())

    
############################# Messages #########################################
def main_welcome():
  return 'Hi how can i help you?'

def abouttext():
  return "I'm a Bot Nice to meet me . My job is to help you decide your next step, i will give you a choice that might fits you"

def nvmtext():
  return 'Alright you can reach me anytime using " /start " have a great day 😄 '
#0
def score_question():
  return 'What was your score in BAC?'
#1
def Speciality_question():
  return 'What is your major in baccalaureate?'
#2
def Math_question():
  return 'What best describes your Math📐 grades ?'
#3
def Physics_question():
  return 'What best describes your Physics🌡️ grades?'
#4
def English_question():
  return 'What best describes your English🇬🇧 grades?'
#5
def French_question():
  return 'What best describes your French🇫🇷 grades?'
#6
def Science_question():
  return 'What best describes your Sciences🔬 grades?'
#7
def ISL_question():
  return 'What best describes your Islamic Law ☪️ grades?'
#8
def His_Geo_question():
  return 'What best describes your History and Geography🗾📜 grades?'
#9
def Philo_question():
  return 'What best describes your Philosophy grades?'
#10
def Tech_question():
  return 'As a Match Tech student there is a additional module that you study based on your speciality. What best describes your grades in it?'
#11
def Management_question():
  return 'What best describes your Management grades?'
#12
def Economy_question():
  return 'What best describes your Economy grades?'
#13
def Arabic_question():
  return 'What best describes your Arabic🇩🇿 grades?'

############################# Handlers #########################################
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('about', about))

updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='start'))
updater.dispatcher.add_handler(CallbackQueryHandler(about, pattern='about'))
updater.dispatcher.add_handler(CallbackQueryHandler(nvm, pattern='Nevermind'))

updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='10<=Bac<12'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='12<=Bac<14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Bac>=14'))

updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Science'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Math'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Math Tech'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Literature and Philosophy'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Foreign languages'))
updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='Management and Economy'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='Math<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<=Math<12'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='Math>=12'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='Physics<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<=Physics<12'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='Physics>=12'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='English<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<=English<14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='English>=14'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='French<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<=French<14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='French>=14'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='Science<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<=Science<12'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='Science>=12'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='ISL<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<=ISL<14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='ISL>=14'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='HG<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<=HG<14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='HG>=14'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='Philo<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<=Philo<14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='Philo>=14'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='Tech<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<=Tech<14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='Tech>=14'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='MG<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<=MG<14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='MG>=14'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='EC<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<=EC<14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='EC>=14'))

updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='Arabic<10'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='10<=Arabic<14'))
updater.dispatcher.add_handler(CallbackQueryHandler(save, pattern='Arabic>=14'))

updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='Main'))

updater.dispatcher.add_handler(CallbackQueryHandler(save,pattern='good'))
updater.start_polling()
