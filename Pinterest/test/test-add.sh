#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" --data "name=foo&value=bar %20 1"  http://localhost:8080/moo/data
echo -e "\n"
