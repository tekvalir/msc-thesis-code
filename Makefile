BENCHDIR := src/benchmarks
LIBDIR := lib
BINDIR := bin

GCC_VER := 9
OLEVEL := 2
DEBUG = false

export CC := gcc-${GCC_VER}
export LIBDIR := $(LIBDIR)

export CFLAGS = -static -g -O${OLEVEL}

export SUFFIX = GCC${GCC_VER}-O${OLEVEL}

benchmarks := $(addprefix $(BINDIR)/, $(shell cd $(BENCHDIR)/ && ls -d */))

all: libs

bench: $(benchmarks)

$(benchmarks):
	@echo "==> Building benchmarks in $@"
	@mkdir -p $@
	@cd $(BENCHDIR)/$(subst $(BINDIR)/,,$@) && $(MAKE) DESTDIR=../../../$@

libs:
	@echo "==> Building libs from $(LIBDIR)"
	@cd $(LIBDIR) && $(MAKE)

clean:
	rm -r $(BINDIR)

clean-libs:
	@cd $(LIBDIR) && $(MAKE) clean

clean-abacus:
	rm Function.txt Inst_data.txt pin.log pintool.log result_.Inst_data.txt
