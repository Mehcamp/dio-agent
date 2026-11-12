# DIO Security Analyst

> Evolução do DIO Agent — especialização em Cybersecurity e Application Security.

O **DIO Security Analyst** é uma especialização do **DIO Agent**, um agente de IA que acompanha estudantes da DIO. Enquanto o DIO Agent original atua como mentora de estudos, o DIO Security Analyst atua como analista de segurança: ele ensina o estudante a pensar em segurança, a revisar código e configurações, a classificar riscos com base em evidências e a produzir relatórios técnicos com correções e validação.

Esta documentação descreve a especialização, sua motivação, funcionalidades, artefatos, fluxo de análise, demonstração prática, como executá-la, os cenários de avaliação, as decisões de projeto e suas limitações.

---

## 1. Apresentação

O **DIO Security Analyst** é uma evolução do DIO Agent. O projeto original foi concebido para acompanhar estudantes da DIO em suas jornadas de aprendizado tecnológico, com habilidades (skills) que ajudam a planejar estudos, destravar desafios, explicar conceitos, pesquisar na web, revisar portfólio e escolher a carreira. A especialização de segurança segue a mesma proposta de mentoria, aplicada a um domínio de alto impacto: a segurança da informação.

A especialização abrange duas vertentes da aplicação da segurança:

- **Cybersecurity** — segurança de sistemas, rede e infraestrutura, com atenção a servidores expostos, máquinas, configurações e resposta a incidentes.
- **Application Security** — segurança de aplicações, com atenção a código, APIs, banco de dados, autenticação, autorização e boas práticas de desenvolvimento seguro.

**Motivação:** a segurança não pode ser um adendo no final do processo de aprendizado. O estudante precisa praticar a leitura de código com olhar crítico, validar descobertas com evidências e comunicar riscos de forma clara e priorizada. O DIO Security Analyst foi criado para proporcionar exatamente isso: uma especialização que transforma o agente em um mentor de segurança, capaz de produzir análises técnicas estruturadas, com relatórios que diferencia risco real de recomendação genérica de boas práticas.

A personalidade do agente é definida em `agent/persona.md`, a base de conhecimento de segurança em `agent/knowledge/security-basics.md` e o método de análise na skill `Análise de vulnerabilidades` (`skills/vulnerability-analysis/`).

---

## 2. Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| **Análise de vulnerabilidades** | Identifica falhas em código-fonte, configurações e infraestrutura (SQL Injection, XSS, exposição de credenciais, autenticação inadequada, controle de acesso, configuração insegura, componentes desatualizados). |
| **Identificação de SQL Injection e outras falhas** | Localiza o padrão de injeção e demais falhas da OWASP Top 10, mapeando identificadores de segurança (CWE) e contextos de exploração. |
| **Classificação de riscos** | Classifica cada descoberta com severidade (informativa, baixa, média, alta, crítica) e estimativa de probabilidade de exploração, justificadas por contexto. |
| **Recomendações de correção** | Entrega correções imediatas e melhorias de longo prazo, sempre com a correção mais simples que elimina o risco sem sacrificar funcionalidade. |
| **Relatórios técnicos** | Produção de relatórios estruturados com resumo executivo, evidências, causa técnica, impacto, probabilidade, severidade, CWE, CVSS, MITRE ATT&CK, correção e validação. |
| **Análise contextual de cenários de segurança** | Aplica a análise a cenários reais: logs, respostas de erro, configurações de servidor, enunciados de infraestrutura e sistemas expostos. |
| **Orientação defensiva e ética** | Exige autorização e escopo antes de qualquer recomendação; atua exclusivamente em ambientes autorizados, com ênfase em análise estática e verificações não destrutivas. |

---

## 3. Arquivos criados e modificados

A especialização é composta pelos arquivos abaixo. Organizados por personalidade, conhecimento, skills e configuração do agente, indicando se foram criados ou modificados nesta especialização.

### Configuração do agente

| Arquivo | Status | Finalidade |
|---|---|---|
| `AGENTS.md` | Modificado | Registra a skill `Análise de vulnerabilidades` na tabela de skills do agente, ensinando ao harness quando aplicá-la. |

### Personalidade

