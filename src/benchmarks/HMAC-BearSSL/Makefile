LIBBEARSSL32 = -I../../../$(LIBDIR)/bearssl-0.6/inc -L../../../$(LIBDIR)/bearssl-0.6 -lbearssl

all: hmac_out hmac_outCT

hmac_out:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)

hmac_outCT:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)
