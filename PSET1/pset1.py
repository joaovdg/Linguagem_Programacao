# IDENTIFICAÇÃO DO ESTUDANTE:
# Preencha seus dados e leia a declaração de honestidade abaixo. NÃO APAGUE
# nenhuma linha deste comentário de seu código!
#
#    Nome completo: Joao Lucas Saraiva
#    Matrícula: 202198361
#    Turma: CC3M
#    Email: joaolucassaraivasb@hotamil.com
#
# DECLARAÇÃO DE HONESTIDADE ACADÊMICA:
# Eu afirmo que o código abaixo foi de minha autoria. Também afirmo que não
# pratiquei nenhuma forma de "cola" ou "plágio" na elaboração do programa,
# e que não violei nenhuma das normas de integridade acadêmica da disciplina.
# Estou ciente de que todo código enviado será verificado automaticamente
# contra plágio e que caso eu tenha praticado qualquer atividade proibida
# conforme as normas da disciplina, estou sujeito à penalidades conforme
# definidas pelo professor da disciplina e/ou instituição.
#


# Imports permitidos (não utilize nenhum outro import!):
import sys
import math
import base64
import tkinter
from io import BytesIO
from PIL import Image as PILImage


def fazerKernel(n):
# Cria uma matriz vazia chamada kernel com dimensões 'n' por 'n'

        kernel = [[1/n**2 for index in range(n)]for index in range(n)]
        # 1 - (FOR) Inicia um loop for index in range(n) para percorrer as linhas do kernel.
        # 2 - (FOR) Dentro do loop, inicia outro loop for index in range(n) para percorrer as colunas do kernel.
        # Atribui o valor 1/n**2 a cada elemento do kernel.
        # O valor 1/n**2 é usado para garantir que a soma de todos os elementos do kernel seja igual a 1.
        # Isso é importante para preservar o brilho geral da imagem durante a convolução.
    
        return kernel
        # Retorna a matriz do filtro resultante
        
        # RESUMO DA VARIAVEL
        # Em resumo, a função kernelMaker gera uma matriz de filtro com valores proporcionais a 1/n**2.
        # O parâmetro n determina o tamanho do filtro, ou seja, a dimensão da matriz n por n.
        # A função retorna a matriz do filtro resultante, que pode ser usada para realizar operações de filtragem em imagens,
        # como DESFOQUE, NITIDEZ, REALCE EM BORDAS, entre outros, ou seja todas as operaçãoes do projeto.






