all: lib

lib: bearssl-0.6 mbedtls-3.1.0 # openssl-3.0.5

bearssl-0.6:
	@echo "=====> Building BearSSL 0.6"
	@tar -xf tar/bearssl-0.6.tar.gz
	@patch -p0 < tar/bearssl_conf_patch.diff
	@cd bearssl-0.6 && $(MAKE) CONF=Unix32 BUILD=. lib

mbedtls-3.1.0:
	@echo "=====> Building BearSSL 3.1.0"
	@tar -xf tar/mbedtls-3.1.0.tar.gz
	@patch -p0 < tar/mbedtls-3.1.0_make_patch.diff
	@cd mbedtls-3.1.0 && \
	$(MAKE) no_test CFLAGS="-m32 -g --static -DMBEDTLS_ALLOW_PRIVATE_ACCESS"

clean:
	rm -r bearssl-0.6 mbedtls-3.1.0


# make CC="gcc -m32" \
     CFLAGS="-m32 -O0 -g -fno-pie" \
     LDFLAGS="-m32" \
     no_test
