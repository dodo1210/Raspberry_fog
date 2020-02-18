# Raspberry Fog

Este projeto tem como objetivo medir o desempenho de uma mini cloud (Fog) com Rapberry e comparar com servidores comuns para verificar a sua viabilidade. Para isso foi realizada o envio de imagens para dar a medição de processamento de cada um dos servidores. Mais detalhes dessa análise de desempenho: http://natal.uern.br/eventos/csbc2018/wp-content/uploads/2018/08/Anais-Final-WPerformance.pdf

Este projeto contém dependência do programa RabbitMQ e das bibliotecas: pika, subprocess, base64, opencv2 e glob.

Este projeto foi desenvolvido em Python e contém três arquivos de execução, são eles: recebe.py, envia.py e niveis_de_cinza2.py

recebe.py: Este arquivo recebe uma imagem, que para convertida em base64 e executa o código níveis_de_cinza2.py, por fim da a resposta de tempo de processamento.<br>
envia.py: Este arquivo converte uma imagem, converte para base64 e envia para o arquivo recebe.py.
níveis_de_cinza_2: Este arquivo é acionado a partir da lib subprocess no arquivo recebe.py. Nele é segmentada uma imagem em níveis de cinza.

A ordem de execução é recebe.py, depois envia.py. O arquivo níveis_de_cinza2.py é acionado pelo recebe.py.
