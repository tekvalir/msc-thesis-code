#include "bearssl.h"
#include <stdint.h>
#include <stdio.h>
#define KEY16
#define PLAINTEXT32
#include "../../common.h"

int main() {
    br_hmac_context ctx;
    br_sha256_context sha_ctx;
    br_hmac_key_context key_ctx;

    abacus_make_symbolic(1, (void *[]){skey}, (uint32_t[]){KEYLEN});

    br_sha256_init(&sha_ctx);
    br_hmac_key_init(&key_ctx, sha_ctx.vtable, skey, (size_t) KEYLEN);
    br_hmac_init(&ctx, &key_ctx, 0);
    br_hmac_update(&ctx, plaintext, (size_t) DATALEN);

#ifdef DEBUG
    printf("original:\t");
    printhex(plaintext, DATALEN);
#endif

    unsigned char *out = malloc(br_sha256_SIZE);
    if (out == NULL) {
        fprintf(stderr, "Memory allocation failed!\n");
        return 1;
    }

    size_t out_len = br_hmac_out(&ctx, out);

#ifdef DEBUG
    printf("\ntransformed:\t");
    printhex(out, out_len);
    printf("\n");
#endif

    free(out);
    return 0;
}
