import datetime
import base64
import os

def update_stream_time():
    print("--- NMS Stream Tracker: Auto Time Updater ---")
    
    try:
        # 1. Automatically grab the CURRENT local time
        dt = datetime.datetime.now()
        formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"[+] Captured Current Time: {formatted_time}")
        
        # 2. Convert to an Epoch timestamp
        epoch_time = int(dt.timestamp())
        
        # 3. Encode the timestamp to Base64
        epoch_str = str(epoch_time)
        b64_encoded = base64.b64encode(epoch_str.encode('utf-8')).decode('utf-8')
        
        print(f"[+] Epoch Timestamp generated: {epoch_time}")
        print(f"[+] Base64 Encoded String: {b64_encoded}")
        
        # 4. Read the HTML file
        file_name = 'index.html'
        
        if not os.path.exists(file_name):
            print(f"\n[-] ERROR: '{file_name}' not found!")
            print("Make sure this python script is in the exact same folder as your index.html file.")
            input("\nPress Enter to exit...")
            return
            
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        # 5. Search line-by-line and replace
        found_target = False
        for i, line in enumerate(lines):
            if "const START_TIME_B64" in line:
                lines[i] = f'const START_TIME_B64 = "{b64_encoded}";\n'
                found_target = True
                break
        
        if not found_target:
            print(f"\n[-] ERROR: Could not find the 'const START_TIME_B64' line in {file_name}.")
            print("Did you accidentally delete it from the HTML?")
            input("\nPress Enter to exit...")
            return
            
        # 6. Save the file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.writelines(lines)
            
        print(f"\n[+] SUCCESS! '{file_name}' has been updated with the current time.")
        print("    You can now push the updated index.html to GitHub.")
        
    except Exception as e:
        print(f"\n[-] An unexpected error occurred: {e}")

    # This stops the window from instantly closing on Windows
    input("\nPress Enter to close this window...")

if __name__ == "__main__":
    update_stream_time()