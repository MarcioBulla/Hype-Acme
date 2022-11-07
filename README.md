# Hype-Acme
Código Fonte para soluções dos problemas indicados pelo PS na Hype.

> O Documento `solution.ipynb` contem todos as respostas.

> NOTA: todos manuseio de `TABLES` foram feitos através da linguagem SQL, seguindo orientação das questões!. Utilizei o ambiente Jupyter apenas para uma melhor aprestação dos dados.



# Recomendações
- docker compose
- Python 3.10;
- Instalar bibliotecas necessárias em `requirements.txt`;
- Utilize ambiente virtual `virtualenv`.

## Instruções
Testar aplicação

### Execução do docker compose
Primeiro deve construir o container com os `DATABASES` e `TABLES`. Para isso usaremos o `docker compose`:

```bash
docker compose up -d
```
ou
```bash
docker-compose up -d
```
Ele criara 2 container um `MySQL:latest` e outro `Python:3.10`. O container de Python irá baixar e imputar os dados no container `MySQL`, para que possamos utiliza-las em nossas analises.
### Linux
Com os contêiner iniciados podemos acessar o container do `MySQL` para fazer nossas analises.

- Instale o `virtualenv`;
    ```bash
    pip install virtualenv
    ```
- Crie um ambiente virtual;
    ```bash
    virtualenv -p python3.10 Hype 
    ```
- Ative o ambiente virtual;
    ```bash
    source Hype/bin/activate
    ```
- Instale requirimentos do repositório
    ```bash
    pip install -r path/to/requirements.txt
    ```
- Adicionar ambiente no Jupyter,
    ```bash
    python -m ipykernel install --user --name=Hype
    ```
- Verifique que a presença do kernel no jupyter
    ```bash
    jupyter-kernelspec list
    ```
    deve aparecer o kernel que foi criou.