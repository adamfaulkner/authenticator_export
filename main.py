import sqlite3
import sys
import qrcode

def do_work(filename):
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    c.execute('SELECT * FROM accounts')
    for i, row in enumerate(c.fetchall()):
        email = row[1]
        code = row[2]
        provider = row[5]
        issuer = row[6]
        original_name = row[7]
        formatted = "otpauth://totp/%s?secret=%s&issuer=%s" % (original_name, code, issuer)
        img = qrcode.make(formatted)
        img.save('/tmp/qrcode' + str(i) + '.png')

if __name__ == "__main__":
    do_work(sys.argv[1])
