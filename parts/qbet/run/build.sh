#!/bin/bash
set -euo pipefail
source /home/cube/Gh-sync/opendev-labs/QBET/parts/qbet/run/environment.sh
set -x
cp --archive --link --no-dereference . "/home/cube/Gh-sync/opendev-labs/QBET/parts/qbet/install"
