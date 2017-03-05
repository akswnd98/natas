cond = "abcdefghijklmnopqrstuvwxyz"
sent = "waiheacj63wnnibroheqi3p9t0m5nhmh"

result = ""
for x in sent:
    if x in cond:
        result += chr(ord(x) - 32)

    else:
        result += x
