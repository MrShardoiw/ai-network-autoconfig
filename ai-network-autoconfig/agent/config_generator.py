def generate_config(vendor, intent):
    print(f"[SIMULATION] AI is processing intent: {intent}")
    
    # This is a 'Dummy' response. It returns a valid Cisco config 
    # without calling any external API or account.
    dummy_cisco_config = """hostname RTR-HQ-CORE
!
interface GigabitEthernet0/0
 ip address 192.168.10.1 255.255.255.0
 no shutdown
!
router ospf 1
 network 192.168.10.0 0.0.0.255 area 0
!
end"""
    return dummy_cisco_config