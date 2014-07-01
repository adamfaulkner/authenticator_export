Authenticator Export Script
===========================

Simple script to export Google authenticator database to a collection of QR codes.

This depends on the qrcode python package. Install this with
    pip install qrcode

Usage:

1. Pull the authenticator database from phone somehow. This database lives at:
/data/data/com.google.android.apps.authenticator2/databases/databases

2. run

        python main.py databases

3. QR codes are created in /tmp/qrcode#.png

4. Tweak as needed.
