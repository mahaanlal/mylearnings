mydict = {
    "Mahaan":"Gorakhpur",
    "Kapil":"Mathura",
    "Sachin":"Mewat",
    "Yash":"Agra",
    "Vishwas":"Delhi",
    "Kshitiz":"Lucknow"
}
print("Enter a Name:", end="")
a = input("")
print(a, "Lives in:",mydict.get(a))