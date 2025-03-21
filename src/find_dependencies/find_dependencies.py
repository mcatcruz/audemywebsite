import os
import re

def find_component_usage(component_name, search_path="src/"):
    """
    Searches all Vue files in the project for occurrences of a given component name.
    Returns a list of files where the component is used.
    """
    matches = []
    component_regex = re.compile(rf"\b{component_name}\b", re.IGNORECASE)

    for root, _, files in os.walk(search_path):
        for file in files:
            if file.endswith(".vue"):  # Only check .vue files
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if component_regex.search(content):
                        matches.append(file_path)

    return matches

# 🔹 Change this to search for a different component
component_to_search = "CallToAction"

# 🔹 Run the search
usage_locations = find_component_usage(component_to_search)

# 🔹 Print results
if usage_locations:
    print(f"{component_to_search} is used in:")
    for location in usage_locations:
        print(f"- {location}")
else:
    print(f"No usage found for {component_to_search}.")
