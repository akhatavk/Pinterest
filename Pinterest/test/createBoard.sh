#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" --header "Content-Type: application/json" -X POST -d '{"boardname":"board2"}' http://localhost:8080/v1/user/amoljmane/board
echo -e "\n"





            
