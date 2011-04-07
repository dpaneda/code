#include <glib.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <iostream>
#include <fstream>

using namespace std;

#define FILL_TABLE	1
#define SEARCH		2
#define BUFFER_SIZE	1024

/* Funcion de debug que imprime una entrada de la tabla hash */
void print_word_entry (gpointer key, gpointer value, gpointer user_data) {
	GSList *l=(GSList *)value;
	printf("%s: ",(char *)key);
	for (; l !=NULL; l=l->next) {
		printf("%d ",GPOINTER_TO_INT(l->data));
	}
	printf("\n");
}

void free_list (gpointer key, gpointer value, gpointer user_data) {
	g_slist_free((GSList *)value);
}

/* Calcula los elementos comunes a las listas dadas. Esta funcion tiene como precondicion
 * que las listas esten ordenadas de forma descendente para funcionar correctamente 
 */
GSList * g_slist_intersection (GSList *l, GSList *l2) {
	GSList *result=NULL;
	for (;l && l2;) {
		if (l->data == l2->data) {
			result=g_slist_prepend(result,l->data);
			l=l->next;
			l2=l2->next;
		} else if (l->data > l2->data) 
			l=l->next;
		else 
			l2=l2->next;
	}
	return result;
}

/* WARNING: Esta funcion solo funciona con codificacion 8859 */
void normalize_line(guchar *str) {
        for (int i=0 ; ; i++) {
		switch (str[i]) {
			case '\0':
				return;
			case 193:
			case 225:
				str[i]='a';
				break;
			case 201:
			case 233:
	                        str[i]='e';
				break;
			case 205:
			case 237:
				str[i]='i';
				break;
			case 211:
			case 243:
				str[i]='o';
				break;
			case 218:
			case 250:
	                        str[i]='u';
		}
		if (isalnum(str[i]))
			str[i]=tolower(str[i]);
		else
			str[i]=' ';
        }
}

/*
 * Clase para la busqueda de frases
 *
 * La clase usa una tabla hash para guardar las palabras encontradas en las frases
 * de "LISTA A" con alguna optimizacion para mejorar el rendimiento:
 *
 * - Los valores de la tabla hash son una lista ordenada de numeros que indican las 
 *   en donde aparece dicha palabra. Esta ordenacion permite bajar en un orden de 
 *   magnitud la comparacion de las listas pasando de un O(n^2) a O(n). El orden es
 *   descendente para evitar la necesidad de una insercion ordenada.
 *
 * - La busqueda en la tabla hash se hace realizando intersecciones de las listas de 
 *   palabras de la linea a buscar para minimizar la longitud de la listas a crear y 
 *   por tanto el tiempo de busqueda.
 *
 *   - El tratamiento de la linea se hace con una funcion propia (normalize_line) no
 *   muy elegante pero mucho mas eficiente que usar otras funciones externas.
 *
 */
class frases {
	
	private:
		GHashTable *word_hash;
		char *results;
		GString *error_msg;

	public:
		frases(const char * word_file, const char * result_file);
		~frases();
		void result();
		void salida(char *);
};

frases::frases(const char *word_file, const char *result_file) {
	FILE *fd=NULL,*fresults=NULL;
	char *line_buffer=NULL;
	unsigned int line,mode=0;
	ssize_t read;
	size_t len;
	error_msg=g_string_new("");

	if (0 == strcmp(word_file,""))
		word_file = "minilorem2";

	if (0 == strcmp(result_file,""))
		results = strdup("results.log");
	else 
		results = strdup(result_file);

	if ( ! (fd = fopen(word_file,"r")) ) {
		g_string_printf(error_msg,"Error opening words file: %s", strerror(errno));
		throw error_msg;
	}
	if ( ! (fresults = fopen(results,"w")) ) {
		g_string_printf(error_msg,"Error opening words file: %s", strerror(errno));
		throw error_msg;
	}

	word_hash = g_hash_table_new_full(g_str_hash,g_str_equal,g_free,NULL);

	gchar *p;
	GSList * line_list,*aux,*l,*g;

        while ((read = getline(&line_buffer, &len, fd)) != -1) {
		if ( 0 == strcmp(line_buffer,"LISTA A\n") ) {
			mode=FILL_TABLE; 
			mode=1;
			line=1;
			continue;
		} else if ( 0 == strcmp(line_buffer,"LISTA B\n") ) {
			mode=SEARCH;
			line=1;
			g_hash_table_foreach (word_hash,print_word_entry,NULL);
			continue;
		}
		
		normalize_line((guchar *)line_buffer);
		p = strtok(line_buffer," ");
		if (!p) {
			line++;
			continue;
		}

		if (mode == FILL_TABLE) {
			for (; p!=NULL; p = strtok(NULL," ")) {
				line_list = (GSList *) g_hash_table_lookup(word_hash,p);
				line_list = (GSList *) g_slist_prepend(line_list,GINT_TO_POINTER(line));
				g_hash_table_insert(word_hash,strdup(p),line_list);
			}
		} else if (mode == SEARCH) {
			l = (GSList *) g_hash_table_lookup(word_hash,p);

			p=strtok(NULL," ");
			if (!p) 
				line_list=g_slist_copy(l);
			else 
				line_list=NULL;

			for (; p && l; p=strtok(NULL," ")) {
				g = (GSList *) g_hash_table_lookup(word_hash,p);
				if (line_list) {
					aux = g_slist_intersection(line_list,g);
					g_slist_free(line_list);
					line_list=aux;
				} else
					line_list = g_slist_intersection(l,g);
			}
		
                        for (l=line_list; l; l=l->next)
                                fprintf(fresults,"A%d_B%d\n",GPOINTER_TO_INT(l->data),line);

                        g_slist_free(line_list);
		}

		line++;
	}

	g_free(line_buffer);
	fclose(fd);
	fclose(fresults);
}

frases::~frases() {
	g_hash_table_foreach(word_hash,free_list,NULL);
	g_hash_table_destroy(word_hash);
	g_free(results);
}


void frases::result() {
	char buffer[BUFFER_SIZE];
	fstream f(results);
	
	while (f) {
		f.read(buffer,BUFFER_SIZE);
		cout.write(buffer,f.gcount());
	}
	f.close();
}

void frases::salida(char * filename) {
	char buffer[BUFFER_SIZE];
	ifstream f(results);
	ofstream g(filename);

	while (f) {
		f.read(buffer,BUFFER_SIZE);
		g.write(buffer,f.gcount());
	}
	f.close();
	g.close();
}

int main() {
	string in_file,out_file;
	ofstream ferr("incidentes.log");
	frases *phrases;

	cin >>in_file >>out_file;

	try {
		phrases = new frases(in_file.c_str(),out_file.c_str());
	
		//phrases->result();
		//phrases->salida("pitotiatin.txt");
		delete phrases;
	} catch(GString *msg) {
		ferr <<msg->str <<endl;	
	}
}
