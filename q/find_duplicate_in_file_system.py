from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        # Use a normal dictionary instead of defaultdict
        d = {}

        # Go through each directory description string
        for s in paths:
            # Split into directory and files
            parts = s.split(" ")
            path = parts[0]   # the folder path
            files = parts[1:] # the remaining are files

            # Process each file in this folder
            for file in files:
                # Find where the '(' starts
                idx = file.index("(")

                # Extract file name (before '(')
                filename = file[:idx]

                # Extract file content (including parentheses)
                content = file[idx:]

                # Full file path = folder path + "/" + filename
                full_path = path + "/" + filename

                # Put into dictionary under the content key
                if content not in d:
                    d[content] = []
                d[content].append(full_path)

        # Now collect only the groups that have duplicates
        result = []
        for content in d:
            if len(d[content]) > 1:
                result.append(d[content])

        return result
