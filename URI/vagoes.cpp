//URI 1162 train swapping
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int train[50];
int c;


int main() {
	int	n, l, temp;
	
	scanf("%d",&n);
	for (int j=0; j<n; j++) {
		scanf("%d",&l);
		c = 0;
		for (int i=0; i<l; i++) {
			scanf("%d",&train[i]);		
		}
		
		for (int i=0; i<l-1; i++) {
			for (int k=i+1; k<l; k++) {
				if (train[i]>train[k]) {
					temp = train[i];
					train[i] = train[k];
					train[k] = temp;
					c++;
				}
			}
		}
		
		printf("Optimal train swapping takes %d swaps.\n",c);
	}
	return 0;
}