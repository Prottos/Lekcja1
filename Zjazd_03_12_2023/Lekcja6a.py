import os
import re

# for root, dirs, files in os.walk("."):
#     for name in files:
#         if "Zjazd" in root:
#             print(root, name)
#         else:
#             pass

# for root, dirs, files in os.walk("."):
#     for name in files:
#         x = re.search("\.git", root)
#         if x is None:
#             print(root, files)
#         else:
#             pass

walk_results = list(os.walk("F:\\WSB\\Lekcja1"))
# print(walk_results)
print(walk_results[1])