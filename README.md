# WhatsApp Web Automation with Selenium

Automação robusta para envio de mensagens em grupos do WhatsApp Web utilizando Selenium e ChromeDriver. Este projeto é ideal para enviar lembretes, comunicados ou notificações recorrentes automaticamente. O script é configurado para ser executado automaticamente na data prevista utilizando o agendador de tarefas do sistema operacional (como o Task Scheduler no Windows ou cron no Linux), garantindo que o processo ocorra de forma totalmente automática, sem qualquer intervenção manual por parte do usuário.

---

## Sobre o projeto

Este projeto foi criado para agilizar e otimizar o processo de atualização dos horários de disponibilidade dos membros da ONG **Escrevendo na Quebrada**. Através da automação, ao final de cada mês, o script envia automaticamente uma mensagem para o grupo de tecnologia do WhatsApp, lembrando os membros de atualizarem seus horários para o mês seguinte. Isso evita esquecimentos e reduz a sobrecarga dos coordenadores na organização das agendas, promovendo maior eficiência e comunicação dentro da equipe.

Como evolução, há planos para um sistema complementar que será executado no primeiro dia do mês seguinte. Esse sistema irá processar os horários mais selecionados pelos membros em cada semana, agendar automaticamente as reuniões semanais de metodologia ágil no Google Calendar do setor de tecnologia, e enviar uma mensagem no grupo informando as datas e horários dessas reuniões no início do mês. Todo o fluxo será automatizado, eliminando a necessidade de intervenção manual por parte da coordenação e garantindo maior organização e transparência.

---

## Funcionalidades

- Abre o WhatsApp Web utilizando um perfil de usuário do Chrome já logado.
- Aguarda o carregamento completo da interface, garantindo que o login foi efetuado corretamente.
- Pesquisa por um grupo específico no WhatsApp baseado no nome configurado.
- Envia uma mensagem personalizada e formatada para o grupo.
- Fecha o navegador automaticamente após o envio da mensagem.
- Compatível com execução automática via agendador de tarefas do sistema operacional.
- Logs básicos no console para acompanhar o progresso e erros.

---

## Pré-requisitos

- Python 3.7 ou superior instalado no sistema.
- Google Chrome instalado na versão compatível com o ChromeDriver.
- ChromeDriver na versão exata do seu Google Chrome ([download oficial](https://sites.google.com/chromium.org/driver/)) configurado no PATH do sistema ou na mesma pasta do script.
- Biblioteca Selenium instalada via pip:

  ```bash
  pip install selenium

---

## Configuração

### Configurar perfil do Chrome

Para evitar que seja necessário escanear o QR code a cada execução, é recomendado criar um perfil dedicado no Chrome ou utilizar um perfil já existente que esteja logado no WhatsApp Web. No código, configure o caminho desse perfil na linha abaixo (é necessário editar):

```python
options.add_argument(r"user-data-dir=C:\Users\SeuUsuario\AppData\Local\Google\Chrome\User Data\SEU PERFIL AQUI")
```

---

### Editar grupo e mensagem
No script, personalize as variáveis grupo e mensagem com o nome do grupo do WhatsApp e a mensagem que deseja enviar automaticamente. Exemplo:

```python
grupo = "SEU GRUPO OU CONTATO AQUI"
mensagem = """SUA MENSAGEM AQUI \n\n Link da planilha: SEU LINK AQUI"""
```

---

### Agendamento da execução automática

Configure o agendador de tarefas do seu sistema operacional para executar o script na data desejada (por exemplo, no último dia útil do mês). No Windows, isso pode ser feito via Task Scheduler, criando uma tarefa que execute:

```bash
python caminho\para\seu\script.py
```

Dessa forma, o envio ocorrerá automaticamente sem intervenção manual.

---

### Uso
- Clone este repositório ou baixe o script.
- Configure o perfil do Chrome e personalize a mensagem conforme explicado acima.
- Certifique-se de que o ChromeDriver esteja corretamente instalado e configurado.
- Teste o script executando manualmente para garantir que tudo funciona:

```bash
python enviar_mensagem_whatsapp.py
```

- Configure o agendador de tarefas para execução automática conforme necessidade.

---

### Boas práticas e cuidados

- Perfil Chrome dedicado: Use um perfil exclusivo para essa automação para evitar interferências com seu navegador principal.
- Respeito às políticas do WhatsApp: Evite envio massivo de mensagens para não ser bloqueado pelo WhatsApp.
- Ambiente seguro: Nunca compartilhe seus dados pessoais ou do perfil de usuário.
- Monitoramento: Verifique os logs do script para garantir que as execuções estejam ocorrendo corretamente.
