# Acessar VM Pela Oracle Cloud

- Criar conta de estudante através do link que o professor gerou e enviou no e-mail.
- Gerar uma nova VM na Oracle Cloud:
  - Configurações da VM:
    - 8GB de RAM na opção de forma.
    - Sistema operacional: Ubuntu 24.
  - **IMPORTANTE:** Baixar as chaves **privada** e **pública** antes de iniciar.
- Executar a VM gerada.
- Após iniciar, executar o seguinte comando no PowerShell, substituindo pelo local da chave privada e IP da VM:

  ```bash
  ssh -i "C:\Users\1001c\Downloads\private.key" ubuntu@152.67.52.157
  ```

- Executar comandos do Linux para atualização:

  ```bash
  sudo apt update
  sudo apt update -y
  ```

- Criar o **Portainer** conforme tutorial do professor.
- No Portainer (`http://p.carla.autom.my`):
  - Abrir o Docker.
  - Adicionar os arquivos do **Postgres** (arquivos 3 e 4).
  - Fazer o deploy.

- Gerar arquivos do **n8n**.
  - Após editar com a URL gerada do `auto.my`, criar a conta no n8n.
  - Acesse: [`https://auto.carla.autom.my`](https://auto.carla.autom.my)
