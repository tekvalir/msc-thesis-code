LIBMBEDTLS32 = -I../../../$(LIBDIR)/mbedtls-mbedtls-2.5.0/include -L../../../$(LIBDIR)/mbedtls-mbedtls-2.5.0/library -lmbedtls -lmbedcrypto

all: rsa_1024

rsa_1024:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBMBEDTLS32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBMBEDTLS32)