# Classe Imagem:
class Imagem:
    def __init__(self, largura, altura, pixels):
        self.largura = largura
        self.altura = altura
        self.pixels = pixels



    def get_pixel(self, x, y):
        # O valor minimo que uma imagem pode ter é = 0 
        # por isso caso o X (largura) for menor que  0
        # a variavel é setada para receber o valor   0
        if x < 0:
           x = 0
        # Após a verificação do tamanho minimo vamos para
        # a condicional para verificação do tamanho maximo
        # caso o X seja maior que a largura da imagem, 
        # o valor de X é setado para o valor da imagem - 1 pixel
        # pois os valores começam a partir de 0 
        elif x >= self.largura:
            x = self.largura - 1


        # Verificação do tamanho minimo da IMG que tem que ser no minimo 0
        # então novamente se o valor de Y for menor que 0 
        # ela é setada com valor 0
        if y<0:
            y = 0

        # A verificação do tamanho maximo também ocorre 
        # e caso o Y seja maior que a altura da foto 
        # o valor de Y é setado para o valor da Imagem - 1 pixel
        elif y>=self.altura:
            y = self.altura - 1

        # O retorno dessa função vai mostrar o valor do PIXEL (cor), que vai estar 
        # dentro das cordenadas de x + (y * largura)
        return self.pixels[(x + y * self.largura)]
        # Exemplo
        # Largura = 5
        # Altura  = 4                             x   y
        # Chamada da função get_pixel nos pixels (2 , 3)
        # Nessa chamada os valores de x e y estão dentro dos limites 
        # a função retorna o valor do pixel na posição (2, (3 * 5) ) = 17 na na lista self.pixels[] 
        # caso o valor de x ou de y seja menor que 0 o valor é setado automaticamente para 0 na função a cima.
    
    #FILTRO ADICIONAL: NORMALIZAÇÂO.
    def padrao_pixel(self):
        for x in range(self.largura):
            for y in range(self.altura):
                padrao_pixel = self.get_pixel(x,y)

                # Se o valor do pixel padrao_pixel for menor que 0, ele é ajustado para 0.
                if  padrao_pixel < 0:
                    padrao_pixel = 0

                # Se o valor do pixel padrao_pixel for maior que 255, ele é ajustado para 255
                # Essas condicionais garantem que os valores dos pixels estejam dentro do intervalo válido.
                elif padrao_pixel > 255:
                    padrao_pixel = 255

                # Como os valores dos piexel devem ser interios, é aplicada a função 'round(padrao_pixel)' 
                # que arredonda o valor para o numero inteiro mais proximo
                padrao_pixel = round(padrao_pixel)
                
                # Por fim, a função set_pixel(x, y, padrao_pixel) é chamada
                # para definir o novo valor ajustado do pixel na posição (x, y) na imagem.
                self.set_pixel(x,y, padrao_pixel) 

                # RESUMO DA VARIAVEL
                # Em resumo, a função padrao_pixel percorre todos os pixels da imagem,
                # ajusta seus valores para garantir que estejam dentro de um intervalo específico
                # e arredonda-os para valores inteiros antes de atualizá-los na imagem.
            
    def set_pixel(self, x, y, c):

        # Recebe os parâmetros 'x, y' que representam as coordenadas do pixel e 'C' é o valor  a ser atribuído a ele, respectivamente.
        self.pixels[(x + y * self.largura)] = c
        # Calcula o índice correspondente na lista de pixels para acessar o pixel desejado. O cálculo é realizado por (x + y * self.largura).
        # A coordenada x determina a posição horizontal do pixel.
        # A coordenada y determina a posição vertical do pixel.
        # 'self.largura' representa a largura da imagem.
        # Multiplicar y por self.largura ajusta a posição vertical na lista de pixels.
        # Atribui o valor c ao pixel na posição calculada. self.pixels é a lista que armazena os valores dos pixels da imagem.
        # O pixel é atualizado com sucesso na lista de pixels.

        # RESUMO DA VARIAVEL
        # Em resumo, a função set_pixel recebe as coordenadas x e y de um pixel e atribui o valor c a esse pixel na lista self.pixels.
        # Isso permite modificar o valor de um pixel específico na imagem.


    def aplicar_por_pixel(self, func):
        # Cria uma nova imagem chamada resultado com as mesmas dimensões (largura e altura) da imagem atual (self).
        resultado = Imagem.nova(self.largura, self.altura)
        # Percorre as posições horizontais (largura) da imagem.
        for x in range(resultado.largura):
            # Percorre as posições verticais (altura) da imagem.
            for y in range(resultado.altura):
                # Dentro dos loops, obtém a cor do pixel na posição (x, y) da imagem atual utilizando a função get_pixel(x, y).
                cor = self.get_pixel(x, y)
                # Aplica a nova cor, na cor antiga do pixel.
                nova_cor = func(cor)
                # Define a nova_cor no pixel correspondente na imagem resultado, invertendo as coordenadas x e y para garantir a correta atribuição na nova imagem.
                resultado.set_pixel(x, y, nova_cor)
                # Correção estava Y e X invertendo a imagem alterado para X e Y.
        return resultado


    def correlacao(self, n):
            
            tamanhoKernel = len(n)
            # Obtém o tamanho do kernel n através do uso da função len(n) 
            # e armazena o valor na variável tamanhoKernel. 
            img = Imagem.nova(self.largura, self.altura)
            # Cria uma nova imagem chamada img
            # Com as mesmas dimensões da imagem atual (self.largura e self.altura).
            for x in range(self.largura):
            # Inicia um loop for x in range(self.largura) para iterar sobre as coordenadas 'X' da imagem
                for y in range(self.altura):
                # Dentro do loop for x, inicia um loop for y in range(self.height) para iterar sobre as coordenadas 'Y' da imagem.
                    somaCorrelacao = 0
                    # Cria uma variável chamada correlationSum e a inicializa como zero.
                    # Essa variável será usada para acumular a soma dos produtos entre os valores do kernel e os valores dos pixels da imagem
                    for z in range(tamanhoKernel):
                    # Inicia um loop for z in range(kernel) para iterar sobre as linhas do kernel.
                        for w in range(tamanhoKernel):
                        # Dentro do loop for z, inicia um loop for w in range(tamanhoKernel) para iterar sobre as colunas do kernel.
                            somaCorrelacao += self.get_pixel((x-(tamanhoKernel//2)+z), (y-(tamanhoKernel//2))+w)*n[z][w]
                            # A linha somaCorrelacao += self.get_pixel((x-(tamanhoKernel//2)+z), (y-(tamanhoKernel//2))+w)*n[z][w] calcula a correlação entre o kernel e a imagem.
                            #  Para cada posição (z, w) do kernel, obtém o valor do pixel correspondente na imagem utilizando a função self.get_pixel,
                            #  multiplica-o pelo valor do kernel em (z, w), e acumula o resultado na variável somaCorrelacao.
                    img.set_pixel(x, y, somaCorrelacao)
                    # Utiliza a função img.set_pixel(x, y, correlationSum) para definir o valor do pixel na posição (x, y) na nova imagem img como o resultado da correlação (correlationSum).
            return img
        # Retorno da nova imagem após a operação de correlação. 
        
        # RESUMO DA VARIAVEL 
        # Em resumo, a função correlacao realiza a correlação entre um kernel n e a imagem atual,
        # acumulando a soma dos produtos entre os valores do kernel e os valores dos pixels da imagem.
        # Isso resulta em uma nova imagem que reflete a aplicação do kernel na imagem original.

    def invertida(self):
        return self.aplicar_por_pixel(lambda c: 255 - c)
        # Correção estava com valor 256, mas o valor é 255, pois é o valor maximo que um pixel pode ter.
        # RESUMO VARIAVEL 
        # A invertida pega o valor 'c' do pixel em cada posição (x, y) e subtrai pelo valor maximomo que o pixel pode ter que seria 255.

        
    def borrada(self, n):
        kernel = self.correlacao(fazerKernel(n))
        # 1 - Chama a função fazerKernel (explicação da variavel linha 30 até 47), onde retorna a matriz da foto.
        # 2 - Chama a função Correlacao (explicação da variavel linha 163 ate 194), onde retorna a soma entre
        # os valores do kernel e os valores dos pixels da imagem, resultando na imagem borrada, e atribuindo essa
        # imagem a variavel "KERNEL".
        kernel.padrao_pixel()
        # Chama a função padrao_pixel (explicação da variavel linha 102 até 127), a variavel serve para garantir que
        # todos os pixels na imagem borrada, estejam com valores validos de 0 até 255.
        return kernel
        # RESUMO DA VARIAVEL
        # Em resumo, a função borrada utiliza um kernel de convolução para realizar um desfoque na imagem.
        # O parâmetro n determina o tamanho do kernel, que afeta o grau de desfoque aplicado. 
        # A função retorna a imagem borrada resultante, na qual os valores dos pixels foram ajustados para se adequarem ao intervalo válido.
    
    def focada(self, n):
        imagemBorrada = self.borrada(n)
        # Chama a função self.borrada(n) para criar uma imagem borrada e armazenar na variavel imagemBorrada.
        img = Imagem.nova(self.largura, self.altura)
        # Cria uma imagem nova com as mesmas dimensoes da imagem original.
        for x in range(self.largura):
        # Inicia um loop for x in range(self.largura) para percorrer as colunas da imagem.
            for y in range(self.altura):
            # Dentro do loop for x, inicia um loop for y in range(self.altura) para percorrer as linhas da imagem.
                formula_foco = round(2*self.get_pixel(x,y)-(imagemBorrada.get_pixel(x,y)))
                # Calcula a fórmula de foco para cada pixel da imagem.
                # A fórmula utiliza o valor do pixel na imagem original, multiplicado por 2, subtraído pelo valor do pixel correspondente na imagem borrada. 
                # A função round é utilizada para arredondar o resultado para o valor inteiro mais próximo.
                img.set_pixel(x, y, formula_foco)
                # Define o valor resultante da fórmula de foco como o pixel correspondente na nova imagem img nas coordenadas (x, y).
        img.padrao_pixel()
        # Chama a função img.padrao_pixel() para garantir que os valores dos pixels na nova imagem estejam dentro do intervalo válido, entre 0 e 255.
        return img
        # Retorna a nova imagem img com o efeito de foco aplicado.

        # RESUMO VARIAVEL
        # Em resumo, a função focada aplica um efeito de foco em uma imagem utilizando um filtro de realce.
        # O parâmetro n determina o tamanho do filtro de média usado para criar a imagem borrada. 
        # A função retorna uma nova imagem com o efeito de foco aplicado, na qual os valores dos pixels foram ajustados para se adequarem ao intervalo válido.


    def bordas(self):
        img = Imagem.nova(self.largura, self.altura)
        # 1 - Cria uma nova imagem img com as mesmas dimensões (largura e altura) da imagem original.
        # 2 - Define dois kernels de convolução:
        # 3 - kernelSobelX para detecção de bordas horizontais 
        kernelSobelX = [[1, 0, -1],
                        [2, 0, -2],
                        [1, 0, -1]]
        
        # 4 - kernelSobelY para detecção de bordas verticais.
        kernelSobelY = [[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]]

        SobelXAplicado = self.correlacao(kernelSobelX)
        # Aplica a convolução da imagem original com o kernel kernelSobelY, utilizando a função self.correlacao, e armazena o resultado na variável SobelYAplicado.
        SobelYAplicado = self.correlacao(kernelSobelY)
        # Aplica a convolução da imagem original com o kernel kernelSobelY, utilizando a função self.correlacao, e armazena o resultado na variável SobelYAplicado


        for x in range(self.largura):
        # Inicia um loop for x in range(self.width) para percorrer as colunas da imagem.
            for y in range(self.altura):
            # Dentro do loop for x, inicia um loop for y in range(self.height) para percorrer as linhas da imagem.
                operacao_Sobel = round(math.sqrt(SobelXAplicado.get_pixel(x,y)**2 + SobelYAplicado.get_pixel(x,y)**2))
                # Calcula a operação de Sobel para cada pixel da imagem, que é a raiz quadrada da soma dos quadrados das respostas do operador de Sobel em cada direção. 
                # Utiliza a função math.sqrt para calcular a raiz quadrada.
                img.set_pixel(x, y, operacao_Sobel)
                # Define o valor resultante da operação de Sobel como o pixel correspondente na nova imagem img nas coordenadas (x, y).
        img.padrao_pixel()
        # Chama a função img.padrao_pixel() para normalizar os valores dos pixels na nova imagem, garantindo que estejam dentro do intervalo válido, geralmente entre 0 e 255.
        return img
        # Retorna a nova imagem img com as bordas detectadas.
        # RESUMO VARIAVEL
        # Em resumo, a função bordas aplica o operador de Sobel para detectar bordas em uma imagem. 
        # Utiliza dois kernels de convolução, um para bordas horizontais e outro para bordas verticais.
        # A função retorna uma nova imagem com as bordas detectadas, onde os valores dos pixels foram normalizados para se adequarem ao intervalo válido.

    # Abaixo deste ponto estão utilitários para carregar, salvar e mostrar
    # as imagens, bem como para a realização de testes.

    def __eq__(self, other):
        return all(getattr(self, i) == getattr(other, i)
                   for i in ('altura', 'largura', 'pixels'))

    def __repr__(self):
        return "Imagem(%s, %s, %s)" % (self.largura, self.altura, self.pixels)

    @classmethod
    def carregar(cls, nome_arquivo):
        """
        Carrega uma imagem do arquivo fornecido e retorna uma instância dessa
        classe representando essa imagem. Também realiza a conversão para tons
        de cinza.

        Invocado como, por exemplo:
           i = Imagem.carregar('test_images/cat.png')
        """
        with open(nome_arquivo, 'rb') as guia_para_imagem:
            img = PILImage.open(guia_para_imagem)
            img_data = img.getdata()
            if img.mode.startswith('RGB'):
                pixels = [round(.299 * p[0] + .587 * p[1] + .114 * p[2]) for p in img_data]
            elif img.mode == 'LA':
                pixels = [p[0] for p in img_data]
            elif img.mode == 'L':
                pixels = list(img_data)
            else:
                raise ValueError('Modo de imagem não suportado: %r' % img.mode)
            l, a = img.size
            return cls(l, a, pixels)

    @classmethod
    def nova(cls, largura, altura):
        """
        Cria imagens em branco (tudo 0) com a altura e largura fornecidas.

        Invocado como, por exemplo:
            i = Imagem.nova(640, 480)
        """
        return cls(largura, altura, [0 for i in range(largura * altura)])

    def salvar(self, nome_arquivo, modo='PNG'):
        """
        Salva a imagem fornecida no disco ou em um objeto semelhante a um arquivo.
        Se o nome_arquivo for fornecido como uma string, o tipo de arquivo será
        inferido a partir do nome fornecido. Se nome_arquivo for fornecido como
        um objeto semelhante a um arquivo, o tipo de arquivo será determinado
        pelo parâmetro 'modo'.
        """
        saida = PILImage.new(mode='L', size=(self.largura, self.altura))
        saida.putdata(self.pixels)
        if isinstance(nome_arquivo, str):
            saida.save(nome_arquivo)
        else:
            saida.save(nome_arquivo, modo)
        saida.close()

    def gif_data(self):
        """
        Retorna uma string codificada em base 64, contendo a imagem
        fornecida, como uma imagem GIF.

        Função utilitária para tornar show_image um pouco mais limpo.
        """
        buffer = BytesIO()
        self.salvar(buffer, modo='GIF')
        return base64.b64encode(buffer.getvalue())

    def mostrar(self):
        """
        Mostra uma imagem em uma nova janela Tk.
        """
        global WINDOWS_OPENED
        if tk_root is None:
            # Se Tk não foi inicializado corretamente, não faz mais nada.
            return
        WINDOWS_OPENED = True
        toplevel = tkinter.Toplevel()
        # O highlightthickness=0 é um hack para evitar que o redimensionamento da janela
        # dispare outro evento de redimensionamento (causando um loop infinito de
        # redimensionamento). Para maiores informações, ver:
        # https://stackoverflow.com/questions/22838255/tkinter-canvas-resizing-automatically
        tela = tkinter.Canvas(toplevel, height=self.altura,
                              width=self.largura, highlightthickness=0)
        tela.pack()
        tela.img = tkinter.PhotoImage(data=self.gif_data())
        tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        def ao_redimensionar(event):
            # Lida com o redimensionamento da imagem quando a tela é redimensionada.
            # O procedimento é:
            #  * converter para uma imagem PIL
            #  * redimensionar aquela imagem
            #  * obter os dados GIF codificados em base 64 (base64-encoded GIF data)
            #    a partir da imagem redimensionada
            #  * colocar isso em um label tkinter
            #  * mostrar a imagem na tela
            nova_imagem = PILImage.new(mode='L', size=(self.largura, self.altura))
            nova_imagem.putdata(self.pixels)
            nova_imagem = nova_imagem.resize((event.largura, event.altura), PILImage.NEAREST)
            buffer = BytesIO()
            nova_imagem.save(buffer, 'GIF')
            tela.img = tkinter.PhotoImage(data=base64.b64encode(buffer.getvalue()))
            tela.configure(height=event.altura, width=event.largura)
            tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        # Por fim, faz o bind da função para que ela seja chamada quando a tela
        # for redimensionada:
        tela.bind('<Configure>', ao_redimensionar)
        toplevel.bind('<Configure>', lambda e: tela.configure(height=e.altura, width=e.largura))

        # Quando a tela é fechada, o programa deve parar
        toplevel.protocol('WM_DELETE_WINDOW', tk_root.destroy)


# Não altere o comentário abaixo:
# noinspection PyBroadException
try:
    tk_root = tkinter.Tk()
    tk_root.withdraw()
    tcl = tkinter.Tcl()


    def refaz_apos():
        tcl.after(500, refaz_apos)


    tcl.after(500, refaz_apos)
except:
    tk_root = None

WINDOWS_OPENED = False

if __name__ == '__main__':
    # O código neste bloco só será executado quando você executar
    # explicitamente seu script e não quando os testes estiverem
    # sendo executados. Este é um bom lugar para gerar imagens, etc.
    im = Imagem.carregar(r'test_images\bluegill.png')
    im_invertida = im.invertida()
    


    # QUESTAO 2:
    peixe = Imagem.carregar(r'C:\Users\joao.saraiva\Desktop\pset1\test_images\bluegill.png') # Chamando a img e colocando na variavem
    peixe_invertido = peixe.invertida() ## Igualando outra variavel para receber o valor invertido da imagem chamada anteriormente
    Imagem.salvar(peixe_invertido, 'Respostas\peixe.png') ### Salvando a imagem no Repositorio


     # QUESTAO 4:
    kernel = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [1, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    porco = Imagem.carregar('test_images/pigbird.png')
    porco_correlacao = porco.correlacao(kernel)
    Imagem.salvar(porco_correlacao, 'Respostas/porco_e_passarinho.png')

    
    # SESSAO 5.1  EXERCICIO DO GATINHO
    gatinho = Imagem.carregar('test_images/cat.png')
    gato_borrado = gatinho.borrada(5)
    Imagem.salvar(gato_borrado,'Respostas/gato.png')



    # QUESTAO 5
    cobra = Imagem.carregar('test_images/python.png')
    cobra_focada = cobra.focada(11)
    Imagem.salvar(cobra_focada,'Respostas/cobra.png')

    
    
    
    #QUESTÃO 6
    #RESULTADOS INDIVIDUAIS DA APLICAÇÃO DOS KERNELS DA OPERAÇÃO DE SOBEL 

    kernelSobelX = [[1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]]

    kernelSobelY = [[1,   2,  1],
                    [0,   0,  0],
                    [-1, -2, -1]]

    construcao = Imagem.carregar('test_images/construct.png')
    construcaoSobelX = construcao.correlacao(kernelSobelX)
    Imagem.salvar(construcaoSobelX, 'Respostas/construcaoSobelX.png')

    construcaoSobelY = construcao.correlacao(kernelSobelY)
    Imagem.salvar(construcaoSobelY, 'Respostas/construcaoSobelY.png')

    Bordas_Construcao = construcao.bordas()
    Imagem.salvar(Bordas_Construcao, 'Respostas/construcao_bordas.png')
    
    
    
    pass

    peixe_invertido.mostrar()
    gato_borrado.mostrar()
    porco_correlacao.mostrar()
    cobra_focada.mostrar()
    Bordas_Construcao.mostrar()
    
    
  
    # O código a seguir fará com que as janelas de Imagem.mostrar
    # sejam exibidas corretamente, quer estejamos executando
    # interativamente ou não:
    if WINDOWS_OPENED and not sys.flags.interactive:
        tk_root.mainloop()