| Arquivo | Status | Finalidade |
|---|---|---|
| `agent/persona.md` | Modificado | Define a personalidade e os limites do DIO Security Analyst: identidade, valores, jeito de falar, o que ele não faz e a regra de separar fato da inferência. |

### Conhecimento

| Arquivo | Status | Finalidade |
|---|---|---|
| `agent/knowledge/security-basics.md` | Criado | Base de conhecimento de segurança: tríade CIA, vulnerabilidade/ameaça/risco, princípio do menor privilégio, defense in depth, OWASP Top 10, SQL Injection, XSS, autenticação e autorização, hashing seguro de senhas, gerenciamento de segredos, patches, logs, segmentação de rede, backup e resposta a incidentes. |

### Skills

| Arquivo | Status | Finalidade |
|---|---|---|
| `skills/vulnerability-analysis/SKILL.md` | Criado | Guia passo a passo da skill: quando usar, fluxo de análise com oito etapas e modelo de relatório. |
| `skills/vulnerability-analysis/README.md` | Criado | Documentação da skill, orientada a estudantes e mentores, com exemplos de utilização e limites de segurança. |

### Aplicação de demonstração

| Arquivo | Status | Finalidade |
|---|---|---|
| `app.py` | Criado | Laboratório local de login com SQLite — artefato sobre o qual o agente realiza análise de segurança. |
| `laboratorio.db` | Criado | Banco de dados SQLite gerado ao iniciar o laboratório, contendo a tabela `usuarios` e o usuário de exemplo. |

### Documentação

| Arquivo | Status | Finalidade |
|---|---|---|
| `README.md` (raiz) | Modificado | Este guia — documentação profissional da especialização. |

> Este documento foi o único arquivo modificado nesta entrega. Os demais arquivos do repositório (skills de estudos, glossary, youcom-mcp, CLAUDE.md, entre outros) foram verificados e preservados.

---

## 4. Skill vulnerability-analysis

A skill `Análise de vulnerabilidades` é o método de trabalho do DIO Security Analyst. Ela orienta o agente a analisar vulnerabilidades em aplicações e infraestruturas, explicar causa, impacto e possibilidade de exploração, classificar severidade, relacionar identificadores CWE e CVSS, ligar técnicas a MITRE ATT&CK quando houver mapeamento adequado e recomendar correções com validação segura.

### Quando usar

Use a skill quando o estudante:

- quer revisar código ou configurações em busca de falhas de segurança;
- recebe um cenário (caixa-preta, blast radius, log, erro) e precisa de uma análise estruturada;
- pede ajuda para entender um aviso de segurança, erro de autenticação ou incoerença de acesso;
- quer produzir um relatório técnico de vulnerabilidade com correção e validação;
- está estudando OWASP Top 10, CWE, CVSS ou MITRE ATT&CK e quer aplicar o conhecimento a um caso concreto.

Não use quando o estudante:

- pede uma auditoria real de um sistema alheio ou de um ambiente sem autorização;
- quer explorar, destruir ou exfiltrar dados;
- pede para "burlar" um controle de segurança de um sistema que a pessoa não administra.

### Fluxo de análise

O agente segue sempre as oito etapas, na ordem, voltando à primeira se faltar informação:

1. **Entender o contexto** — ler o que o estudante enviou (código, log, configuração, enunciado) e reestruturar o cenário: o que é o ativo, quem o usa, onde está, em que ambiente.
2. **Confirmar autorização e escopo** — antes de qualquer análise que possa afetar um sistema, confirmar que a pessoa tem autorização explícita e que o escopo está definido. Se em dúvida, para e pergunta.
3. **Identificar ativos e possíveis riscos** — listar ativos (dados sensíveis, funções críticas, controles, infraestrutura, credenciais) e avaliar impactos em confidencialidade, integridade e disponibilidade.
4. **Analisar evidências** — localizar a evidência concreta: linhas de código, arquivos de configuração, URLs, headers, respostas de erro, logs, chamadas de API.
5. **Classificar as descobertas** — causa técnica, impacto, probabilidade de exploração, severidade, identificadores (CWE, CVSS, MITRE) e evidências.
6. **Recomendar correções** — correções imediatas e melhorias de longo prazo, priorizando o risco real.
7. **Definir como validar as correções** — testes e verificações propostos para comprovar que a correção funciona.
8. **Produzir o relatório técnico** — aplicar o modelo de relatório abaixo, deixando claro o que foi observado (fato) e o que é inferência (análise).

