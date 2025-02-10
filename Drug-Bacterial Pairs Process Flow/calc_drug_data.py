# script counting statistical diff distribution
import re
from collections import defaultdict

# Regular expression patterns to extract 'diff' and 'label_drug'
diff_pattern = re.compile(r"diff=(0\.\d+)")
label_drug_pattern = re.compile(r"label_drug='([^']+)'")

def parse_tensorpair_file(filename):
    diff_counter = defaultdict(int)
    label_drug_counter = defaultdict(int)
    total_counter = 0

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("TensorPair("):
                total_counter += 1

                diff_match = diff_pattern.search(line)
                label_drug_match = label_drug_pattern.search(line)

                if diff_match:
                    # round off to two decimal place
                    diff = int(float(diff_match.group(1))*100+0.5)
                    diff_counter[diff] += 1

                if label_drug_match:
                    label_drug = label_drug_match.group(1)
                    label_drug_counter[label_drug] += 1

    return diff_counter, label_drug_counter, total_counter

# Usage example
filename = "drugp.log"  # Replace with the actual filename
diff_counter, label_drug_counter, total_counter = parse_tensorpair_file(filename)

print("Diff counter:", diff_counter)
print("Label drug counter:", label_drug_counter)
print("Total counter:", total_counter)