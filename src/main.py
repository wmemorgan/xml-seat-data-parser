"""Convert XML Seat Data to JSON

This script extracts seat data from an OTA airline booking system
file and outputs it to JSON format.

This tool accepts OTA xml files (.xml).

This script imports the 'getSeatData' module to extract
and shape seat data.

This file can also be imported as a module and contains the following
functions:

    * read_xml_file - reads the OTA xml file
    * create_json_file - outputs the seat data to a JSON file
    * main - the main function of the script
"""

import json
from getSeatData import get_seat_data


def create_json_file(data, output_file):
    json_data = json.dumps(data)

    with open(f"../output/{output_file}", "w") as json_file:
        json_file.write(json_data)
        json_file.close()

def main():
    seat_info = get_seat_data()
    print(len(seat_info))
    create_json_file(seat_info, "seatinfo.json")

if __name__ == "__main__":
    main()

