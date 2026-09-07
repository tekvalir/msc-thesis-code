cd /abacus/Pintools
make PIN_ROOT=/abacus/Intel-Pin-Archive/ TARGET=ia32

cd -

for bfile in bin/AES-BearSSL/*; do
    echo $bfile
    echo "===> /abacus/Intel-Pin-Archive/pin -t /abacus/Pintools/obj-ia32/MyPinToolLinux.so -- ./$bfile"
    /abacus/Intel-Pin-Archive/pin -t /abacus/Pintools/obj-ia32/MyPinToolLinux.so -- "./$bfile"
    echo "===> /abacus/build/App/QIF/QIF ./Inst_data.txt -f Function.txt -d ./$bfile"
    /abacus/QIF-new ./Inst_data.txt -f Function.txt -d "./$bfile" -o ./output.txt 
done