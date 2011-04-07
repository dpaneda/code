#define _GNU_SOURCE

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define SEP	"##########"

typedef struct {
	char *text;
	int line;
	void *next;
} line_list;

line_list * list_add (line_list * llist, char *text, int line) {
	line_list * ll= malloc(sizeof(line_list));
	ll->text = strdup(text);
	ll->line=line;
	ll->next=llist;
	return ll;
}

void list_print (line_list * llist) {
	line_list * iter=llist;

	for ( iter = llist ; iter != NULL; iter=iter->next ) 
		printf("[%d,%s]\n",iter->line,iter->text);
}

line_list * list_found (line_list * llist, char *text) {
	line_list * iter=llist;

	for ( iter = llist ; iter != NULL; iter=iter->next ) 
		if  ( 0 == strcmp(text,iter->text) )
			return iter;
}

int main(int argc, char* argv[])
{
	int opt;
	int verbose=0;
	FILE *fd=0;
	line_list *llist=NULL,*lfound=NULL;
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

	
        while ((read = getline(&line_buffer, &len, fd)) != -1) {
		if (line_buffer[read-1] == '\n')
			line_buffer[read-1] = 0;
		if ( 0 == strcmp(SEP,line_buffer) ) {
			if (verbose)
				printf("Finished\n");
			break;
		}

		llist = list_add (llist,line_buffer,line++);
		if (verbose)
			printf("Added [%d,%s]\n",llist->line,llist->text);
	}

        while ((read = getline(&line_buffer, &len, fd)) != -1) {
		if (line_buffer[read-1] == '\n')
			line_buffer[read-1] = 0;
		if (verbose)
			printf("Testing [%s]\n",line_buffer);

		lfound = list_found(llist, line_buffer);

		if ( NULL != lfound )
			printf("Match at line %d (previously on [%d,%s]\n",line,lfound->line,lfound->text);
		line++;
	}
}
