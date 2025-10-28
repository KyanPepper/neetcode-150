


#Rate limiter limit amount of calls.

class RateLimter:
    def __init__(self, x:int):
        self.data = {}
        self.limit = x

        

    def put(self, t:int,) -> bool:
        keys = self.data.keys()
        delkeys = []
        for key in keys:
                if key < t:
                    delkeys.append(key)
        
        for key in delkeys:
             self.data.pop(key)
             
        if t not in self.data:
            self.data[t] = 1
        elif self.data[t] +1 > self.limit:
            return False
        else:
            self.data[t] = self.data[t] + 1
        
        return True


def testRateLimit_callsDoesNotExceedLimit_returns_true():
        r = RateLimter(3)  


        assert r.put(1) == True
        assert r.put(1) == True
        assert r.put(1) == True

        




def testRateLimit_callsDoesNotExceedLimit_returns_false():
        #arrange
        r = RateLimter(3)  

        #act and assert 
        assert r.put(1) == True
        assert r.put(1) == True
        assert r.put(1) == True
        assert r.put(1) == False


def testRateLimit_oldValuesRemoved_dictionaryRemovesKey():
         #arrange
        r = RateLimter(3)  

        #act 
        r.put(1)
        r.put(2)

        #assert 
        assert 1 not in r.data


     
     



testRateLimit_callsDoesNotExceedLimit_returns_false()
testRateLimit_callsDoesNotExceedLimit_returns_true()
testRateLimit_oldValuesRemoved_dictionaryRemovesKey()



        








