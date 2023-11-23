import re
input_file = 'Input_DSG_Horizon.dat'
output_file = 'output.dat'

header_pattern = r'^3D Horizon, version 1.0'

# Open the input and output files
with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
    # Read the input file line by line
    for line in file_in:
        # Remove leading/trailing whitespace and newline characters
        line = line.strip()

        # Skip lines that match the header pattern
        if re.match(header_pattern, line):
            continue

        # Check if the line contains only numbers
        if re.match(r'^[0-9\s.-]+$', line):
            # Write the valid line to the output file
            file_out.write(line + '\n')



# Replace the original file with the new one
import os
os.replace(output_file, input_file)