#!/bin/bash

#if [ ! -e ~/.jupyter/jupyter_notebook_config.py ]
#then
#  mkdir -vp ~/.jupyter
#  cp -v /curc/tools/jupyterhub/skel/.jupyter/jupyter_notebook_config.py ~/.jupyter/
#fi

if [ ! -e ~/.jupyter/jupyter_notebook_config.json ]
then
  mkdir -vp ~/.jupyter
  cp -v /curc/tools/jupyterhub/skel/.jupyter/jupyter_notebook_config.json ~/.jupyter/
fi

if [ ! -e ~/.jupyter/nbconfig/tree.json ]
then
  mkdir -vp ~/.jupyter/nbconfig
  cp -v /curc/tools/jupyterhub/skel/.jupyter/nbconfig/tree.json ~/.jupyter/nbconfig/
fi
