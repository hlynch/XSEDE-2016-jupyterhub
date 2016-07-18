#!/bin/bash

for profile in /curc/tools/jupyterhub/skel/.ipython/profile_*
do
    if [ ! -e ~/.ipython/$(basename $profile) ]
    then
        mkdir -vp ~/.ipython
        cp -vnr $profile ~/.ipython/ \
            || echo "Failed to copy default IPython profiles."
    fi
done
