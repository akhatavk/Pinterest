#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" --header "Content-Type: application/json" -X POST -d '{"username":"amoljmane", "password":"Janataraja-3841"}' http://localhost:8080/v1/login
echo -e "\n"





            
