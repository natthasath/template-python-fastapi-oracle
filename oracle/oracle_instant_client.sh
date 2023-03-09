#!/bin/bash

# Define variables
ORACLE_VERSION="11.2.0.4.0"
ORACLE_INSTANT_CLIENT="instantclient-${ORACLE_VERSION}-linux.x64"
ORACLE_BASIC="${ORACLE_INSTANT_CLIENT}-basic.zip"
ORACLE_SDK="${ORACLE_INSTANT_CLIENT}-sdk.zip"
ORACLE_SQLPLUS="${ORACLE_INSTANT_CLIENT}-sqlplus.zip"
ORACLE_URL="https://download.oracle.com/otn/linux/instantclient/${ORACLE_VERSION}/${ORACLE_BASIC}"
ORACLE_SDK_URL="https://download.oracle.com/otn/linux/instantclient/${ORACLE_VERSION}/${ORACLE_SDK}"
ORACLE_SQLPLUS_URL="https://download.oracle.com/otn/linux/instantclient/${ORACLE_VERSION}/${ORACLE_SQLPLUS}"

# Download Instant Client files
curl -L -o "${ORACLE_BASIC}" --cookie "oraclelicense=accept-securebackup-cookie" "${ORACLE_URL}"
curl -L -o "${ORACLE_SDK}" --cookie "oraclelicense=accept-securebackup-cookie" "${ORACLE_SDK_URL}"
curl -L -o "${ORACLE_SQLPLUS}" --cookie "oraclelicense=accept-securebackup-cookie" "${ORACLE_SQLPLUS_URL}"