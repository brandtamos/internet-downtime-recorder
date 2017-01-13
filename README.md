# Internet Downtime Recorder
A python script to keep track of how much time your internet connection is down over time. The script creates a file called "data.csv" and records the times the connection goes down and comes back up.

Could possibly be useful for demanding credit on your account from your ISP

### Setup
Place the script wherever your like on your machine. Then, depending on your OS, set up a scheduled task or cron job to run the script every minute (or whatever interval you deem useful).

Included is a windows scheduled task called "Record Internet Downtime.xml" that you can import into the windows task scheduler. This will run the script every minute. You need to modify the User ID and the path to your script in the xml file before importing it.

## License
<img src="https://licensebuttons.net/l/by-nc-sa/3.0/88x31.png" />

This work is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](http://creativecommons.org/licenses/by-nc-sa/4.0/) license.