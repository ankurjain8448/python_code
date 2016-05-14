#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <ctype.h>

using namespace std;

int main()
{
	//freopen("A-large-practice.in", "r", stdin);
	//freopen("A-small-practice.in", "r", stdin);
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int n;
	scanf("%d", &n);
	while(n--)
	{
		char regex[100], expression[100], c, temp;
		scanf("%s", regex);
		scanf("%s", expression);
		int i =0 ,j = 0,flag = 1;
		while(regex[i] != '\0' && flag == 1)
		{
			c = regex[i];
			switch(c)
			{
			case '^': 
				i += 1;
				break;
			case '$':
				i += 1;
				break;
			case '*':
				temp = regex[i-1];
				if(temp == '.')
					temp = expression[j-1];
				while(temp == expression[j])
					j += 1;
				i += 1;
				break;
			case '.':
				if(isalpha(expression[j]))
				{
					j += 1;
					i += 1;
				}
				else
					flag = 0;
				break;
			default:
				if(regex[i] == expression[j])
				{
					i += 1;
					j += 1;
				}
				else
					flag = 0;
			}
		}

		if(flag == 0)
			printf("false\n");
		else if(regex[i] == '\0' ^ expression[j] == '\0')
			printf("false\n");
		else
			printf("true\n");
	}


	return 0;
}