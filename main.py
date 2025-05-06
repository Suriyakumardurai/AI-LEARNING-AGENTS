from agent import Agent
import time

if __name__ == "__main__":
    for i in range(100):
        agent = Agent()

        print("🌅 A new day begins...\n")
        for hour in range(9, 18):  # 9 AM to 5 PM
            print(f"⏰ {hour}:00")
            action = agent.decide_action()
            agent.perform_action(action)
            time.sleep(1)  # Simulate time passing

        print("\n🌙 Day ends. Reflecting...\n")
        agent.reflect()
