// i sampled this file from the original https://github.com/ageimer/sok-detection/blob/main/src/common.c
#include "common.h"


char __attribute__((optimize(0)))
NOP(const void* addr, size_t size) {
    return 0;
}

// function used to annotate secrets in Abacus, see https://github.com/s3team/Abacus/
int __attribute__((optimize(0)))
abacus_make_symbolic(uint32_t argc, void **buffers, uint32_t *buflengths) {
  return 1;
}

void printhex(unsigned char* buf, int len) {
    for(int i = 0; i < len; i++)
        printf("%X ",*(buf+i));
}
