# ProjetoFinalPPI
Esse Projeto visa aplicar em prática todo o conhecimento atingido em sala de aula (msm q talvez não sejamos um bom exemplo de alunos kkkkk)

O onuarte é uma rede social pensada para abranger a comunidade artistica do IFRN campus Pau dos Ferros.

Para Inicializar o projeto, crie um ambiente virtual:
>python -m venv nome_do_ambiente_virtual

Em seguida inicialize:
no Windows:
>nome_do_ambiente_virtual\Scripts\activate

No Unix ou no MacOS, executa:
>source nome_do_ambiente_virtual/bin/activate

O proximo comando é para instalar as dependencias:
>pip install -r requiriments.txt

Espere o fim do download, execute os proximos comandos para migração na exata ordem:
>python manage.py makemigrations
>python manage.py migrate

Por fim, execute com:
>python manage.py runserver
