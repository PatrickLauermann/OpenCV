Opencv_annotations:

  A ferramenta opencv_annotations é muito útil para ajudá-lo a capturar todas as coordenadas retangulares de todas as amostras positivas que você gostaria de usar no treinamento em cascata. A coordenada do retângulo significa (x, y, w, h). O programa irá gerar um arquivo de texto que contém o caminho do arquivo para a imagem positiva. É chamado de opencv_annotations, porque descreve algumas informações sobre cada imagem positiva em suas amostras positivas. 
  
  O programa será executado e tentará abrir todos os arquivos do diretório ./images. Se encontrar qualquer coisa que não seja uma imagem, ele passará por uma exceção e será encerrado. Se houver uma imagem corrompida, ela será encerrada. 

Opencv_createsamples:  

  Cria amostras positivas uma coleção de imagens positivas. O esquema de criação de amostras de teste é semelhante à criação de amostras de treinamento, pois cada amostra de teste é uma imagem de fundo em que uma imagem distorcida e dimensionada aleatoriamente instância da imagem do objeto é colada em uma posição aleatória.
  
  Para criar amostras de treinamento de uma imagem aplicando distorções e mostrar os resultados:
opencv_createsamples  -img  source.png  -num  10  -bg  negatives.dat  -vec  samples_out.vec -show Para criar amostras de treinamento de tamanho 40 x 40 a partir de algumas imagens sem aplicar distorções: opencv_creasamples  -info  source.dat  -vec  samples_out.vec  -w  40  -H  40

Opencv_traincascade:

  O Opencv_traincascade é um novo programa escrito em C ++ usando a API OpenCV 2.x. A principal vantagem é que oferece suporte aos recursos Haar e LBP (Padrões binários locais) e é fácil adicionar outros recursos. Comparado com o recurso Haar, o recurso LBP é um recurso inteiro, então o processo de treinamento e detecção é várias vezes mais rápido do que o recurso Haar. 
  
  A precisão dos recursos LBP e Haar para detecção depende da qualidade e dos parâmetros de treinamento dos dados de treinamento durante o processo de treinamento. É possível treinar um classificador de LBP com a mesma precisão dos recursos de Haar. Opencv_traincascade pode exportar classificadores em cascata selecionados no formato antigo. No entanto, após o processo de treinamento ser interrompido e reiniciado, não pode carregar um formato de arquivo diferente do anterior à interrupção. 

Tutorial:

  Baixar Python 32bit 
  
  Instalar opencv: pip install opencv_python
  
  Adicionar o caminho na variável de ambiente (C:\Users\ seu users\pasta que descompactou\opencv\build\x64\vc14\bin).
  
  Criar as pastas positivas, negativas e treinamento
  
  Executar o código buildListNegative.py para criar a lista das imagens negativas.
  
  Realizar o código opencv_annotation --annotations=saida.txt --images=positivas/. Para selecionar as imagens positivas.
  
  Inserir o código: opencv_createsamples -info saida.txt -bg negativas.txt -vec vetor.vec -w 24 -h 24 para criar o arquivo de vetor.vec
  
  Executar o código opencv_traincascade -data treinamento -vec vetor.vec -bg negativas.txt -numPos -numNeg -w 24 -h 24 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -numStages   30 -acceptanceRatioBreakValue 1.0e-5
  
  Irá começar o treinamento da IA
  
  Testar a IA com o código analiseTreinamento.py
