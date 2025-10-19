
#include <stdlib.h>
#include <stdio.h>
typedef struct ringBuf
{
    int* arr;
    int capacity;
    int readP;
    int writeP;
    int readloops;
    int writeloops;
} ringBuf;

ringBuf init(int capacity){
    ringBuf buf;
    buf.capacity = capacity;
    buf.arr = (int*)malloc(sizeof(int)*capacity);
    buf.readP = 0;
    buf.writeP = 0;
    buf.readloops = 0;
    buf.readloops = 0;
    return buf;
}

int read(ringBuf* buf){
    // if read is less than write and read loops is less than write loops read
    if(buf->readP  < buf->writeP && buf->readloops <= buf->writeloops ){
        int ret = buf->arr[buf->readP];
        buf->readP = buf->readP + 1;

        //If the buffer is at end of the the list start reading at index 0
        if( buf->readP % buf->capacity -1 == 0){
            buf->readloops +=1;
            buf->readP = 0; 
        }
        return ret;
    }
    //error 
    return -1;
}

void write(int val, ringBuf* buf){
    buf->arr[buf->readP] = val;
    if( buf->writeP % buf->capacity -1 == 0){
        buf->readloops +=1;
        buf->readP = 0; 
     }
}




int main(){
   ringBuf buf = init(3);
   printf("%d", buf.capacity);

}