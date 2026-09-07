LIBMBEDTLS32 = -I../../../$(LIBDIR)/mbedtls-3.1.0/include -L../../../$(LIBDIR)/mbedtls-3.1.0/library -lmbedtls -lmbedcrypto

all: aes_crypt_cbc gcm_starts

aes_crypt_cbc:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBMBEDTLS32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBMBEDTLS32)

gcm_starts:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBMBEDTLS32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBMBEDTLS32)
	