#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" --header "Content-Type: application/json" -X POST -d '{"name": "amol", "username":"amoljmane", "password":"Janataraja-384"}' http://localhost:8080/v1/reg
echo -e "\n"





            
