
from email import message
from experta import *
from telegram import MaskPosition
class Message():
    message=""
    data=[0]*15
class Match():
    Matchcounter=0
    Mifullmatch=Stfullmatch=Enfullmatch=Frfullmatch=Msfullmatch=Mdfullmatch=Ecfullmatch=Bifullmatch=Hsfullmatch=Lwfullmatch=False

class info(Fact):
    pass
        
class MI(KnowledgeEngine):
    @Rule(info(Answer="Math>=12"))
    def Math(self):
        Match.Matchcounter+=1

class ST(KnowledgeEngine):
    @Rule(info(Answer="10<=Math<12") or info(Answer="Math>=12"))
    def Math(self):
        Match.Matchcounter+=1
    @Rule(info(Answer="10<=Physics<12") or info(Answer="Physics>=12"))
    def Physics(self):
        Match.Matchcounter+=1

    @Rule(info(Answer="10<=Tech<12") or info(Answer="Tech>=12"))
    def Technology(self):
        Match.Matchcounter+=1

class MD(KnowledgeEngine):
    @Rule(info(Answer="Physics>=12"))
    def Physics(self):
        Match.Matchcounter+=1
    @Rule(info(Answer="Science>=12"))
    def Science(self):
        Match.Matchcounter+=1

class EC(KnowledgeEngine):
    @Rule(info(Answer="10<=Math<12") or info(Answer="Math>=12"))
    def Math(self):
        Match.Matchcounter+=1

    @Rule(info(Answer="EC>=14"))
    def Economy(self):
        Match.Matchcounter+=1
    
    @Rule(info(Answer="MG>=14"))
    def Management(self):
        Match.Matchcounter+=1

class EN(KnowledgeEngine):
    @Rule(info(Answer="English>=14"))
    def English(self):
        Match.Matchcounter+=1
    if(Message.data[1]=="Literature and Philosophy" or Message.data[1]=="Foreign languages"):
        @Rule(info(Answer="10<=English<=14"))
        def English_(self):
            Match.Matchcounter+=1

class FR(KnowledgeEngine):
    @Rule(info(Answer="English>=14"))
    def French(self):
        Match.Matchcounter+=1
    if(Message.data[1]=="Literature and Philosophy" or Message.data[1]=="Foreign languages"):
        @Rule(info(Answer="10<=English<=14"))
        def French_(self):
            Match.Matchcounter+=1

class MS(KnowledgeEngine):
    @Rule(info(Answer="Science>=12"))
    def Science(self):
        Match.Matchcounter+=1

class BI(KnowledgeEngine):
    @Rule(info(Answer="10<=Science<12") or info(Answer="Science>=12"))
    def Science(self):
        Match.Matchcounter+=1

class HS(KnowledgeEngine):
    @Rule(info(Answer="ISL>=14"))
    def Islamic_law(self):
        Match.Matchcounter+=1
    @Rule(info(Answer="HG>=14"))
    def His_Geo(self):
        Match.Matchcounter+=1
    @Rule(info(Answer="Philo>=14"))
    def Philosophy(self):
        Match.Matchcounter+=1
def getdata(data):
    
    Message.data=data
    Answer()
    # engine = Score()
    # engine.reset()
    # engine.declare(info(Answer=str(Message.data[0])))
    # engine.run()
    return Message.message

