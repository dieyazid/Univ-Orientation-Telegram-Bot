from experta import *
class Message():
    message=""
    data=[0]*15
    major=""
    Final_Message=""
class Match():
    Matchcounter=0
    Mifullmatch=Stfullmatch=Enfullmatch=Frfullmatch=Msfullmatch=Mdfullmatch=Ecfullmatch=Bifullmatch=Hsfullmatch=Lwfullmatch=False
class module():
    islamic=english=french=hisgeo=philo=math=physics=science=tech=management=economy=0 
class info(Fact):
    pass
        
class MI(KnowledgeEngine):
    @Rule(info(Answer="Math>=12"))
    def Math(self):
        Match.Matchcounter+=1
        module.math=12
    
    @Rule(info(Answer="10<=Math<12"))
    def Math_(self):
        module.math=10

class ST(KnowledgeEngine):
    @Rule(info(Answer="10<=Math<12"))
    def Math(self):
        Match.Matchcounter+=1
        module.math=10

    @Rule(info(Answer="Math>=12"))
    def Math_(self):
        Match.Matchcounter+=1
        module.math=12

    @Rule(info(Answer="10<=Physics<12"))
    def Physics(self):
        Match.Matchcounter+=1
        module.physics=10

    @Rule(info(Answer="Physics>=12"))
    def Physics_(self):
        Match.Matchcounter+=1
        module.physics=12

    @Rule(info(Answer="10<=Tech<12"))
    def Technology(self):
        Match.Matchcounter+=1
        module.tech=10

    @Rule(info(Answer="Tech>=12"))
    def Technology_(self):
        Match.Matchcounter+=1
        module.tech=12

class MD(KnowledgeEngine):
    @Rule(info(Answer="Physics>=12"))
    def Physics(self):
        Match.Matchcounter+=1
        module.physics=12

    @Rule(info(Answer="10<=Physics<12"))
    def Physics_(self):
        module.math=10

    @Rule(info(Answer="Science>=12"))
    def Science(self):
        Match.Matchcounter+=1
        module.science=12

    @Rule(info(Answer="10<=Science<12"))
    def Science_(self):
        module.science=10

class EC(KnowledgeEngine):
    @Rule(info(Answer="10<=Math<12"))
    def Math(self):
        Match.Matchcounter+=1
        module.math=10

    @Rule(info(Answer="Math>=12"))
    def Math_(self):
        Match.Matchcounter+=1
        module.math=12

    @Rule(info(Answer="EC>=14"))
    def Economy(self):
        Match.Matchcounter+=1
        module.economy=14

    @Rule(info(Answer="10<=EC<14"))
    def Economy_(self):
        module.economy=10
    
    @Rule(info(Answer="MG>=14"))
    def Management(self):
        Match.Matchcounter+=1
        module.management=14

    @Rule(info(Answer="10<=MG<14"))
    def Management_(self):
        module.management=10

class EN(KnowledgeEngine):
    @Rule(info(Answer="English>=14"))
    def English(self):
        Match.Matchcounter+=1
        module.english=14

    @Rule(info(Answer="10<=English<14"))
    def English__(self):
        module.english=10

    if(Message.data[1]=="Literature and Philosophy" or Message.data[1]=="Foreign languages"):
        @Rule(info(Answer="10<=English<=14"))
        def English_(self):
            Match.Matchcounter+=1
            module.english=10

class FR(KnowledgeEngine):
    @Rule(info(Answer="French>=14"))
    def French(self):
        Match.Matchcounter+=1
        module.french=14

    @Rule(info(Answer="10<=French<14"))
    def French__(self):
        module.french=10

    if(Message.data[1]=="Literature and Philosophy" or Message.data[1]=="Foreign languages"):
        @Rule(info(Answer="10<=French<=14"))
        def French_(self):
            Match.Matchcounter+=1
            module.french=10

class MS(KnowledgeEngine):
    @Rule(info(Answer="Science>=12"))
    def Science(self):
        Match.Matchcounter+=1
        module.science=12
    
    @Rule(info(Answer="10<=Science<12"))
    def Science_(self):
        module.science=10

class BI(KnowledgeEngine):
    @Rule(info(Answer="10<=Science<12"))
    def Science(self):
        Match.Matchcounter+=1
        module.science=10

    @Rule(info(Answer="Science>=12"))
    def Science_(self):
        Match.Matchcounter+=1
        module.science=12

class HS(KnowledgeEngine):
    @Rule(info(Answer="ISL>=14"))
    def Islamic_law(self):
        Match.Matchcounter+=1
        module.islamic=14

    @Rule(info(Answer="10<=ISL<14"))
    def Islamic_law_(self):
        module.islamic=10

    @Rule(info(Answer="HG>=14"))
    def His_Geo(self):
        Match.Matchcounter+=1
        module.hisgeo=14

    @Rule(info(Answer="10<=HG<14"))
    def His_Geo_(self):
        module.hisgeo=10

    @Rule(info(Answer="Philo>=14"))
    def Philosophy(self):
        Match.Matchcounter+=1
        module.philo=14

    @Rule(info(Answer="10<=Philo<14"))
    def Philosophy_(self):
        module.philo=10

def getdata(data):
    
    Message.data=data
    Message.major = Message.data[1]
    Answer()
    return Message.message