### Como o agente utiliza essa especialização

- O agente reconhece, pela mensagem do estudante, quando a situação pede análise de segurança e aplica a skill `Análise de vulnerabilidades` automaticamente — não é preciso "chamar" a skill.
- A skill está registrada em `AGENTS.md`, que o harness lê ao abrir o projeto, e tem seu próprio guia e documentação para estudantes e mentores.
- O agente não entrega respostas prontas para desafios da DIO — isso é papel da skill `Destravar desafio`.

### Modelo de relatório

O relatório técnico segue o modelo padrão:

```markdown
# Relatório de Análise de Segurança — [Título]

## 1. Resumo executivo
- O que foi avaliado: ...
- Ambiente/análise: ...
- Resultado geral: N descobertas (X informativas, Y baixas, Z médias, A altas, B críticas).
- Recomendação prioritária: ...

## 2. Descobertas
### 2.1 [Título da descoberna]
**Classificação:** informativa | baixa | média | alta | crítica
**Causa técnica:** ...
**Impacto:** ...
**Probabilidade de exploração:** ...
**Severidade:** ...
**CWE:** CWE-xxx (descrição abreviada)
**CVSS:** (escore estimado e justificativa dos componentes)
**MITRE ATT&CK:** (técnica, se houver mapeamento; caso contrário, omita)
**Evidências:**
- Trecho de código / configuração / log / endpoint: ...
- Explicação da evidência: ...
**Recomendação de correção:** ...
**Validação:** ...
```

### Materiais complementares

- Base de conhecimento de segurança: `agent/knowledge/security-basics.md`
- Documentação desta skill: `skills/vulnerability-analysis/README.md`

---

## 5. Demonstração prática

### O laboratório local: app.py

O laboratório é um sistema de login didático, em Python puro (sem frameworks externas), que utiliza o **SQLite** — o banco já vem incluído na biblioteca padrão do Python — para armazenar e validar credenciais. O arquivo `app.py` contém:

- `conectar()`: abre a conexão com `laboratorio.db`.
- `criar_banco()`: cria a tabela `usuarios (id, usuario, senha)` e insere o exemplo `admin` / `123456` (o uso de senha em texto plano é intencional, para fins didáticos do laboratório; não é uma recomendação de produção).
- `login(usuario, senha)`: consulta o banco pelo usuário e senha.
- `if __name__ == "__main__"`: gera o banco e exibe o menu interativo de login.

Para iniciar o laboratório, basta executar:

```bash
python app.py
```

O agente pode analisar o código, o banco ou o fluxo completo, indicando o que está em risco e como corrigir.

### A vulnerabilidade SQL Injection identificada

A skill identifica o padrão clássico de SQL Injection quando a entrada do usuário é concatenada diretamente dentro de uma consulta SQL. Ilustra-se pelo padrão de referência abaixo:

```python
import sqlite3

def buscar_usuario(email):
    conn = sqlite3.connect("banco.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM usuarios WHERE email = '{email}'")
    return cur.fetchone()
```

**O que a análise conclui:**

- **Causa técnica:** a variável `email`, que vem da entrada do usuário, é injetada diretamente na estrutura da consulta SQL. O banco não distingue dados da estrutura da consulta.
- **Impacto:** um atacante pode modificar a intenção da consulta — ler tabelas inteiras, alterar ou excluir dados, contornar autenticação ou, em bancos mais permissivos, executar comandos sobre o sistema. Afeta confidencialidade, integridade e disponibilidade.
- **Severidade:** normalmente **crítica** ou **alta**, dependendo do contexto (exposição da aplicação, privilégios do banco, ausência de controles adicionais).
- **CWE:** CWE-89 (SQL Injection).
- **CVSS:** depende do contexto. Como ilustração, uma consulta de login exposta sem autenticação chega a ter AV:N (acesso remoto), AC:L (sem interferência), PR:N (sem autenticação), UI:N (sem interação do usuário), S:U (escopo não alterado), C:H/I:H/A:H — o que resulta em escore crítico (~9.8). O relatório definitivo deve detalhar os componentes com base no ativo real.
- **MITRE ATT&CK:** o mapeamento direto só é feito quando houver correspondência com o comportamento observado; no caso de injeção via interface de login exposta, recomenda-se omitir se não houver informação da superfície de ataque.
- **Evidência:** a linha do código onde a entrada é interpolada na consulta, sem sanitização e sem parâmetros vinculados.

