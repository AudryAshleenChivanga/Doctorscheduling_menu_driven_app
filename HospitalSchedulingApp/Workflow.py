#!/usr/bin/python3
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

def print_colored(text, color):
    print(f"{color}{text}{Colors.END}")

def display_workflow():
    workflow = """
   [Start]
     |
     v
Display Welcome Message and Hospital Selection
     |
     v
Hospital Selection
     |
     v
Department Selection
     |
     v
Department Selection Input
     |
     v
   Scheduling------------------------>To be Approved by Department of Public Health, Kigali
     |
     v
Appointment Summary
     |
     v
 Repeat or Exit
     |
     v
   [End]
    """
    print_colored(workflow, Colors.GREEN)

if __name__ == "__main__":
    display_workflow()

