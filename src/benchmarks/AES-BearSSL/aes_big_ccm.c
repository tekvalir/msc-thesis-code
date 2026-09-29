#include "bearssl.h"
#include <stdint.h>
#include <stdio.h>
#define KEY16
#define IV12
#define PLAINTEXT32
#include "../../common.h"

int main() {
    br_aes_big_ctrcbc_keys ctx;
    br_ccm_context ccm_ctx;
    uint8_t tag[16];

    abacus_make_symbolic(1, (void *[]){skey}, (uint32_t[]){KEYLEN});

    br_aes_big_ctrcbc_init(&ctx, skey, (size_t) KEYLEN);
    br_ccm_init(&ccm_ctx, &ctx.vtable);
    br_ccm_reset(&ccm_ctx, iv, (size_t) IVLEN, 0, (uint64_t) DATALEN, 16);

#ifdef DEBUG
    printf("original:\t");
    printhex(plaintext, DATALEN);
#endif

    br_ccm_flip(&ccm_ctx);
    br_ccm_run(&ccm_ctx, 1, plaintext, (size_t) DATALEN);
    br_ccm_get_tag(&ccm_ctx, tag);

#ifdef DEBUG
    uint8_t iv[IVLEN] = { 0x07 };

    printf("\nencrypted:\t");
    printhex(plaintext, DATALEN);

    br_ccm_reset(&ccm_ctx, iv, (size_t) IVLEN, 0, (uint64_t) DATALEN, 16);
    br_ccm_run(&ccm_ctx, 0, plaintext, (size_t) DATALEN);

    printf("\ndecrypted:\t");
    printhex(plaintext, DATALEN);
    printf("\n");
#endif

    return 0;
}
