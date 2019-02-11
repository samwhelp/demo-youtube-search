#!/usr/bin/env bash

./main.sh | php -r '$input = file_get_contents("php://stdin"); var_dump(json_decode($input, true));' | less
