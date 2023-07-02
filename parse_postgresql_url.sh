#!/bin/bash

read -p "Enter external database url: " url

url=${url#*//}
IFS=":/@"
read -ra url_parts <<< "$url"
port=5432

echo "Server: ${url_parts[2]}"
echo "Database: ${url_parts[3]}"
echo "Port: ${port}"
echo "Username: ${url_parts[0]}"
echo "Password: ${url_parts[1]}"