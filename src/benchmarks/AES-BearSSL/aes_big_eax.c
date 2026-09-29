#include "bearssl.h"
#include <stdint.h>
#include <stdio.h>
#define KEY16
#define IV12
#define PLAINTEXT32
#include "../../common.h"

int main() {
    br_aes_big_ctrcbc_keys ctx;
    br_eax_context eax_ctx;
    uint8_t tag[16];

    abacus_make_symbolic(1, (void *[]){skey}, (uint32_t[]){KEYLEN});

    br_aes_big_ctrcbc_init(&ctx, skey, (size_t) KEYLEN);
    br_eax_init(&eax_ctx, &ctx.vtable);
    br_eax_reset(&eax_ctx, iv, (size_t) IVLEN);

#ifdef DEBUG
    printf("original:\t");
    printhex(plaintext, DATALEN);
#endif

    br_eax_flip(&eax_ctx);
    br_eax_run(&eax_ctx, 1, plaintext, (size_t) DATALEN);
    br_eax_get_tag(&eax_ctx, tag);

#ifdef DEBUG
    uint8_t iv[IVLEN] = { 0x07 };

    printf("\nencrypted:\t");
    printhex(plaintext, DATALEN);

    br_eax_reset(&eax_ctx, iv, (size_t) IVLEN);
    br_eax_flip(&eax_ctx);
    br_eax_run(&eax_ctx, 0, plaintext, (size_t) DATALEN);

    printf("\ndecrypted:\t");
    printhex(plaintext, DATALEN);
    printf("\n");
#endif

    return 0;
}