### A correção: consultas parametrizadas com placeholders

A correção substitui a concatenação de strings pela **vinculação de parâmetros** (parameterized queries / prepared statements). O banco trata a entrada como **dados**, nunca como parte da consulta.

```python
import sqlite3

def buscar_usuario(email):
    conn = sqlite3.connect("banco.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    return cur.fetchone()
```

Observações sobre o método:

- Para **SQLite**, o placeholder é `?`; para **PostgreSQL (psycopg2)**, é `%s`; para outras bases, o valor segue a documentação do driver (ex.: `:nome` em algumas bibliotecas).
- O segundo argumento de `execute()` é a tupla (ou dicionário) de parâmetros, enviada separadamente pelo driver.
- A mesma técnica vale para INSERT, UPDATE, DELETE e para queries dinâmicas com cláusulas que não contêm entradas do usuário.
- Em ORMs, usar os métodos de busca com parâmetros (ex.: `filter(u.email == email)` no SQLAlchemy) e nunca strings SQL construídas à parte.

### Como a correção foi validada

**Resultados efetivamente testados** (evidências reais do projeto):

- Revisão estática do código: o padrão de placeholders está aplicado corretamente na consulta de referência, sem interpolação de variáveis na string do SQL.
- Inicialização do laboratório: `python app.py` executa com sucesso, criando o banco `laboratorio.db` e exibindo o menu de login.
- Fluxo de login com credenciais de exemplo: `admin` / `123456` autoriza o acesso, confirmando que o fluxo continua funcionando normalmente.

**Validação recomendada (não executada neste projeto):**

- Envio de payloads comuns de SQL Injection (ex.: `' OR '1'='1`, `admin' --`, `1' OR '1'='1`) para a query de referência, confirmando que o banco trata o valor como dado e não retorna registros indevidos.
- Teste positivo: credenciais válidas continuam autenticando.
- Revisão de código automatizada (ex.: scan estático) verificando que nenhuma string de consulta contém entrada do usuário interpolada.

### Diferença entre resultados testados e recomendações adicionais

| Resultados efetivamente testados | Recomendações adicionais (não testadas) |
|---|---|
| Revisão estática do padrão de placeholders vs. interpolacao de string. | Envio de payloads de SQL Injection no laboratório. |
| Inicialização e fluxo de login do `app.py` com credenciais de exemplo. | Teste dinâmico de autenticação (enviar `admin` / `123456` e tentar a burla). |
| Verificação de que o código segue o método de queries parametrizadas. | Análise de configuração do servidor, firewall e rede. |
| | Armazenamento seguro de senhas (ex.: Argon2id, bcrypt, scrypt ou PBKDF2) no laboratório. |
| | Validação de correções via testes de aceitação. |

As recomendações adicionais são boas práticas de segurança, mas **não foram validadas** neste projeto: elas permanecem como sugestões para o estudante ou equipe executarem em um ambiente controle.

---

## 6. Como executar

### Como abrir o projeto no Hermes

1. No **Hermes**, abra a pasta raiz do projeto — a que contém o arquivo `AGENTS.md`.
2. O harness lê o `AGENTS.md` automaticamente e o agente assume a personalidade do **DIO Security Analyst**.
3. Não é necessário instalar pacotes, bancos ou dependências para conversar com o agente. O laboratório (`app.py`) usa SQLite, que já vem com o Python.

Alternativas de harness (conforme a documentação original do projeto): Google Antigravity, Claude Code, Codex, OpenCode. Todo harness que lê `AGENTS.md` funciona.

### Requisitos necessários

| Equipamento | Requisito |
|---|---|
| Para usar o agente | Um harness compatível com `AGENTS.md` (Hermes, Google Antigravity, Claude Code, Codex, OpenCode). |
| Para o laboratório | Python 3.x (o módulo `sqlite3` já vem na biblioteca padrão). |

### Comandos reais de instalação e inicialização

