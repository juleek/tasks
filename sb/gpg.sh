#!/bin/bash

set -e
set -x

while [[ $# -gt 0 ]]
   do
      key="$1"
      case $key in
      --import)
         mkdir -p $GPGH
         echo "secret key" >> $GPGH/key
         exit 0
      ;;
      --sign)
         FILENAME="$2"; shift; shift;
         cat $GPGH/key > $FILENAME.sig
         echo $(md5sum $FILENAME) >> $FILENAME.sig
      ;;
      *)    # unknown option
         echo "unknown option: $key"
         exit 1
      ;;
   esac
done
