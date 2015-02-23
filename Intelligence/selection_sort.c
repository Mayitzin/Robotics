/**
 *  Selection Sort
 *  -----------
 *  Using Standard C99.
 *  Shows every sorting cycle.
 *  Hints:
 *  - ASCII characters from 'A' to 'Z' span from 65 to 90.
 *  See:
 *  [1] http://www.algolist.net/Algorithms/Sorting/Bubble_sort
 *  [2] https://www.youtube.com/watch?v=Cq7SMsQBEUw
 *
 *  History:
 *      04.02.2015. First implementation.
 *      05.02.2015. Chaged 'for' loop to 'while' condition.
 *  
 *  @author: Mario Garcia
 *  www.mayitzin.com
 */

#include <stdio.h>

void SelectionSort(int a[], int array_size)
{
     int i;
     for (i = 0; i < array_size - 1; ++i)
     {
          int j, min, temp;
          min = i;
          for (j = i+1; j < array_size; ++j)
          {
               if (a[j] < a[min])
                    min = j;
          }

          temp = a[i];
          a[i] = a[min];
          a[min] = temp;
     }
}