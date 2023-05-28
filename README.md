# Ubiquiti_Stock_Script
 
This tool was made to check if a device is in stock in the ubiquiti store. Since ubiquiti is having issues keeping devices in stock this tool can help notify you when a specified device becomes availible. 

# Set up devices.csv
1. create a file named (devices.csv) and place it in the same directory as (ubiquiti.py)

2. Open devices.csv and fill cell A1 with the device name and B1 with the devices link
   Column A is for devices names and column B is for links
   Example
   dream-machine-pro | https://link-to-dream-machine-pro
   g3-flex | https://link-to-g3-flex

3. Save the file and close


# Set ubiquiti.py varibles
at the top of the script you will see 4 variables

    I recommend setting up a burner Gmail account for this step

    fromEmail
        - put your Gmail email address in this string. The script will log into this account.

    password
        - put your Gmail password in this string. Make sure it is an app password set up for mail.
            - go to manage your google account
            - Security
            - signing in to google
            - app passwords
            - allow for mail
            - copy your app password and place it in the password string

    toEmail
        - place your destination email address. Remember you can also email a text message.
            - att      = number@txt.att.net
            - t mobile = number@tmomail.net
            - verizon  = number@vtext.com
            
    check_minutes
        - this variable will pause this script in minutes. Default is set to 10

RUN ubiquiti.py
