#define _GNU_SOURCE

#include <glib.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>

#define FILL_TABLE	1
#define SEARCH		2

#define ERROR_FILE	"incidentes.log"
#define RESULT_FILE	"results.log"

void print_word_entry (gpointer key, gpointer value, gpointer user_data) {
	GSList *l;
	printf("%s: ",(char *)key);
	for (l = value; l !=NULL; l=l->next) {
		printf("%d ",GPOINTER_TO_INT(l->data));
	}
	printf("\n");
}

void reverse_list (gpointer key, gpointer value, gpointer user_data) {
	g_hash_table_insert(user_data,strdup(key),g_slist_reverse(value));
}

void free_list (gpointer key, gpointer value, gpointer user_data) {
	g_slist_free(value);
}

gchar * normalize_line(const gchar *line,int len) {
	gchar *line_down;
	//line_down=g_utf8_normalize(line,len,G_NORMALIZE_ALL);
	//line_down=g_strdelimit(line, "´",'');
	line_down = g_ascii_strdown(line,-1);
	g_strcanon(line_down, "0123456789qertyuiopasdfghjklzxcvbnm",' ');
	return line_down;
}

int main(int argc, char* argv[])
{
	FILE *fd=NULL,*results,*errors;
	GHashTable *word_hash;
	char *line_buffer=NULL;
	unsigned int line,len,read,mode=0;

	fd = fopen(argv[optind],"r");
	errors = fopen(ERROR_FILE,"w");
	results = fopen(RESULT_FILE,"w");

	if (fd == NULL) {
		fprintf(errors,"Error opening file: %s\n",strerror(errno));
		exit(EXIT_FAILURE);
	}

	word_hash = g_hash_table_new_full(g_str_hash,g_str_equal,g_free,NULL);

	char *a_list="LISTA A\n";
	char *b_list="LISTA B\n";
	
	gchar *p,*line_down;
	GSList * line_list, *aux,*l;

        while ((read = getline(&line_buffer, &len, fd)) != -1) {
		if ( 0 == strcmp(line_buffer,a_list) ) {
			mode=FILL_TABLE; 
			line=1;
			continue;
		} else if ( 0 == strcmp(line_buffer,b_list) ) {
			mode=SEARCH;
			g_hash_table_foreach (word_hash,reverse_list,word_hash);
			//g_hash_table_foreach (word_hash,print_word_entry,NULL);
			line=1;
			continue;
		}
		
		line_down = normalize_line(line_buffer,len);
		p = strtok(line_down," ");
		if (!p) {
			g_free(line_down);
			line++;
			continue;
		}

		if (mode == FILL_TABLE) {
			for (; p!=NULL; p = strtok(NULL," ")) {
				line_list = g_hash_table_lookup(word_hash,p);
				line_list = g_slist_prepend(line_list,GINT_TO_POINTER(line));
				g_hash_table_insert(word_hash,strdup(p),line_list);
			}
		} else if (mode == SEARCH) {
			l = g_hash_table_lookup(word_hash,p);
			line_list=g_slist_copy(l);
	
			for (p=strtok(NULL," "); p && l; p=strtok(NULL," ")) {
				aux = g_hash_table_lookup(word_hash,p);
				l=line_list;
				while (l && aux) {
					if (l->data == aux->data) {
						l=l->next;
						aux=aux->next;
					} else if (l->data < aux->data) {
						line_list=g_slist_remove(line_list,l->data);
						l=l->next;
					} else 
						aux=aux->next;
				}
				for (; l; l=l->next) 
					line_list=g_slist_remove(line_list ,l->data);
			}
	
			for (l=line_list; l; l=l->next) 
				fprintf(results,"A%d_B%d\n",GPOINTER_TO_INT(l->data),line);
	
			g_slist_free(line_list);	
		}

		g_free(line_down);
		line++;
	}

	free(line_buffer);
	fclose(fd);
	fclose(errors);
	fclose(results);
	g_hash_table_foreach(word_hash,free_list,NULL);
	g_hash_table_destroy(word_hash);

	return 0;
}
