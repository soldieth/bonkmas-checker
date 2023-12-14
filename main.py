import requests


if __name__ == '__main__':
    with open("wallets.txt", "r") as file:
        wallets = list(file.read().split("\n"))
    eligible = ""
    for wallet in wallets:
        r = requests.get(f"https://bonkmas.com/api/eligibility?wallet={wallet}").json()
        if r['message'] == "Wallet is eligible.":
            print(f"{wallet} is eligible.")
            eligible += f'{wallet}\n'
    with open("eligible.txt", "w") as file:
        file.write(eligible)
    input("Wallets checked. Check 'eligible.txt'. Good luck.\nWith best wishes from soldi.eth.freesoldev.acoservice - https://t.me/soldidi")


