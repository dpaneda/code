#include <stdio.h>
#include <string.h>
#include <libmemcached/memcached.h>

void hilazo (void *ptr) {
	memcached_return_t rc;
	size_t value_len;
	uint32_t flags;
	const char *key = "foo";
	char *value;
	int i;

	memcached_st *memc= memcached_create(NULL);
	memcached_server_st *servers = NULL;

	memcached_server_add(memc, "localhost", MEMCACHED_DEFAULT_PORT);

	for (i = 0; i < 1000000; i++)
		value = memcached_get (memc, key, strlen(key), &value_len, &flags, &rc);
	
	memcached_free(memc);
}

void main(void) {
	pthread_t t[4];
	int i;

	for (i = 0; i < 4; i++)
		pthread_create(&t[i], NULL, hilazo, NULL);

	for (i = 0; i < 4; i++)
		pthread_join(t[i], NULL);

	exit(0);
}
