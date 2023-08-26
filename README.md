

## Mass Mailer

A small mass mailer script written in Python3.

## Installation/Setup

1. Create a file in the same directory as the mass mailer script directory called `emails.txt`, inside of this file enter your email list. It should be in the format
```
a@a.com
a@b.com
a@c.com
```

2. Install the dependencies using `pip3 install -r requirements.txt`

3. Create a file called `.env` and enter your details in the following format
```
FROM_ADDRESS=<your email address>
PASSWORD=<your password>
```

> **If your account uses 2FA, you must disable this feature. You will also need to allow insecure apps in your google account settings**

4. Create another file called `body.txt` this will be contain the message that you want to send

## Usage

Once you have completed the `Installation/Setup` step, you can run the file using the following command.

If you are using a plain text body you can run the script with
```
python3 app.py
```

If your `body.txt` file contains HTML, then you must append the `-h` argument
```
python3 app.py -h
```
## Authors

- [@sroffey-github](https://www.github.com/sroffey-github)