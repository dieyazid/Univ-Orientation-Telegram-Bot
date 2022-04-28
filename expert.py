
from experta import *
class Message():
    message=""
    data=[]

class info(Fact):
    pass

class Score(KnowledgeEngine):
    @Rule(info(Answer="12-14"))
    def BadMath(self):
        Message.message = "+14 Nicccceee"

class Major(KnowledgeEngine):
    @Rule(info(Answer="Science"))
    def Science(self):
        engine = Science()
        engine.reset()
        engine.declare(info(Answer=Message.data[1]))
        engine.run()

    @Rule(info(Answer="Math"))
    def Math(self):
        Message.message = "Math?"

    @Rule(info(Answer="Bad"))
    def BadMath(self):
        Message.message = "Why?"

class Science(KnowledgeEngine):
    @Rule(info(Answer="12-14"))
    def BadMath(self):
        Message.message = "+14 Nicccceee"
                
engine = Score()
engine.reset()

def getdata(data):
    Message.data=data
    engine.declare(info(Answer=Message.data[0]))
    engine.run()
    return Message.message