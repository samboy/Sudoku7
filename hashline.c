/* Donated to the public domain by Sam Trenholme 2019-09-14
 * This program is a program that does a simple MAC
 * Given a hash prefix as its first and only argument (the hashPrefix), it 
 * reads lines from standard input. For each line, it strips any trailing 
 * newline characters from the line, takes the hashPrefix, concatenates a 
 * '|' character, then contactenates the line.  The program then runs
 * a RG32 hash on the combined string, and outputs both the hash and the 
 * line to standard output.  For example:

cat > foo << EOF
line1
line 2
line #3
EOF
cat foo | ./hashline bar
9a96ef0f20ee036b43c96c16f06c4ed45efdf3f44736a6bdd9c6e342b460f099 line1
ef7aa1aae2bb3430bbe7de03702a932c2545ccd07112e067435c69ada9f0524a line 2
0e6ba6e8465ec75f9cc86ed98e62d113be02cfb87f66ff71dc706277f44a6fd8 line #3

 * Note that 9a96ef0f20ee... is the RadioGatun[32] hash of 'bar|line1',
 * ef7aa1aae2bb... the RadioGatun[32] hash of 'bar|line 2', and so on.
 */

#include <stdint.h> 
#define rg uint32_t 
#define rgp(a) for(c=0;c<a;c++)
#define rgn w[c*13]^=s;u[16+c]^=s;
void rgf(rg*a,rg*b){rg m=19,A[45],x,o=13,c,y,r=0;rgp(12)b[c+c%3*o]^=a
[c+1];rgp(m){r=(c+r)&31;y=c*7;x=a[y++%m];x^=a[y%m]|~a[(y+1)%m];A[c]=A
[c+m]=x>>r|x<<(32-r)%32;}for(y=39;y--;b[y+1]=b[y])a[y%m]=A[y]^A[y+1]^
A[y+4];*a^=1;rgp(3)a[c+o]^=b[c*o]=b[c*o+o];}void rgl(rg*u,rg*w,char*v
){rg s,q,c,x;rgp(40)w[c]=u[c%19]=0;for(;;rgf(u,w)){rgp(3){for(s=q=0;q
<4;){x=*v++;s|=(x?255&x:1)<<8*q++;if(!x){rgn;rgp(17)rgf(u,w);return;}
}rgn;}}}rg rgi(rg*m,rg*b,rg*a){if(*a&2)rgf(m,b);return m[*a^=3];}

/* Example of API usage, non-Golfed (also public domain) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc,char **argv){
        uint32_t belt[40], mill[19], c, j, phase = 2;
	char *hashPrefix;
	char line[1200];
	char thisline[1200];
	size_t len;

        if(argc < 2) {
                printf("Usage: hashline hashPrefix\n");
                exit(1);
        }

	hashPrefix = argv[1];

	if(strlen(hashPrefix) > 120) {
		printf("hashPrefix is too long\n");
		exit(1);
	}

	while(!feof(stdin)) {
		if(fgets(line, 800, stdin) == NULL) {
			exit(0);
		}
		len = strlen(line);
		if(len > 0) {
			if(line[len - 1] == '\n') {
				line[len - 1] = 0;
			}
		}
		if(len > 1) {
			if(line[len - 2] == '\r') {
				line[len - 2] = 0;
			}
		}
		strcpy(thisline,hashPrefix);
		strcat(thisline,"|");
		strcat(thisline,line);
		rgl(mill,belt,thisline);
        	for(c = 0; c < 8; c++) {
                	j = rgi(mill, belt, &phase); /* Get number from PRNG */
                	j = (j << 24 |
                     		(j & 0xff00) << 8 |
                     		(j & 0xff0000) >> 8 |
                     		j >> 24);
                	printf("%08x",j);
		}
		printf(" %s",line);
		puts("");
        }
        return 0;
}
