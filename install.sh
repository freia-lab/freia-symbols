#!/bin/bash
rsync -va --exclude '.git' --exclude .project --exclude 'install.sh' --no-o --no-g --no-p --chmod=ug=rwX ./* /opt/epics/opi/bob/freia-symbols/
