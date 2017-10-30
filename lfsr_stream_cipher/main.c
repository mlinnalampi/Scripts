#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "lfsr.h"



int main(void){
    unsigned char n[5];
    n[0]=0x00;
    n[1]=0x01;
    n[2]=0x01;
    n[3]=0x00;
    n[4]=0x00;

    size_t size = 32;

    unsigned char res[size];

    lfsr(n, res, size);
    for(int i=0;i<32;i++){
        printf("%x", res[i]);
    }
    printf("\n");


}