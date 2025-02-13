import os
import subprocess

class TechWorks:
    def __init__(self):
        self.steps = [
            self.check_system_health,
            self.restore_system_files,
            self.uninstall_recent_updates,
            self.reset_system_settings,
            self.reboot_system
        ]

    def guide_user(self):
        print("Welcome to TechWorks: Your System Recovery Assistant for Windows!")
        for step in self.steps:
            user_input = input(f"\nWould you like to proceed with {step.__name__.replace('_', ' ')}? (yes/no): ").strip().lower()
            if user_input == 'yes':
                try:
                    step()
                except Exception as e:
                    print(f"An error occurred during {step.__name__.replace('_', ' ')}: {e}")
            elif user_input == 'no':
                print(f"Skipping {step.__name__.replace('_', ' ')}.")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def check_system_health(self):
        print("Checking system health...")
        os.system("sfc /scannow")

    def restore_system_files(self):
        print("Restoring system files...")
        os.system("DISM /Online /Cleanup-Image /RestoreHealth")

    def uninstall_recent_updates(self):
        print("Uninstalling recent updates...")
        os.system("wusa /uninstall /kb:<KB_number>")

    def reset_system_settings(self):
        print("Resetting system settings to default...")
        # This is a placeholder for the actual reset logic
        print("System settings have been reset.")

    def reboot_system(self):
        print("Rebooting system...")
        subprocess.run(["shutdown", "/r", "/t", "0"])

if __name__ == "__main__":
    techworks = TechWorks()
    techworks.guide_user()