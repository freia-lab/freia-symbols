#!/bin/bash
rsync -va --exclude '.git' --exclude 'install.sh' . /opt/epics/opi/boy/freia-symbols/