def Answer():

    ##Mi Match
    engine = MI()
    engine.reset()
    print(Message.data)
    engine.declare(info(Answer=str(Message.data[2])))
    engine.run()
    if(Match.Matchcounter==1):
        Match.Mifullmatch=True
        print(Match.Mifullmatch)

    Match.Matchcounter=0
    
    ##St Match
    engine = ST()
    engine.reset()

    engine.declare(info(Answer=str(Message.data[2])))
    engine.run()
    
    engine.declare(info(Answer=str(Message.data[3])))
    engine.run()

    if(Message.data[1]=="Math Tech"):
        engine.declare(info(Answer=str(Message.data[8])))
        engine.run()
    
    if(Match.Matchcounter>=2):
        Match.Stfullmatch=True

    Match.Matchcounter=0

    ##Medecine Match
    if(Message.data[0]=="Bac>=14"):
        engine = MD()
        engine.reset()

        engine.declare(info(Answer=str(Message.data[3])))
        engine.run()
        
        engine.declare(info(Answer=str(Message.data[6])))
        engine.run()
        
        if(Match.Matchcounter>=1):
            Match.Mdfullmatch=True
        
        Match.Matchcounter=0

    ##Economics Commerce Science  Match
    engine = EC()
    engine.reset()

    engine.declare(info(Answer=str(Message.data[2])))
    engine.run()

    if(Message.data[1]=="Management and Economy"):
        engine.declare(info(Answer=str(Message.data[8])))
        engine.run()

        engine.declare(info(Answer=str(Message.data[9])))
        engine.run()
        if(Match.Matchcounter>=2):
            Match.Ecfullmatch=True
    else:
        if(Match.Matchcounter==1):
            Match.Ecfullmatch=True

    Match.Matchcounter=0

    ##English
    engine = EN()
    engine.reset()

    engine.declare(info(Answer=str(Message.data[4])))
    engine.run()
    
    if(Match.Matchcounter==1):
        Match.Enfullmatch=True

    Match.Matchcounter=0

    ##French
    engine = FR()
    engine.reset()

    engine.declare(info(Answer=str(Message.data[4])))
    engine.run()
    
    if(Match.Matchcounter==1):
        Match.Frfullmatch=True

    Match.Matchcounter=0

    ##Biology
    engine = BI()
    engine.reset()

    engine.declare(info(Answer=str(Message.data[6])))
    engine.run()
    
    if(Match.Matchcounter==1):
        Match.Bifullmatch=True

    Match.Matchcounter=0

    ##Material Science
    engine = MS()
    engine.reset()

    engine.declare(info(Answer=str(Message.data[6])))
    engine.run()
    
    if(Match.Matchcounter==1):
        Match.Msfullmatch=True

    Match.Matchcounter=0

    ##Human and Social Science
    engine = HS()
    engine.reset()
    if(Message.data[1]=="Foreign languages" or Message.data[1]=="Literature and Philosophy"):
        answerindex=4
    if(Message.data[1]=="Management and Economy"):
        answerindex=5
    if(Message.data[1]=="Math Tech"):
        answerindex=6
    else:
        answerindex=7
    engine.declare(info(Answer=str(Message.data[answerindex])))
    engine.run()

    engine.declare(info(Answer=str(Message.data[answerindex+1])))
    engine.run()

    engine.declare(info(Answer=str(Message.data[answerindex+2])))
    engine.run()
    
    if(Match.Matchcounter==1):
        Match.Hsfullmatch=True

    Match.Matchcounter=0

    ##Law
    Match.Lwfullmatch=True

    Match.Matchcounter=0

    Match.Mifullmatch=Match.Stfullmatch=Match.Enfullmatch=Match.Frfullmatch=Match.Msfullmatch=Match.Mdfullmatch=Match.Ecfullmatch=Match.Bifullmatch=Match.Hsfullmatch=Match.Lwfullmatch=False
    
    Redirect()

def Redirect():
    if(Message.data[1]=="Science" or Message.data[1]=="Math" or Message.data[1]=="Math Tech"):
        if(Match.Mdfullmatch):
            Message.message="Based on your answers i think you can go for Medecine. You can be a great Doctor🧑‍⚕️. check this link below to know more about it\n https://ume.la/i94q4E"
        else:        
            if(Match.Mifullmatch):
                Message.message="Based on your answers i think you can go for Mathematics and Computer Science and maybe oneday you'll code more friends for me 🫠.\n check this link below to know more about it\n https://ume.la/lnlS9U"
            else:
                if(Match.Stfullmatch):
                    Message.message="Based on your answers i think you can go for Science and Technology🧪.\n check this link to know more about it\n https://ume.la/y6ao8e"
                else:
                    if(Match.Msfullmatch and Message.data[1]!="Math Tech"):
                        Message.message="Based on your answers i think you can go for Material Science🧫.\n check this link to know more about it\n https://ume.la/TsKJ3A"
                    else:
                        if(Match.Ecfullmatch):
                            Message.message="Based on your answers i think you can go for Economic, commercial, management sciences 🏦.\n check this link to know more about it\n https://ume.la/RHqLrM"
                        else:
                            if(Match.Bifullmatch and Message.data[1]!="Math Tech"):
                                Message.message="Based on your answers i think you can go for Biology 🧬.\n check this link to know more about it\n https://ume.la/uOQqyf"
                            else:
                                if(Match.Enfullmatch ):
                                    Message.message="Based on your answers i think you can go for English 🇬🇧.\n check this link to know more about it\n https://ume.la/GREHge"
                                else:
                                    if(Match.Hsfullmatch ):
                                        Message.message="Based on your answers i think you can go for Human Sciences 📑 .\n check this link to know more about it\n https://ume.la/3BgrUz"
                                    else:
                                        if(Match.Frfullmatch ):
                                            Message.message="Based on your answers i think you can go for French🇫🇷.\n check this link to know more about it\n https://ume.la/fN8Adv"
                                        else:
                                            if(Match.Lwfullmatch ):
                                                Message.message="Based on your answers i think you can go for Law and political science⚖️.\ncheck this link to know more about it\n https://ume.la/RMCz9q"
    else:
        if(Match.Ecfullmatch and Message.data[1]=="Management and Economy"):
            Message.message="Based on your answers i think you can go for Economic, commercial, management sciences 🏦.\n check this link to know more about it\n https://ume.la/RHqLrM"
        else:
            if(Match.Hsfullmatch):
                Message.message="Based on your answers i think you can go for Human Sciences 📑 .\n check this link to know more about it\n https://ume.la/3BgrUz"
            else:
                if(Match.Lwfullmatch ):
                    Message.message="Based on your answers i think you can go for Law and political science⚖️.\ncheck this link to know more about it\n https://ume.la/RMCz9q"
                else:
                    if(Match.Enfullmatch ):
                        Message.message="Based on your answers i think you can go for English 🇬🇧.\n check this link to know more about it\n https://ume.la/GREHge"
                    else:
                        if(Match.Frfullmatch ):
                            Message.message="Based on your answers i think you can go for French🇫🇷.\n check this link to know more about it\n https://ume.la/fN8Adv"
            