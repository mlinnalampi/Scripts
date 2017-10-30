#include "lfsr.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void lfsr(const unsigned char* n, unsigned char* res, size_t size){
    unsigned int tmp[6];
    for (int i=0;i<5;i++){tmp[i]=n[i];}
    for (int i=0;i<size;i++){
        for(int j=5;j>0;j--){
            tmp[j]=tmp[j-1];
        }
        tmp[0]=tmp[5]^tmp[2];
        res[i]=tmp[5];
    }
}