#!/bin/bash

BASE="http://192.168.56.102/.hidden/"

function crawl() {
  local url=$1

  links=$(curl -s "$url" | grep href | cut -d'"' -f2)

  for link in $links; do
    if [[ "$link" == "../" ]]; then
      continue
    elif [[ "$link" == "README" ]]; then
      echo "[+] $url/README"
      curl -s "$url/README"
    else
      crawl "$url/$link"
    fi
  done
}

crawl "$BASE"
