from client import SelfDrivingWebApplicationActionDriverClient

def main():
    client = SelfDrivingWebApplicationActionDriverClient()
    res = client.drive_web_task("https://app.cloudprovider.internal", "Download August invoice")
    print(f"Goal Accomplished: {res['goal_accomplished']}")
    print(f"Actions Executed: {res['actions_executed_count']}")
    print(f"Summary: {res['final_state_summary']}")

if __name__ == "__main__":
    main()
