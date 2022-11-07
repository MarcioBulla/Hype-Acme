# Hype-Acme
Codigo Fonte para soluções dos problemas indicados pelo PS na Hype.

# Recomendações
- Python 3.10;
- Instalar bibliotecas necessárias em `requirements.txt`;
- Utilize ambiente virtual `vitualenv`.

## Instruções
Tutorial para preparar o ambiente e executar os notebooks.

### Linux
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
    deve aparecer o kernel que criou.