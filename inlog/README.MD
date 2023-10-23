#### Coleta Domiciliar no Município de Fortaleza
<b>Versão:</b> v1.0
<br><b>Autor:</b> Pedro Florencio
<br><b>Contato:</b> <i>pedro.almeida@iplanfor.fortaleza.ce.gov.br</i>

---

<b>Sobre:</b> Este repositório apresenta o tratamento dos dados de coleta domiciliar extraídos do sistema INLOG, gerenciado pela Marquise Ambiental e de uso da Secretaria de Conservação de Serviços Públicos (SCSP).

<b>Organização:</b> (em desenvolvimento)

<b>Funcionalidades:</b>

- process-setorizacao.py: (em desenvolvimento)
- 20231022_ColetaDomiciliarSetores.ipynb: (em desenvolvimento)
<b>Instruções:</b>
<br> nome_arquivo_entrada.csv process-setorizacao.py nome_arquivo_saida

<b>Novidades da v1.1:</b>

- Extração automática dos dados no sistemas INLOG, aplicando-se Prefect para orquestração dos dados;
- Uso da arquitetura Delta Lake;
- Upload em data warehouse PostgreSQL.