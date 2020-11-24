# Instagram accounts registrations
Simple registration of Instagram accounts (via email) using Selenium

### Overview ###
To run the script, prepare a list of emails in the *email:password* format in `emails.txt` file. After registration is complete, the logins and passwords of created accounts will be saved in `result.txt` file.
The script selects a random browser (Chrome or Firefox) takes emails, generates random login, password, birthdate (using `utils.py`), checks the form is valid and verificate account taking code from email (using `email_tool.py`). IMAP must be enabled for a successful performance! 

### Requirements ###
* [Selenium](https://pypi.org/project/selenium/)
* Folder *drivers* with [chromedriver](https://chromedriver.chromium.org/) and [geckodriver](https://github.com/mozilla/geckodriver/releases/) inside
* List of emails in `emails.txt` file. Format of rows should be *email:password*
