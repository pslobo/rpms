#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

OK=$(tput setaf 2)
RESET=$(tput sgr0)
BOLD=$(tput bold)

specs=( **/*.spec )

for spec in "${specs[@]}"; do
    PACKAGE=$(basename "$spec" | cut -d "." -f1)
    REPO=$(rg -e "URL:\s+(\.*)" -r "\$1" -N "$spec")

    echo "${OK}[INFO]${RESET} ${BOLD}${PACKAGE}${RESET}: checking for updates"

    NEW=$(curl --silent "https://api.github.com/repos/${REPO#*com/}/releases/latest" -H "Accept: application/vnd.github.v3+json" | jq '.name' | tr -d \" | tr -d v)
    CURRENT=$(rg -e "Version:\s+(\.*)" -r "\$1" -N "$spec")

    if [[ $(echo "${CURRENT}" | cut -d "." -f 1) -ge $(echo "${NEW}" | cut -d "." -f 1) ]] && \
       [[ $(echo "${CURRENT}" | cut -d "." -f 2) -ge $(echo "${NEW}" | cut -d "." -f 2) ]] && \
       [[ $(echo "${CURRENT}" | cut -d "." -f 3) -ge $(echo "${NEW}" | cut -d "." -f 3) ]]
    then
	echo "${OK}[INFO]${RESET} ${BOLD}$PACKAGE${RESET}: current version (${CURRENT}) equal to new version (${NEW})"
	continue
    fi

    sed -i -r "s/^(Version:\s+).*$/\1$NEW/" "$spec"
    sed -i -r "s/^(Release:\s+).*$/\11%{?dist}/" "$spec"
    DATETIME=$(LC_TIME=en_US date "+%a %b %d %Y")
    sed -i -r "s/%changelog/%changelog\n* $DATETIME Pedro <rpms@plobo.net> - $NEW-1\n- chore(update): $NEW\n/" "$spec"

    echo "${OK}[INFO]${RESET} ${BOLD}${PACKAGE}${RESET}: updated to version $NEW"

done
