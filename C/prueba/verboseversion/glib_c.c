#define _GNU_SOURCE

#include <glib.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
	int opt;
	int verbose=0;
	FILE *fd=0;
	GHashTable *line_hash;
	GString *lbuffer,*sep;
	gpointer *lfound=NULL;
	char *line_buffer;
	int line=1,len=0,read=0;

	while ((opt = getopt(argc, argv, "v")) != -1) {
		switch (opt) {
			case 'v':
				verbose = 1;
				break;
			default: 
				fprintf(stderr, "Usage: %s [-v] file\n", argv[0]);
				exit(EXIT_FAILURE);
		}
	}

	if (optind >= argc) {
		fprintf(stderr, "Expected file after options\n");
		fprintf(stderr, "Usage: %s [-v] file\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	fd = fopen(argv[optind],"r");

	if (fd == NULL) {
		perror("Critical error");
		exit(EXIT_FAILURE);
	}

	line_hash = g_hash_table_new(g_string_hash,g_string_equal);
	sep = g_string_new("##########");
	
        while ((read = getline(&line_buffer, &len, fd)) != -1) {
		if (line_buffer[read-1] == '\n')
			line_buffer[read-1] = 0;

		lbuffer=g_string_new(line_buffer);

		if ( g_string_equal(sep,lbuffer) ) {
			if (verbose)
				printf("Finished\n");
			break;
		}

		g_hash_table_insert(line_hash,lbuffer,GINT_TO_POINTER(line++));

		if (verbose)
			printf("Added [%d,%s]\n",line,line_buffer);
	}

        while ((read = getline(&line_buffer, &len, fd)) != -1) {
		if (line_buffer[read-1] == '\n')
			line_buffer[read-1] = 0;
		if (verbose)
			printf("Testing [%s]\n",line_buffer);

		lbuffer = g_string_new(line_buffer);
		lfound = g_hash_table_lookup(line_hash, lbuffer);

		if ( NULL != lfound )
			printf("Match at line %d (previously on [%d,%s]\n",line,GPOINTER_TO_INT(lfound),line_buffer);
		line++;
	}
}
