LIBBEARSSL32 = -I../../../$(LIBDIR)/bearssl-0.6/inc -L../../../$(LIBDIR)/bearssl-0.6 -lbearssl

all: rsa_i31_oaep_decrypt

rsa_i31_oaep_decrypt:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)