def Answer():

    ##Mi Match
    if(Message.data[1]=="Science" or Message.data[1]=="Math" or Message.data[1]=="Math Tech"):
        engine = MI()
        engine.reset()
        # print(Message.data)
        engine.declare(info(Answer=str(Message.data[2])))
        engine.run()
        if(Match.Matchcounter==1):
            Match.Mifullmatch=True
            # print(Match.Mifullmatch)

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

        if(Message.data[1]=="Science" or Message.data[1]=="Math"):
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

    ##Economics Commerce Science  Match
    if(Message.data[1]!="Foreign languages" or Message.data[1]!="Literature and Philosophy"):
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

    

    ##Human and Social Science
    engine = HS()
    engine.reset()
    if(Message.data[1]=="Foreign languages" or Message.data[1]=="Literature and Philosophy"):
        answerindex=4
    else :
        if(Message.data[1]=="Management and Economy"):
            answerindex=5
        else:
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

    Redirect()
    
    Match.Mifullmatch=Match.Stfullmatch=Match.Enfullmatch=Match.Frfullmatch=Match.Msfullmatch=Match.Mdfullmatch=Match.Ecfullmatch=Match.Bifullmatch=Match.Hsfullmatch=Match.Lwfullmatch=False
                          
def Redirect():
    # engine = Next()
    # engine.reset()
    # var = {module.math:"math",module.physics:"physics",module.science:"science",module.english:"english",module.french:"french",module.islamic:"islamic",module.hisgeo:"hisgeo",module.economy:"economy",module.management:"management",module.philo:"philo",module.tech:"tech"}

    # engine.declare(info(Answer=str(Message.major)))
    # engine.run()
    science()
    ################################
    engine = Reply()
    engine.reset()
    engine.declare(info(Answer=str(Message.Final_Message)))
    engine.run()
            

def science():
        var = {module.math:"math",module.physics:"physics",module.science:"science",module.english:"english",module.french:"french",module.islamic:"islamic",module.hisgeo:"hisgeo",module.philo:"philo"}
        output = var.get(max(var))
        # print(output)
        match output:
            case "math":
                if(Match.Mifullmatch):
                    Message.Final_Message="Mi"
                else:
                    if(Match.Stfullmatch):
                        Message.Final_Message="St"
                    else:
                        if(Match.Ecfullmatch):
                            Message.Final_Message="Ec"
                        else:
                            Message.Final_Message="Lw"
            case "science":
                if(Match.Mdfullmatch):
                    Message.Final_Message="Md"
                else:
                    if(Match.Msfullmatch):
                        Message.Final_Message="Ms"
                    else:
                        Message.Final_Message="Bi"
            case "english":
                if(Match.Enfullmatch):
                    Message.Final_Message="En"
                else:
                    Message.Final_Message="Lw"
            case "french":
                if(Match.Frfullmatch):
                    Message.Final_Message="Fr"
                else:
                    Message.Final_Message="Lw"
            case _:
                Message.Final_Message="Hs"

       
        


class Reply(KnowledgeEngine):
    @Rule(info(Answer="En"))
    def English(self):
        Message.message="Based on your answers i think you can go for English 🇬🇧.\n check this link to know more about it\n https://ume.la/GREHge"

    @Rule(info(Answer="Fr"))
    def French(self):
        Message.message="Based on your answers i think you can go for French🇫🇷.\n check this link to know more about it\n https://ume.la/fN8Adv"
    
    @Rule(info(Answer="Hs"))
    def Human_Sciences(self):
        Message.message="Based on your answers i think you can go for Human Sciences 📑 .\n check this link to know more about it\n https://ume.la/3BgrUz"
    
    @Rule(info(Answer="Bi"))
    def Biology(self):
        Message.message="Based on your answers i think you can go for Biology 🧬.\n check this link to know more about it\n https://ume.la/uOQqyf"
    
    @Rule(info(Answer="St"))
    def Science_Tech(self):
        Message.message="Based on your answers i think you can go for Science and Technology🧪.\n check this link to know more about it\n https://ume.la/y6ao8e"

    @Rule(info(Answer="Mi"))
    def Comp_Math(self):
        Message.message="Based on your answers i think you can go for Mathematics and Computer Science and maybe oneday you'll code more friends for me 🫠.\n check this link below to know more about it\n https://ume.la/lnlS9U"

    @Rule(info(Answer="Md"))
    def Medecine(self):
        Message.message="Based on your answers i think you can go for Medecine. You can be a great Doctor🧑‍⚕️. check this link below to know more about it\n https://ume.la/i94q4E"

    @Rule(info(Answer="Ms"))
    def Material_Science(self):
        Message.message="Based on your answers i think you can go for Material Science🧫.\n check this link to know more about it\n https://ume.la/TsKJ3A"

    @Rule(info(Answer="Ec"))
    def Economy(self):
        Message.message="Based on your answers i think you can go for Economic, commercial, management sciences 🏦.\n check this link to know more about it\n https://ume.la/RHqLrM"
    
    @Rule(info(Answer="Lw"))
    def Law(self):
        Message.message="Based on your answers i think you can go for Law and political science⚖️.\ncheck this link to know more about it\n https://ume.la/RMCz9q"     