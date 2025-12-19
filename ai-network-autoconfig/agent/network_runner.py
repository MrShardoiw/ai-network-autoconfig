import os

def get_running_config(device):
    print(f"[SIMULATION] Connecting to {device['host']}...")
    # In a real setup, Netmiko would go here. 
    # For the dummy version, we return an empty config to trigger 'drift'.
    return "hostname old-router" 

def apply_config(device, config):
    print(f"[SIMULATION] Successfully pushed to {device['name']} ({device['host']})")
    print("--- Applied Config ---")
    print(config)
    print("----------------------")