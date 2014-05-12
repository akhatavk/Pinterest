#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i http://localhost:8080/moo/ping
echo -e "\n"
