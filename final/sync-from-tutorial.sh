#!/usr/bin/env bash
set -eou pipefail
cd "`dirname "$0"`/.."
d=tutorial; [ -d $d ] || {
	echo "Error: directory \"$PWD/$d\" does not exists! Aborting ..."
	exit 1
}
rsync -av \
	--exclude .git \
	--exclude venv \
	--exclude .pytest_cache \
	--exclude '__*__' \
	--exclude .idea \
	tutorial/ final/
