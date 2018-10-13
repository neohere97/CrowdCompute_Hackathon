import rpyc
import random


class MyService(rpyc.Service):
    def on_connect(self, conn):
        
        pass

    def on_disconnect(self, conn):
        
        pass

    def exposed_get_answer(self,num): 
        rand_sum = 0
        for _ in range(0,num):
            rand_sum+=random.randint(0,100000)
        return rand_sum/num
          

    def get_question(self):  
        return "what is the airspeed velocity of an unladen swallow?"

    
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()