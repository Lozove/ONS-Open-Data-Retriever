# Código de Recuperação de Dados Abertos do ONS

Este código Python recupera Dados Abertos do ONS (Operador Nacional do Sistema Elétrico) a partir de uma URL para um determinado tipo de dados e intervalo de anos especificados em um arquivo de configuração **.yml**. Os dados recuperados são então salvos em um arquivo CSV em um diretório **data**.

## Pré-requisitos
Este código requer que os seguintes módulos Python estejam instalados:

- os
- logging
- yaml
- pandas

## Uso
Coloque o arquivo de script Python em um diretório desejado.
Crie um arquivo **config.yml** no mesmo diretório que o arquivo de script Python. O arquivo **config.yml** deve especificar os parâmetros **data_names**, **first_year** e **last_year**. **data_names** especifica uma lista de tipos de dados para recuperar, **first_year** especifica o ano inicial do intervalo de dados a serem recuperados e **last_year** especifica o ano final do intervalo de dados a serem recuperados.
Execute o script Python usando um interpretador Python. O script recuperará os dados especificados no arquivo **config.yml** e salvará os dados em um arquivo CSV em um diretório **data**. Um diretório **logs** também será criado para armazenar as informações de registro.

## Descrição do Código
O código começa verificando se existem um diretório **data** e um diretório **logs**. Se eles não existirem, eles são criados usando o módulo **os**.

O código então configura o logger para gravar em um arquivo de log e no console usando o módulo **logging**. O logger é usado para registrar o início e o final do processo de recuperação de dados e para registrar quaisquer erros ou avisos que possam ocorrer durante o processo.

O arquivo de configuração **config.yml** é carregado no código usando o módulo **yaml**.

A função **main** é então chamada, que itera por cada tipo de dados especificado no arquivo de configuração. Para cada tipo de dados, a função **get_ons_data_frames** é chamada para recuperar os data frames para cada ano no intervalo de anos especificado. Os data frames recuperados são concatenados em um único data frame e salvos em um arquivo CSV no diretório **data**.

A função **get_ons_data_frames** recupera os data frames para cada ano no intervalo de anos especificado para um determinado tipo de dados. A função cria uma lista vazia para armazenar os data frames para cada ano e itera por cada ano no intervalo de anos especificado. Para cada ano, a função tenta ler os dados da URL em um data frame usando o módulo **pandas**. Se os dados forem recuperados com sucesso, o data frame é adicionado à lista de data frames para o tipo de dados especificado. Se os dados não estiverem disponíveis para o tipo de dados e ano especificados, um aviso é registrado. A função, em seguida, concatena todos os data frames recuperados em um único data frame e o retorna.

Finalmente, a função **main** é chamada quando o script Python é executado. A condição **if name == 'main'** garante que a função **main** seja chamada somente quando o script Python for executado diretamente e não quando ele for importado como um módulo.
