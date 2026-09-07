LIBBEARSSL32 = -I../../../$(LIBDIR)/tar/bearssl-0.6/inc -L../../../$(LIBDIR)/bearssl-0.6 -lbearssl

all: aes_big_cbc aes_big_gcm aes_ct_cbc aes_ct_gcm

aes_big_cbc:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)

aes_big_gcm:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)

aes_ct_cbc:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)

aes_ct_gcm:
	@echo "=====> $(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)"
	@$(CC) $(CFLAGS) -m32 ../../common.c $@.c -o $(DESTDIR)/$@-$(SUFFIX) $(LIBBEARSSL32)
