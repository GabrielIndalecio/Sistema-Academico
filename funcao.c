#include <string.h>
#include <stdio.h>

int verificar_login(const char* usuario, const char* senha) {
    FILE* arquivo = fopen("usuarios.txt", "r");
    if (!arquivo) return 0;

    char linha[100];
    while (fgets(linha, sizeof(linha), arquivo)) {
        char u[50], s[50];
        sscanf(linha, "%s %s", u, s);
        if (strcmp(usuario, u) == 0 && strcmp(senha, s) == 0) {
            fclose(arquivo);
            return 1;
        }
    }

    fclose(arquivo);
    return 0;
}


int cadastro_usuario(const char* usuario, const char* senha) {
    FILE* arquivo = fopen("usuarios.txt", "a+");
    if (!arquivo) return 0;

    char linha[100];
    char u[50], s[50];

    
    while (fgets(linha, sizeof(linha), arquivo)) {
        sscanf(linha, "%s %s", u, s);
        if (strcmp(usuario, u) == 0) {
            fclose(arquivo);
            return 0; 
        }
    }

    
    fprintf(arquivo, "%s %s\n", usuario, senha);
    fclose(arquivo);
    return 1;
}