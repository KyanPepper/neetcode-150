from typing import List


class ringbuf:
    def __init__(self,n):
        self.r = 0
        self.w = 0
        self.buf = [-1] * n


    def read(self) -> List[int]:
        ret = []
        while self.r!=self.w:
            ret.append(self.buf[self.r])
            r = (r + 1) % len(self.buf) # overflow will revert back to index 
        

    def write(self, num:int):
        self.buf[self.w] = num
        self.w = (self.w +1) % len(self.buf) 


    




def test_ringbuf_doesnt_overflow():
    #arrange 
    size = 3
    r= ringbuf(size)

    #act
    for i in range(5):
        r.write(2)

    #assert 
    assert len(r.buf) == size

def test_ringbuf_reads():
    #arrange 
    size = 3
    r= ringbuf(size)

    #act
    for i in range(5):
        r.write(2)

    #assert 
    assert len(r.buf) == size




            



        
        