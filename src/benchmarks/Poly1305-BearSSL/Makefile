LIBBEARSSL32 = -I../../../$(LIBDIR)/bearssl-0.6/inc -L../../../$(LIBDIR)/bearssl-0.6 -lbearssl

all: poly1305_ctmul_chacha20_ct poly1305_ctmul_chacha20_sse2

poly1305_ctmul_chacha20_ct:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)

poly1305_ctmul_chacha20_sse2:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)
