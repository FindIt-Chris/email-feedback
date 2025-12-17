
from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ========================
# KONFIGURATION
# ========================

SHEET_NAME = "Shop List"
WORKSHEET_NAME = "Feedback on the email of interest"

# ========================
# APP
# ========================

app = Flask(__name__)

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

CREDS = ServiceAccountCredentials.from_json_keyfile_name(
    "interest-emailfeedback-555d3050a45c.json", SCOPE
)

client = gspread.authorize(CREDS)
sheet = client.open(SHEET_NAME).worksheet(WORKSHEET_NAME)


def schreibe_antwort(antwort):
    if antwort == "yes":
        sheet.append_row(["", 1, ""])
    elif antwort == "no":
        sheet.append_row(["", "", 1])


@app.route("/yes")
def yes():
    schreibe_antwort("yes")
    return render_template("danke.html")


@app.route("/no")
def no():
    schreibe_antwort("no")
    return render_template("danke.html")


# ========================
# TERMINAL-AUSGABE (FESTE, FUNKTIONIERENDE LINKS)
# ========================

if __name__ == "__main__":

    BASE_URL = "http://127.0.0.1:5000"

    print("\n========================")
    print("FERTIGE LINKS (KOPIEREN & IN E-MAIL EINFÜGEN)")
    print("========================\n")
    print("YES LINK:")
    print(f"{BASE_URL}/yes")
    print("\nNO LINK:")
    print(f"{BASE_URL}/no")
    print("\n========================\n")

    app.run(host="0.0.0.0", port=5000)
