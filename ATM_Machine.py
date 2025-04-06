import tkinter as tk
import random
import time
import threading
import sys

try:
    import winsound
    windows = True
except:
    windows = False

# 🔊 Cursed sound effect
def cursed_sound():
    if windows:
        for _ in range(5):
            winsound.Beep(random.randint(300, 800), 200)
            time.sleep(0.1)

# 👻 Cursed popup with keyboard lock
def cursed_popup():
    def glitch_text():
        while True:
            label.config(
                text=random.choice([
                    "⚠️ CURSED TRANSACTION ALERT ⚠️",
                    "🏦 YOUR MONEY IS HAUNTED 🏦",
                    "😱 THE BANK WANTS YOUR SOUL 😱",
                    "💀 RUN. NOW. 💀"
                ]),
                fg=random.choice(["red", "white", "cyan", "magenta", "yellow"]),
                font=("Courier", random.randint(18, 26), "bold")
            )
            root.update()
            time.sleep(0.4)

    if windows:
        threading.Thread(target=cursed_sound, daemon=True).start()

    root = tk.Tk()
    root.title("💀 CURSED ALERT 💀")
    root.configure(bg="black")
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.focus_force()

    # ❌ Disable closing
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    root.bind("<Escape>", lambda e: None)

    # 🚫 Trap all key presses
    def block_keys(event):
        return "break"
    
    root.bind_all("<Key>", block_keys)
    root.bind_all("<Alt-Key>", block_keys)
    root.bind_all("<Control-Key>", block_keys)
    root.bind_all("<Command-Key>", block_keys)

    label = tk.Label(
        root,
        text="⚠️ Your money is cursed. The bank is haunted. Run.",
        fg="red",
        bg="black",
        font=("Courier", 24, "bold")
    )
    label.pack(expand=True)

    threading.Thread(target=glitch_text, daemon=True).start()
    root.mainloop()

# 🏦 ATM Guardian Code
reversed_money = []
money = []
odd_count = 0
even_count = 0
amount = 0
count = 0

while True:
    try:
        withdrawals = int(input("Enter the amount (or -1 to stop): "))
        if withdrawals == -1:
            break
        count += 1
        amount += withdrawals
        money.append(withdrawals)
        reversed_money.append(str(withdrawals)[::-1])
        if withdrawals % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    except:
        print("Invalid input. Try again.")

# 🧠 Digital root
original_amount = amount
while original_amount >= 10:
    sum_of_digits = 0
    while original_amount > 0:
        sum_of_digits += original_amount % 10
        original_amount //= 10
    original_amount = sum_of_digits
digital_root = original_amount

# 🔁 Palindrome curse check
def is_palindrome(n):
    return str(n) == str(n)[::-1]

ritual_amount = amount
cursed = True
for i in range(10):
    reversed_ritual = int(str(ritual_amount)[::-1])
    new_sum = ritual_amount + reversed_ritual
    if is_palindrome(new_sum):
        cursed = False
        break
    ritual_amount = new_sum

# 🧾 Final Output
print("\n🧾 TRANSACTION LOG 🧾")
print("Total withdrawals:", count)
print("Total amount withdrawn:", amount)
print("Odd withdrawals:", odd_count)
print("Even withdrawals:", even_count)
if money:
    print("Maximum withdrawal:", max(money))
    print("Minimum withdrawal:", min(money))
else:
    print("No withdrawals were made.")
print("Reversed withdrawals:", reversed_money)
print("Digital root of total amount:", digital_root)

# 💀 Trigger the curse
if cursed:
    cursed_popup()
