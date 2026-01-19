#include <stdlib.h>
#include <stdio.h>

int main(void){

	int n = 0xBEEFFACE;

	printf("n = %d\n", n);
	printf("n = %x\n", n);

	int *p = &n; // pointer has 64-bits
	printf("p = %p\n", p);
	printf("p is pointing to: 0x%x\n", *p);

	size_t length = sizeof(int);
	unsigned char* pc = (unsigned char*) p;

	for (size_t i = 0; i < length; i++){
		printf("Address %p\t0x%x\n", pc+i, pc[i]);
	}

	return 0;
}
