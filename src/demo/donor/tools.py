import rpyc

class MyService(rpyc.Service):
    def on_connect(self, conn):
        
        pass

    def on_disconnect(self, conn):
      
        pass

    def exposed_get_answer(self): 
        return "hello ksuhaal"
        

    exposed_the_real_answer_though = 43    

    def get_question(self):  
        return "what is the airspeed velocity of an unladen swallow?"

    
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()