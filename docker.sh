#!/bin/bash

docker build . -t abacus
docker run -v $(pwd):/project -v $(pwd)/../Abacus:/abacus -w /project --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --security-opt apparmor=unconfined -it abacus bash
