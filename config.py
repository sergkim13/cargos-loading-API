import os

from dotenv import load_dotenv

load_dotenv()

TRUCK_LENGTH = os.environ.get('TRUCK_LENGTH', 500)  # centimeters
TRUCK_WIDTH = os.environ.get('TRUCK_WIDTH', 200)  # centimeters
TRUCK_HEIGHT = os.environ.get('TRUCK_HEIGHT', 300)  # centimeters
TRUCK_CAPACITY = os.environ.get('TRUCK_CAPACITY', 1000)  # kilograms
GAP = os.environ.get('GAP', 5)  # centimeters
TRUCK_AREA = TRUCK_LENGTH * TRUCK_WIDTH
