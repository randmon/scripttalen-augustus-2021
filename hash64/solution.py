import hashlib
import base64

for i in range(10001):
    sha = hashlib.sha384(str(i).encode('ascii')).digest()
    b64 = base64.b64encode(sha).decode('ascii')
    print(f"{i} {b64}")
#31c79ef0ee467eb05d2d37ac98