Os comandos abaixo são os indicados na documentação do projeto:

```bash
# 1. Clonar o repositório
git clone https://github.com/digitalinnovationone/dio-agent.git

# 2. Entrar ou abrir a pasta no harness (a pasta que contém AGENTS.md)
cd dio-agent

# 3. Manter o repositório atualizado
git pull

# 4. Iniciar o laboratório local
python app.py
```

> `git clone` e `git pull` são os comandos reais descritos no README do projeto. O comando `python app.py` inicia o laboratório local descrito na seção 5, com base no arquivo `app.py`.

### Exemplos de prompts para utilizar o agente

```text
Analisa este código e me diz se tem falhas de segurança:
[cola o código]
```

```text
Revisão de segurança de uma API REST: o que pode dar errado e como corrigir?
```

```text
Tenho um servidor Ubuntu exposto à internet e quero avaliar sua segurança.
(Dá contexto, autorização e escopo antes de recomendar qualquer procedimento.)
```

```text
O que significa essa mensagem de log de autenticação?
[cola a mensagem]
```

---

## 7. Cenário de avaliação

**Cenário:** "Tenho um servidor Ubuntu exposto à internet e quero avaliar sua segurança."

Nesse cenário, o agente **não inicia varredura, não escaneia portas, não tenta conectar-se ao servidor e não executa testes contra sistemas externos**. A primeira ação do agente é solicitar contexto, autorização e escopo antes de recomendar qualquer procedimento.

O agente pergunta, entre outros, se:

- o servidor pertence ao solicitante e há autorização formal;
- a avaliação é de uma produção ou de um ambiente de laboratório;
- serviços e portas estão expostos;
- SSH, firewall e atualizações estão configurados;
- há dados sensíveis no servidor;
- há restrições legais, planos de comunicação de incidentes e limites de escopo.

Assim que o contexto fornecido, a análise se baseia em boas práticas e em indicadores de risco (red flags) detectáveis sem acessar o sistema. O relatório deixa sempre claro o que seria verificado em uma avaliação real, com autorização, e o que só poderia ser confirmado após acesso ao ambiente.

As regras básicas do agente para este cenário:

- Somente ambientes autorizados e dentro do escopo definido.
- Nenhum procedimento destrutivo, nenhuma exfiltração de dados, nenhuma tentativa de obter persistência.
- Preferência por análise estática e verificações não destrutivas.
- Pergunta antes de agir sempre que houver dúvida sobre autorização.
- Não inventa evidências, escores ou vulnerabilidades: indica o que falta.

---

## 8. Decisões e melhorias

### Principais decisões de implementação

- **Especialização vertical separada do núcleo do DIO Agent.** A especialização em segurança foi construída como uma camada própria — personalidade (`agent/persona.md`), base de conhecimento (`agent/knowledge/security-basics.md`) e skill (`skills/vulnerability-analysis/`) — mantendo intacta a missão original de mentoria.
- **Base de conhecimento de segurança independente.** O `security-basics.md` reúne os modelos fundamentais (CIA, menor privilégio, defense in depth, OWASP Top 10, CWE, CVSS, MITRE ATT&CK, hashing, logs, segmentação e resposta a incidentes) para que o agente sempre possa apoiar sua análise em referências consolidadas.
- **Skill com fluxo obrigatório de oito etapas.** O método define uma ordem fixa de análise e um modelo de relatório padronizado, evitando respostas soltas e imprevisíveis.
- **Laboratório local como artefato de demonstração.** O `app.py` com SQLite ancilla a análise em um código real, pequeno e seguro para executar, ao mesmo tempo em que serve de prova de conceito.
- **Limites éticos definidos na configuração.** O agente não age em ambientes alheios sem autorização explícita, não realiza exploração destrutiva e não inventa evidências.

### A melhoria escolhida para o agente

A melhoria central foi transformar o DIO Agent — um mentor genérico de estudos — em um especialista com método: uma **specialização estruturada** com personalidade, conhecimento, fluxo de análise e demonstração prática. Em vez de ampliar a gama de tópicos sem profundidade, o projeto aprofundou o agente em um domínio, com um processo definido e com evidências reais do próprio repositório.

### Como a especialização diferencia o DIO Security Analyst de um chatbot genérico

