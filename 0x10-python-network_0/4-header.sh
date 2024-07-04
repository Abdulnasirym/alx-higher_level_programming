#!/bin/bash
#Sends a gGET request to the URL
HEADER="X-School-User-Id: 98"
curl -s -H "$HEADER" "$1"
