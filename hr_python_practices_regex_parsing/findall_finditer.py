ip = "abaabaabaabaae"

import re

match = re.findall(r"(?<=[qwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})[qwrtypsdfghjklzxcvbnm]", ip)

if len(match) > 0:
    print("\n".join(match))
else:
    print('-1')