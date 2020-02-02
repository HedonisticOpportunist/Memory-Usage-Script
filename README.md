# memory_usage_script

This script measures the overall memory usage every 15 seconds. If the usage is greater than 80 %, then information about the overall memory usage will be logged (specifically how much memory is available, how much is being used and how much is free). 

Run the script every time the system starts by running the following commands when configuring/installing the script: 

crontab -e

reboot path to/extension.sh
