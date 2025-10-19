import csv
import re


def parse_complexity_file(input_file, output_file):
    """
    Parse the complexity report and extract the file summary section to CSV.

    Args:
        input_file: Path to the input text file (G1_complexity.txt)
        output_file: Path to the output CSV file
    """

    with open(input_file, 'r') as f:
        content = f.read()

    # Find the section that starts with the header line
    # Look for the pattern after "============" and before "==========="
    pattern = r'NLOC\s+Avg\.NLOC\s+AvgCCN\s+Avg\.token\s+function_cnt\s+file\s*\n-+\n(.*?)\n=+'

    match = re.search(pattern, content, re.DOTALL)

    if not match:
        print("Could not find the file summary section!")
        return

    # Extract the data section
    data_section = match.group(1).strip()

    # Parse each line
    rows = []
    for line in data_section.split('\n'):
        line = line.strip()
        if not line:
            continue

        # Split by whitespace, but keep the file path together
        parts = line.split()

        if len(parts) >= 6:
            # Extract values
            nloc = parts[0]
            avg_nloc = parts[1]
            avg_ccn = parts[2]
            avg_token = parts[3]
            function_cnt = parts[4]
            # Join remaining parts as the file path
            file_path = ' '.join(parts[5:])

            rows.append([nloc, avg_nloc, avg_ccn, avg_token, function_cnt, file_path])

    # Write to CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        writer.writerow(['NLOC', 'Avg.NLOC', 'AvgCCN', 'Avg.token', 'function_cnt', 'file'])

        # Write data rows
        writer.writerows(rows)

    print(f"Successfully converted {len(rows)} rows to {output_file}")


if __name__ == "__main__":
    import sys
    import os

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Example usage - modify these paths as needed
    input_file = os.path.join(script_dir, "G1_complexity.txt")
    output_file = os.path.join(script_dir, "G1_complexity_summary.csv")

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file not found at: {input_file}")
        print(f"Script directory: {script_dir}")
        print(f"\nPlease specify the correct path to your file:")
        print(f"  Example: python Convert_to_CSV.py /path/to/G1_complexity.txt")

        # If command line argument provided, use it
        if len(sys.argv) > 1:
            input_file = sys.argv[1]
            if len(sys.argv) > 2:
                output_file = sys.argv[2]
            else:
                output_file = input_file.replace('.txt', '_summary.csv')
        else:
            sys.exit(1)

    parse_complexity_file(input_file, output_file)

    # Display the first few rows
    print("\nFirst 5 rows of the CSV:")
    with open(output_file, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i < 6:  # Header + 5 rows
                print(','.join(row))