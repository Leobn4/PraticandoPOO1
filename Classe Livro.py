class Livro:
    def __init__(self,titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.pagina_atual = 0

    def abrir_livro(self):
        self.pagina_atual == 1

    def ler_paginas(self):
        self.pagina_atual += 1 
        
    def exibir_progresso(self):
        print((self.pagina_atual / self.numero_paginas) * 100)




L1 = Livro ("It: a Coisa","Stephen King",1104 )

L1.exibir_progresso()

for pagina in range(1, 1105):
    print(f"Lendo página {pagina}")
    L1.ler_paginas ()

L1.exibir_progresso()
