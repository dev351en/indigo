import ctypes
from ctypes import wintypes

advapi32 = ctypes.windll.advapi32

class CREDENTIAL(ctypes.Structure):
    _fields_ = [
        ('Flags', wintypes.DWORD),
        ('Type', wintypes.DWORD),
        ('TargetName', wintypes.LPWSTR),
        ('Comment', wintypes.LPWSTR),
        ('LastWritten', wintypes.FILETIME),
        ('CredentialBlobSize', wintypes.DWORD),
        ('CredentialBlob', ctypes.POINTER(ctypes.c_char)),
        ('Persist', wintypes.DWORD),
        ('AttributeCount', wintypes.DWORD),
        ('Attributes', ctypes.c_void_p),
        ('TargetAlias', wintypes.LPWSTR),
        ('UserName', wintypes.LPWSTR),
    ]

PCREDENTIAL = ctypes.POINTER(CREDENTIAL)

CredReadW = advapi32.CredReadW
CredReadW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, ctypes.POINTER(PCREDENTIAL)]
CredReadW.restype = wintypes.BOOL

CredFree = advapi32.CredFree
CredFree.argtypes = [ctypes.c_void_p]

targets = ["gemini:antigravity", "git:https://github.com", "github.com", "antigravity"]
for t in targets:
    pcred = PCREDENTIAL()
    if CredReadW(t, 1, 0, ctypes.byref(pcred)):
        cred = pcred.contents
        blob = ctypes.string_at(cred.CredentialBlob, cred.CredentialBlobSize)
        print(f"Target '{t}' found! User: {cred.UserName}, Blob len: {len(blob)}")
        try:
            print("Decoded blob preview:", blob.decode('utf-8')[:30])
        except Exception:
            try:
                print("Decoded utf-16 preview:", blob.decode('utf-16')[:30])
            except Exception:
                pass
        CredFree(pcred)
    else:
        err = ctypes.GetLastError()
        print(f"Target '{t}' not found (error {err})")
