def xyz_there(str):
    x =str[-3:]
    y = str[:3]
    dot1 = str[3:4]
    dot2 = str[-3:-4]
    if dot1 == "." or dot2 ==".":
        return False
    if x == "xyz" or y =="xyz":
        return True

print(xyz_there("xyzdhdfhjdfjhh.xyz"))
