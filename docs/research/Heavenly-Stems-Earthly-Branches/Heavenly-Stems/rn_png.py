import subprocess

data = """
丁1.png  丁3.png  乙2.png  壬2.png  己2.png  庚2.png  戊1.png  甲1.png  甲3.png  癸2.png  辛3.png
丁2.png  乙1.png  壬1.png  己1.png  庚1.png  庚3.png  戊2.png  甲2.png  癸1.png  辛1.png
"""
ordinals = "甲、乙、丙、丁、戊、己、庚、辛、壬、癸"
idx = ordinals.split("、")
def mv_cmd(s):
    n = idx.index(s[0]) + 1
    pfx = str(n).zfill(2)
    return f"mv {s} {pfx}-{s}".split()

m = { d.strip() : mv_cmd(d.strip()) for d in data.split()}

print(m)
# print(idx)

for _,v in m.items():
    print(" ".join(v))
    result = subprocess.run(
        v,
        check=True,  # Raise an exception for non-zero return codes (errors)
        capture_output=True, # Capture stdout and stderr
        text=True # Decode stdout and stderr as text
    )
