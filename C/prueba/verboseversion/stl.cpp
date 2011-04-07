#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>
#include <map>

using namespace std;

#define MAX_LINE_SIZE 1000

int main(int argc, char* argv[])
{
	int opt;
	int verbose=0;
	int line=1;
	char line_buffer[MAX_LINE_SIZE];
	string lineb;

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

	ifstream file(argv[optind]);
	map<string, int> lines_map;

	string sep("##########");

	while (file) {
		file.getline(line_buffer,MAX_LINE_SIZE);
		lineb=line_buffer;
		if (lineb == sep) {			
			if (verbose)
				cout <<"Finished\n";
			break;
		}

		lines_map[line_buffer] = line++;

		if (verbose)
			cout <<"Added [" <<line <<"," <<lineb <<"]\n";
	}

	while (file) {
		file.getline(line_buffer,MAX_LINE_SIZE);
		lineb=line_buffer;
		if (verbose)
			cout <<"Testing " <<lineb <<endl;

		if (lines_map[lineb])
			cout <<"Match at line " <<line <<" previosly found on ["
				<<lines_map[lineb] <<"," <<lineb <<"]\n";
		
		line++;
	}
}
