
s = "jU5t_a_sna_3lpm12g94c_u_4_m7ra41" 
ans = ""
for i in range(0,8):
    ans+=s[i]
for i in range(15,7,-1):
    ans+=s[i]
for i in range(16,32):
    if(i%2==1):
        ans+=s[i]
    else:
        ans+=s[46-i]

print(ans)

# 8 15
# 9 14

'''
for (i=0; i<8; i++) {
    buffer[i] = password.charAt(i);
}
for (; i<16; i++) {
    buffer[i] = password.charAt(23-i);
}
for (; i<32; i+=2) {
    buffer[i] = password.charAt(46-i);
}
for (i=31; i>=17; i-=2) {
    buffer[i] = password.charAt(i);
}
String s = new String(buffer);
return s.equals("jU5t_a_sna_3lpm12g94c_u_4_m7ra41");
'''
