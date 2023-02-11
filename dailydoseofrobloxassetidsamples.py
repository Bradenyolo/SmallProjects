import random, time, os, sys
samples = 0

print("-- Daily Dose of Roblox asset ID samples --")
print("-- Created by Python beginner Bradenyolo --")
print("-- This lovely python script will generate asset IDs from late 2017 to right now! --\n")

sampleAmount = int(input("Before you start generating IDs, how many samples do you want?: "))
samples = sampleAmount
    
confirm = input("Would you like to get a list of generated Roblox asset ID samples? Respond with (y/n) to continue: ")

if confirm == "yes" or confirm == "y":
    print(f"Generating {samples} samples, please wait...\n")
    time.sleep(2)
    
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    filename = "asset_storage.txt"
    notefile = "note.txt"
    notepath = os.path.join(desktop, notefile)
    filepath = os.path.join(desktop, filename)

    with open(filepath, "w") as file:
        for i in range(samples):
            asset = random.randint(1000000000, 15000000000)
            file.write(f"https://roblox.com/library/{asset}\n")
    with open(notepath, "w") as file:
        file.write("If some asset IDs didn't work, they were generated, meaning some of them might not exist.")
    
    print(f"Generated asset IDs saved to {filepath}.")
    time.sleep(5)
else:
    sys.exit()
