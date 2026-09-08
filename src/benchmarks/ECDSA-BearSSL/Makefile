LIBBEARSSL32 = -I../../../$(LIBDIR)/bearssl-0.6/inc -L../../../$(LIBDIR)/bearssl-0.6 -lbearssl

all: ecdsa_i31_sign_p256

ecdsa_i31_sign_p256:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)
