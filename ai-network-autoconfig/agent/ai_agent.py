import yaml
from config_generator import generate_config
from network_runner import get_running_config, apply_config

def main():
    # 1. Load the fake inventory
    with open("inventory/devices.yml") as f:
        inventory = yaml.safe_load(f)

    for device in inventory["devices"]:
        print(f"\n--- Processing {device['name']} ---")
        
        # 2. Use the 'Dummy' AI to get a config
        intent = "Set hostname to RTR-HQ-CORE and enable OSPF"
        new_config = generate_config(device['vendor'], intent)

        # 3. Simulate checking the device
        running_config = get_running_config(device)

        # 4. If they are different (which they are in our dummy test), "apply" it
        if running_config != new_config:
            print("[!] Drift detected! Updating device...")
            apply_config(device, new_config)
        else:
            print("[✓] Config matches. No changes needed.")

if __name__ == "__main__":
    main()