#include <glib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

gpointer where;

gpointer hilo(gpointer data) {
	int a;
	int id=GPOINTER_TO_INT(data);
	//char g[1024*1024*10];
	int *g;

	g_message("Hilo %d - Stack %p - %p",id,&a,&g);
	g_message("Hilo %d - Where %p (%d)",id,where,*(int *)(where-80));
	g=(int *)(where-80);
	g=9;
	sleep(30);
	return NULL;
}

int main(void) {
	int var=42;
	GThread *hilo1,*hilo2;
	GThread *hilo3,*hilo4;
	GThread *hilo5,*hilo6;
	GThread *hilo7,*hilo8;


	if (!g_thread_supported ()) 
		g_thread_init (NULL);

	where = &var;

	hilo1 = g_thread_create(hilo,GINT_TO_POINTER(1),TRUE,NULL);
	hilo2 = g_thread_create(hilo,GINT_TO_POINTER(2),TRUE,NULL);
	hilo3 = g_thread_create(hilo,GINT_TO_POINTER(3),TRUE,NULL);
	hilo4 = g_thread_create(hilo,GINT_TO_POINTER(4),TRUE,NULL);
	hilo5 = g_thread_create(hilo,GINT_TO_POINTER(5),TRUE,NULL);
	hilo6 = g_thread_create(hilo,GINT_TO_POINTER(6),TRUE,NULL);

	g_message("Main:   %p",main);
	g_message("Heap:   %p",malloc(9));
	g_message("malloc: %p",malloc);
	g_message("read:   %p",open);
	g_message("Stack:  %p",&var);

	sleep(2);
	return 0;
}
