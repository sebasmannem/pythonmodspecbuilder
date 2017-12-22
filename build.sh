#!/bin/bash
set -e

mkdir -p ~/rpmbuild/SOURCES
cp -a /targetsources/* ~/rpmbuild/SOURCES
echo Building snappy. Output redirected to /targetlogs/snappy.log
rpmbuild -ba /targetspecs/snappy.spec 2>&1 | tee /targetlogs/snappy.log

export PKG_CONFIG_PATH=${PKG_CONFIG_PATH}:/usr/local/lib/pkgconfig
export PATH=$PATH:/usr/pgsql-9.6/bin

#Build specbuilder environment
pip3 install xmltodict jinja2 lxml

#Build(=create) specs
echo Building with specbuilder. Output redirected to /targetlogs/specbuilder.log
python3 /host/specbuilder/specbuilder --build --recursive --verbose --package pghoard --package google-api-python-client --package python-swiftclient --template /host/specbuilder/spec.jinja2 --switchfile /targetsources/switchfile --buildermail smannem@bol.com 2>&1 | tee /targetlogs/specbuilder.log

echo Copying specs to /targetspecs
cp -n ~/rpmbuild/SPECS/* /targetspecs

echo Copying sources to /targetsources
cp -n ~/rpmbuild/SOURCES/* /targetsources

echo Copying rpms to /targetrpms
find ~/rpmbuild/RPMS/ -type f | grep -v debuginfo | while read f; do cp $f /targetrpms; done