| DIO Security Analyst | Chatbot genérico |
|---|---|
| Aplica um fluxo obrigatório de análise (8 etapas). | Responde a partir do padrão da conversa, sem método fixo. |
| Só age com autorização e escopo definido. | Não reflete limites legais e éticos. |
| Produz relatórios com evidências, causa, impacto, probabilidade, severidade, CWE, CVSS, MITRE. | Geralmente responde em parágrafos soltos, sem identificadores de risco. |
| Diferencia risco real de recomendação de boas práticas. | Pode misturar os dois, apresentando orientações genéricas como correções. |
| Nunca inventa evidências, CWE, CVSS ou MITRE. | Pode trazer informação incorreta ou não verificada. |
| Entrega orientação defensiva e ética, educando o estudante. | Não tem missão de aprendizado. |

---

## 9. Segurança e limitações

### Testes realizados em laboratório próprio

Todos os testes foram realizados no **laboratório local do repositório**:

- o sistema de login `app.py`;
- o banco SQLite `laboratorio.db` gerado pelo próprio laboratório.

O laboratório roda localmente e não expõe nenhuma rede. Nenhum teste foi executado em servidores ou dispositivos de terceiros.

### Ethics: avaliações somente em ambientes autorizados

O agente **não executa testes contra sistemas externos sem autorização explícita e escopo definido**. Ele não realiza exploração destrutiva, exfiltração de dados, tentativa de obter persistência ou ocultar atividades. Qualquer avaliação — inclusive o cenário do item 7 — deve ocorrer somente em ambientes autorizados (hábitos de uso são o primeiro controle de segurança).

### Limitações do agente

- **Análise estática.** O agente lê código, logs e configurações; não possui acesso ao ambiente em execução.
- **Sem acesso à rede de produção.** Em um cenário de servidor exposto, o agente apenas orienta o que deveria ser verificado, não o verifica.
- **Não substitui auditoria formal.** Relatórios técnicos de segurança são apoio ao aprendizado e a decisões de priorização; não substituem auditorias executadas por profissionais qualificados.
- **Semiconexões de escopo.** Qualquer classificação depende de contexto: a superfície de ataque, os privilégios do sistema e os controles existentes. Quando o contexto é insuficiente, o agente indica o que falta em vez de adivinhar.
- **Laboratório didático.** O `app.py` armazena a senha de exemplo em texto plano — intencional, para fins de aprendizado; não é uma boa prática de produção.
- **Sem garantia de remediação.** O agente entrega análise e recomendações; não garante que um ativo esteja livre de novas vulnerabilidades.

---

## 10. Conclusão

O DIO Security Analyst consolida uma especialização completa dentro do repositório do DIO Agent, com:

- **personalidade e limites definidos** (`agent/persona.md`);
- **base de conhecimento de segurança** (`agent/knowledge/security-basics.md`);
- **skill com método e modelo de relatório** (`skills/vulnerability-analysis/`);
- **registro no harness** (`AGENTS.md`);
- **laboratório de demonstração** (`app.py` + `laboratorio.db`);
- **documentação profissional da especialização** (este README).

Os principais aprendizados foram: como estruturar uma especialização de agente com método; a importância de não entregar respostas prontas, mas de conduzir o estudante ao raciocínio; e como produzir análises defensivas e éticas, com evidências, classificação de risco e validação clara das recomendações.

---

## Referências e documentação complementar

- Glossário do projeto: `docs/glossary.md`
- Conectar a busca do You.com: `docs/youcom-mcp.md`
- Documentação do Hermes: https://hermes-agent.nousresearch.com/docs
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- MITRE ATT&CK: https://attack.mitre.org/
- CWE: https://cwe.mitre.org/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- NIST SP 800-53 rev. 5: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final

---

## Próximos passos — itens pendentes de preenchimento manual

Lista de itens que merecem preenchimento ao longo do projeto (sem conteúdo, por enquanto):

- Prints e vídeos de demonstração do agente analisando código de segurança.
- Exemplo de relatório técnico gerado automaticamente pelo agente em um cenário completo.
- Capturas de tela do laboratório `app.py` em execução.
- Lista de verdicts de validação dos testes de SQL Injection propostos.
- Registro de revisões manuais realizadas sobre as recomendações adicionais.
