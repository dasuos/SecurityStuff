## Rootkit - rootkit
**DO NOT RUN** on production or persistent hosts. Run only in an isolated disposable VM snapshot only for research/educational purposes

**rootkit.c**
- Educational demo of simple rootkit blocking reboot system call by disabling write protect flag (cr0 register) and overwriting function pointer in the system call table
- By using a virtual machine, compile the kernel module by running <code>make</code> and <code>sudo insmod rootkit.ko</code>, then reboot to verify that the kernel has not shut down, and try to ping the machine
