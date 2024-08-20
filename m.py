import sys
import time

def perform_bgmi_attack(target_ip, port, time_seconds):
    print(f"BGMI Attack Started. Target: {target_ip}, Port: {port}, Time: {time_seconds} seconds.")
    time.sleep(time_seconds)  # Simulate the time it takes to perform the attack
    print(f"BGMI Attack Finished. Target: {target_ip} Port: {port} Time: {time_seconds}")

def main():
    while True:
        command = input("Enter command: ").strip().split()
        
        if not command:
            continue
        
        if command[0] == '/bgmi' and len(command) == 4:
            try:
                target_ip = command[1]
                port = int(command[2])
                time_seconds = int(command[3])
                perform_bgmi_attack(target_ip, port, time_seconds)
            except ValueError:
                print("Invalid input. Make sure the port and time are numbers.")
        else:
            print("Invalid command or parameters.")

if __name__ == "__main__":
    main()
