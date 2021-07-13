# Wrapmail

## Installation 

pip install wrapmail

## Google Gmail API Wrapper Setup

This module comes with a wrapper for Google's Gmail api.
Google requires authentication for using the Gmail api. In order to use the wrapper, go to google developers console, create project, register Gmail api.
The only required scope is https://mail.google.com/ Then, you need to download the client_secret json file and include it in your directory. You can change the name of the client secret file or put it into another directory but you should specify the directory of the client secret by setting CLIENT_SECRET environment variable. Wrapmail will first look for the environment variable, if not present it will look for client_secret.json in the working directory. You can also add a search path too.

After you include client_secret.json and instantiated the Gmail class and run the main python file, and automatic authentication window will open and ask you
to sign in. After signing in, if your authentication was successful you will be prompted by message "authentication flow has completed" and a pickle file will be created. As long as pickle file does not expire and is included in your working directory, you won't need to complete these steps. Do not share your client secret file, its contents or your pickle file. The authenticated email address will be used to send mails.

Since OAuth is used, you don't need to allow for less secure apps in your gmail account.

## SMTP Mail Wrapper Setup

This module comes with a wrapper for using SMTP mails.
Before sending mail, you should set environment variables EMAIL and PASSWORD so that wrapmail can login to your account.
If SMTP_SERVER and SMTP_PORT environment variables are given, SMTP wrapper will use them to connect to the server; if not present it will use smtp.gmail.com with port 587.

You don't need to stick with gmail for this wrapper but you need to declare SMTP_SERVER and SMTP_PORT environment variables to match with the smtp service your email provider of choice uses.

Sometimes email providers restrict usage of SMTP servers, so if you have problem connecting with an email provider through this wrapper you may want to check smtp guidelines of your email provider. For example, for using Google's smtp services you need to allow for less secure apps (https://support.google.com/accounts/answer/6010255?hl=en)

## Initializing mail instance

Initialize mail object by invoking the constructor and passing parameters TO (mail adress of the target, *not your mail adress*), MSG (message as string) and TITLE (title of the message).

## Using HTML Mail

You can send an html mail by not passing MSG while invoking the constructor and passing html parameter instead.

## Attachments

You can invoke .add_attachment() method on instances of both wrappers and pass directory of the attachment as string. You can invoke add_attachment multiple times which will result in multiple attachments. Both wrappers are tested for png, jpg and pdf files (and their permutations as multiple attachments)

## Sending the mail

After you initialized everything regarding the mail, you can invoke .send() method. It is a good idea to surround this with a try-except block and log problems in case an unexpected thing such as network problem occurs.
