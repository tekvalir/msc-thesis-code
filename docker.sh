#!/bin/bash

docker build . -t abacus
docker run -v $(pwd):/project -v $(pwd)/../Abacus:/abacus -w /project -it abacus bash