#include <stdio.h>
#include <stdlib.h>
#include <assert.h>





typedef struct cirbuf
{
    int* buf;
    int capacity;
    int readp;
    int writep;
 }cirbuf;

cirbuf init(int capacity){
    cirbuf buffer;
    buffer.buf = (int*)malloc(sizeof(int)*capacity);
    buffer.capacity = capacity;
    buffer.readp = 0;
    buffer.writep = 0;
    return buffer;
}

void read(cirbuf * buf){
    int index = 0;
    int capacity = buf->capacity;
    int tempbuf[capacity];

    while(buf->readp != buf->writep){
        tempbuf[index] = buf->buf[buf->readp]; // Add current node to print 
        buf->readp = (buf->readp +1 )% (buf->capacity);
        index +=1;
    }
    //print for now
    for (int i = 0; i < index; i++)
    {
        printf("%d",tempbuf[i]);
    }

    
}

void write(int num, cirbuf *b){
    b->buf[b->writep] = num;
    b->writep = ((b->writep +1) % b->capacity);
}


int main(){
    cirbuf buf = init(5);





    
}