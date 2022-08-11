#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{
    int i, j, l, num;
    char tx_text[] = "Hello World!";
    char *rx_bin, *rx_text;

    l = strlen(tx_text);
    rx_bin = malloc(8 * l * sizeof(char));
    rx_text = malloc(l * sizeof(char));

    printf("%s\n", tx_text);

    // for checking
    // printf("%d\n", c[1]);

    // string to binary sequence
    for (i = 0; i < l; i++)
    {
        for (j = 7, num = 0; j >= 0; j--)
        {
            rx_bin[8 * i + 7 - j] = (tx_text[i] & (1 << j)) ? '1' : '0';
            // turn every 8 bits into an integer
            num += (rx_bin[8 * i + 7 - j] == '0' ? 0 : pow(2, j));
            putchar(rx_bin[8 * i + 7 - j]);
            // putchar((tx_text[i] & (1 << j)) ? '1' : '0');
        }
        // automatically converts an integer to a character due to data type conversion
        rx_text[i] = num;
        putchar(' ');
    }
    putchar('\n');
    printf("%s\n", rx_text);

    free(rx_bin);
    free(rx_text);
    return 0;
}