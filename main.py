from hdwallet import HDWallet
from os import urandom

# Enter the name of the file that is the address of the desired wallets
filename = "targets.txt"

count = 0
success = 0

print(f"Importing targets from {filename}...")
with open(filename) as f:
    target_address = f.read().split()
    f.close()

print(f"Target count: {len(target_address):,}")
print()


while True:
    count += 1
    private_key = urandom(32).hex()
    hdwallet = HDWallet(symbol='ETH')
    hdwallet.from_private_key(private_key=private_key)
    address = hdwallet.p2pkh_address()

    print(f"Total attempts: {count:,} - Address: {address}", end="\r")

    if address in target_address:
        success += 1
        print()
        print("-" * 40)
        print(f"An address was successfully cracked!\nPrivateKey: {private_key}\nAddress: {address}\nTotal successes: {success:,}\nTotal attempts: {count:,}")
        print("-" * 40)
        print()
        
        with open("CrackedWallets.txt", "a") as f:
            f.write(f"Address: {address}\nPrivateKey: {private_key}\n")
            f.write("-" * 40)
            f.write("\n")
            f.close()
