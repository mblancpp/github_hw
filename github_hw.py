# github_hw.py
# Simulated Network Device Data (8 Devices)
devices = [
    {
        "hostname": "core-sw-01",
        "type": "Switch",
        "ip": "192.168.1.10",
        "location": "HQ Data Center",
        "status": "up",
        "cpu": 45,
        "memory": 60,
        "uptime_days": 120,
        "backup_status": "Success",
    },
    {
        "hostname": "core-sw-02",
        "type": "Switch",
        "ip": "192.168.1.11",
        "location": "HQ Data Center",
        "status": "up",
        "cpu": 85,  # Flagged: High CPU
        "memory": 65,
        "uptime_days": 95,
        "backup_status": "Success",
    },
    {
        "hostname": "edge-rtr-01",
        "type": "Router",
        "ip": "10.0.0.1",
        "location": "HQ Data Center",
        "status": "up",
        "cpu": 30,
        "memory": 82,  # Flagged: High Memory
        "uptime_days": 210,
        "backup_status": "Success",
    },
    {
        "hostname": "branch-rtr-01",
        "type": "Router",
        "ip": "10.10.1.1",
        "location": "Branch Office",
        "status": "down",  # Flagged: Status Down
        "cpu": 0,
        "memory": 0,
        "uptime_days": 0,
        "backup_status": "Failed",
    },
    {
        "hostname": "fw-primary",
        "type": "Firewall",
        "ip": "172.16.0.1",
        "location": "HQ Data Center",
        "status": "up",
        "cpu": 40,
        "memory": 50,
        "uptime_days": 180,
        "backup_status": "Failed",  # Flagged: Backup Failed
    },
    {
        "hostname": "fw-secondary",
        "type": "Firewall",
        "ip": "172.16.0.2",
        "location": "HQ Data Center",
        "status": "up",
        "cpu": 20,
        "memory": 35,
        "uptime_days": 3,  # Flagged: Low Uptime (< 7 days)
        "backup_status": "Success",
    },
    {
        "hostname": "dist-sw-01",
        "type": "Switch",
        "ip": "192.168.2.10",
        "location": "Branch Office",
        "status": "up",
        "cpu": 15,
        "memory": 40,
        "uptime_days": 300,
        "backup_status": "Success",
    },
    {
        "hostname": "dist-sw-02",
        "type": "Switch",
        "ip": "192.168.2.11",
        "location": "Branch Office",
        "status": "up",
        "cpu": 90,  # Flagged: High CPU, High Memory, Failed Backup
        "memory": 88,
        "uptime_days": 15,
        "backup_status": "Failed",
    },
]


def evaluate_device_health(device):
    """Evaluates device data and returns warning flags."""
    flags = []

    if device["status"] != "up":
        flags.append("STATUS DOWN")
    if device["cpu"] > 80:
        flags.append(f"HIGH CPU ({device['cpu']}%)")
    if device["memory"] > 80:
        flags.append(f"HIGH MEMORY ({device['memory']}%)")
    if device["backup_status"] != "Success":
        flags.append("BACKUP FAILED")
    if device["uptime_days"] < 7 and device["status"] == "up":
        flags.append(f"LOW UPTIME ({device['uptime_days']} days)")

    return flags


def print_operational_report(device_list):
    """Calculates totals and prints the operational report."""
    print("=" * 60)
    print("         NETWORK AUTOMATION OPERATIONAL REPORT         ")
    print("=" * 60)

    type_totals = {}
    location_totals = {}
    flagged_devices = []

    for dev in device_list:
        # Totals by Type
        dev_type = dev["type"]
        type_totals[dev_type] = type_totals.get(dev_type, 0) + 1

        # Totals by Location
        loc = dev["location"]
        location_totals[loc] = location_totals.get(loc, 0) + 1

        # Evaluate flags
        issues = evaluate_device_health(dev)
        if issues:
            flagged_devices.append((dev["hostname"], issues))

    print("\n[+] TOTAL DEVICES BY TYPE:")
    for d_type, count in type_totals.items():
        print(f"    - {d_type}: {count}")

    print("\n[+] TOTAL DEVICES BY LOCATION:")
    for loc, count in location_totals.items():
        print(f"    - {loc}: {count}")

    print("\n[!] DEVICES REQUIRING IMMEDIATE ATTENTION:")
    print("-" * 60)
    if flagged_devices:
        for hostname, warnings in flagged_devices:
            print(f"  * Device: {hostname}")
            for w in warnings:
                print(f"      - Issue: {w}")
    else:
        print("  All devices operating within normal parameters.")

    print("=" * 60)
    print(f" Total Devices Analyzed: {len(device_list)}")
    print(f" Total Flagged Devices:  {len(flagged_devices)}")
    print("=" * 60)


if __name__ == "__main__":
    print_operational_report(devices)
# Updated summary calculations for feature branch
