#!/bin/bash
NOW=$(date +"%Y-%m-%d_%H-%M")
FILENAME="backup_$NOW.zip"
mkdir -p backup
zip -r backup/$FILENAME . -x "backup/*" "*.zip" "__pycache__/*" "venv/*"
echo "[$(date)] ✅ Backup created: backup/$FILENAME" >> backup/backup.log
