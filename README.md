# Clocker Bot

Python Selenium ChromeDriver Bot that can quickly handle clocking events for a CNC employee then sends the user an email confirmation. 

# Requirements
  1. python interpreter 
  2. Selenium
  3. Chromedriver
  4. python dot env
  5. sendgrid-python
  6. Sendgrid account (free)

  **Note:** A Sendgrid account is used to enable email confirmation. If running clocker_bot from the terminal manually, the user will receive confirmation of the clock event in the terminal so in this case the developer may choose to forgo the email confirmation functionality. The Sendgrid function calls in clocker.py will need to be deleted/commented out if so. 

# Installation

### Install python/python3 and pip/pip3
### Clone this repository
### Install [Selenium](https://selenium-python.readthedocs.io/installation.html)
```
pip install selenium
```
### Install [Chromedriver](https://chromedriver.chromium.org/):
  1. First determine which version of chrome you have by opening Chrome > help > About Google Chrome
  2. Choose the version of Chromedriver that matches your major version of Chrome
  3. Unzip and place the chromedriver.exe anywhere you'd like noting its path. The simplest location will be in the repository folder. 

### Install [python-dotenv](https://pypi.org/project/python-dotenv/)
```
pip install python-dotenv
```

### Signup for a free [Sendgrid](https://signup.sendgrid.com/) account
  1. Add your sender email to Sendgrid from the dashboard. 
  2. Navigate to Settings > API Keys and create a new API Key. 
  **WARNING** Sendgrid will only show you this API key ONCE so copy and paste it somewhere safe. 

### Install [sendgrid-python](https://github.com/sendgrid/sendgrid-python) 
Simply install with pip, no need to follow the setup guide in the sendgrid-python github repo
```
pip install sendgrid
```

### Create a .env file in the cloned folder of the form: 

```
# Clocker Secrets
CNC_USR=<your CNC username>
CNC_PW=<your CNC password>
DRIVER_PATH=<path to the chromedriver.exe>

# Confirmer Secrets
SENDGRID_KEY=<Sendgrid API Key>
SG_FROM=<sender email address verified in Sendgrid>
SG_TO=<receiver of the confirmation email>
```

**Note:** The DRIVER_PATH variable needs to be the absolute path to the chromedriver executable. If chromedriver was placed in the repo folder for example:

```
DRIVER_PATH=/Users/ME/Files/clocker_bot/chromedriver
```

**All set!**

# Running

All you have to do is run the clocker bot is run the clocker.py script. Chromedriver will start a new session of Chrome and close the session when complete. 

## Setting up a custom terminal command

The easiest way create a custom terminal command to is create an alias function in the terminal that includes the path to clocker.py. You can avoid directly adding to your PATH by doing such. Instructions on how to create an alias are shown for different shells below. Choose your shell.  

#### bash 
In your .bash_profile or .bashrc file:

```
# Aliases
# alias alias_name="command_to_run"
# alias yourCustomName="<python or python3> <path to clocker.py>"

alias clockme="python3 ~/Developments/clocker_bot/clocker.py"
```
  
#### fish 
In your terminal:

```
alias clockme='python3 $HOME/Development/clocker_bot/clocker.py'
```

Then to save this alias for all sessions:

```
funcsave clockme
```

# Automation

So like this next section is for educational purposes only. No ethical employee would automate their clock events right? 

### Serverless

So an ethical employee would never create an [AWS Lambda cron job](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html). And they definitely wouldn't copy and paste this repo code into a python instance or better yet dockerize this repo and push to Lambda. 

### Self Served

An ethical employee wouldn't purchase a highly efficient [Raspi](https://www.amazon.com/dp/B07XTRFD3Z/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B07XTRFD3Z&pd_rd_w=80WeJ&pf_rd_p=b34bfa80-68f6-4e86-a996-32f7afe08deb&pd_rd_wg=9h5ru&pf_rd_r=D5MJ2F5BD28DB3P81B8Y&pd_rd_r=a95cd0e0-35f9-413e-ad3b-714ab74dac2e&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFOTUVBT0tEV0cyOEUmZW5jcnlwdGVkSWQ9QTAxMjczMzZROU04OExZRzFSVTYmZW5jcnlwdGVkQWRJZD1BMDU1MTEwNDVUV0REQ0hGQ0NYSiZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) and install all the dependencies for clocker_bot in the linux environment along with [crontab](https://opensource.com/article/17/11/how-use-cron-linux) and have the running perpetually. And an ethical employee definitely wouldn't have already calculated the yearly cost of keeping a pi on 24/7 running this light load to be approximately $11.30/year. 

**On a serious note: I am not actually running clocker_bot on a cron job. I work a lot of overtime and I like to keep track of that. Running clocker_bot on a cron, even once, would compromise the integrity of this overtime data. I am however, using a custom React Native application that calls an endpoint that will run clocker_bot for me. When I'm ready to clock in, I simply open the app and press a button. Perhaps sometime in the future that app will be open sourced.**



