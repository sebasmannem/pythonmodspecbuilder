#!/usr/local/bin/bash
os_type=${1:-r7}
docker build -t pghoardbuilder:$os_type -f dockerbuild/Dockerfile.$os_type dockerbuild/

docker run --rm -v $PWD/logs:/targetlogs -v $PWD/rpms:/targetrpms -v $PWD/specs:/targetspecs -v $PWD/SOURCES:/targetsources -v $PWD:/host:ro pghoardbuilder:$os_type /host/build.sh
