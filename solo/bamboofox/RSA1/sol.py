e = 65537
p = 197190551693620844742806745857374013519
q = 202262026640576218403863688407252754551
n = 39884160619925061242382780320938658760471933575219236630625373253059062774969
c = 24336247866805264982828691353056629935309097940841257352771940702851022944390
d = 28153883128598702766301664452252380053381648776689438034556048488686821162873

phi = (p-1)*(q-1)
from Crypto.Util.number import *

print(long_to_bytes(pow(c,d,n)))
