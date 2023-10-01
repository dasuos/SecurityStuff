#include <linux/module.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/kprobes.h>
#include <linux/syscalls.h>

//rewrite write protect flag stored in the cr0 register
static void overwrite_cr0_register(long value) {
	__asm__ volatile("mov %0, %%cr0" :: "r"(value) : "memory");
}

unsigned long *system_call_table_address;

asmlinkage int (*original_reboot_system_call) (int, int, int, void*);

static struct kprobe _kprobe = {
	.symbol_name = "kallsyms_lookup_name"
};

typedef unsigned long (*kallsyms_lookup_name_t) (const char *name);

unsigned long *get_system_call_table_address(void) {
	register_kprobe(&_kprobe);
	kallsyms_lookup_name_t lookup_name = (kallsyms_lookup_name_t) _kprobe.addr;
	unregister_kprobe(&_kprobe);

	return (unsigned long*) lookup_name("sys_call_table");
}

asmlinkage int blocked_reboot_system_call(int magic1, int magic2, int cmd, void *arg) {
	return EPERM;
}

void overwrite_reboot_system_call_pointer(unsigned long system_call_pointer) {
	//disable write protection
	overwrite_cr0_register(
		read_cr0() & (~0x10000)
	);
	
	system_call_table_address[__NR_reboot] = system_call_pointer;
	
	//enable write protection
	overwrite_cr0_register(
		read_cr0() | (0x10000)
	);
}

static int startup(void) {
	system_call_table_address = get_system_call_table_address();

	//save address for returning reboot system call to the original state
	original_reboot_system_call = (int (*)(int, int, int, void *)) system_call_table_address[__NR_reboot];

	//block reboot system call
	overwrite_reboot_system_call_pointer(
		(unsigned long) blocked_reboot_system_call
	);
	
	return 0;
}

static void __exit shutdown(void) {
	//return reboot system call to the original state
	overwrite_reboot_system_call_pointer(
		(unsigned long) original_reboot_system_call
	);
}

module_init(startup);
module_exit(shutdown);

MODULE_LICENSE("GPL");

