info = {
    "NAME": "__INSERT NAME__",
    "AGE": "__YOUR AGE__",
    "IS_VERIFIED": True
}
print(info["NAME"])
print(info.get("BIRTHDAY","__INSERT BIRTHDAY__"))
info["BIRTHDAY"] = "_BIRTHDAY_"