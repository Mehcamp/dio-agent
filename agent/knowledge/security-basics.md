# Segurança da Informação em uma visão geral

Base de conhecimento fundamental para o agente **DIO Security Analyst**. Use sempre que o contexto de segurança for necessário para analisar vulnerabilidades, explicar relatórios ou orientar correções.

## Tríade CIA

A tríade CIA é o modelo conceitual mais usado para avaliar impactos de segurança:

- **Confidencialidade:** garante que a informação só seja acessada por pessoas autorizadas. Vulnerabilidades que violam a confidencialidade incluem exposição de dados, SQL Injection que lê tabelas, XSS que rouba sessões, exposição de credenciais e arquivos não protegidos.
- **Integridade:** garante que a informação não foi alterada indevidamente. Vulnerabilidades que violam a integridade incluem injeção de dados em consultas, XSS que altera conteúdo da página, alteração de arquivos de configuração, ataque de tipo man-in-the-middle e correção de logs.
- **Disponibilidade:** garante que os ativos estejam acessíveis quando necessários. Vulnerabilidades que violam a disponibilidade incluem negação de serviço, exclusão de dados, desativação de contas críticas e exposição de informações que permitem travar um sistema.

Qualquer descoberta de segurança deve ser lida em termos de qual (ou quais) dos três pilares ela compromete.

## Vulnerabilidade, ameaça, risco e impacto

- **Vulnerabilidade:** uma falha, defeito ou fraqueza em um sistema (código, configuração, processo). Ex.: não sanitizar entrada, senha armazenada sem hash, porta de serviço sem firewall.
- **Ameaça:** uma possível ação ou evento que pode aproveitar uma vulnerabilidade. Ex.: um atacante automaticamente tentando SQL Injection, um scraper coletando dados expostos, um atacante que rouba uma senha criptografada.
- **Risco:** a probabilidade de uma ameaça aproveitar uma vulnerabilidade, combinada com o impacto. O risco não é só "a falha existe", é "quão provável é que ela seja explorada e com que consequência".
- **Impacto:** as conseqüências de um ataque bem-sucedido sobre um ativo. Ex.: vazamento de dados, perda de integridade, indisponibilidade de serviço.

Diferenciar esses conceitos evita que o agente trate uma vulnerabilidade de "crítica" só porque o nome soa grave, e sim porque o risco concreto é baixo ou alto.

## Princípio do menor privilégio

- Toda entidade (usuário, processo, serviço, conta) deve ter apenas os privilégios mínimos necessários para executar sua função.
- Aplica-se a: contas de banco de dados (usuário com `SELECT` apenas onde for preciso), serviços que rodam com conta limitada, contas de API com escopo reduzido, permissões de arquivos e diretórios.
- Benefícios: limita o blast radius. Se um serviço é comprometido, ele só consegue acessar o que já tem autorização para acessar.

## Defense in Depth

- Estratégia de defender um ativo em camadas, de forma que a falha de uma camada não mate a defesa.
- Exemplo: API validada (app), autenticação obrigatória (rede/load balancer), WAF (rede), servidores na rede privada (rede), monitoramento (detecção).
- O objetivo não é "um único controle perfeito", mas "muitas camadas que impedem o avanço de um ataque".

## Secure by Design e Secure by Default

- **Secure by Design:** a segurança é considerada na fase de arquitetura, não sobreporretamente no final. Exemplos: arquitetura zero trust, não expor serviços diretamente à internet, limpeza de dado por design.
- **Secure by Default:** o sistema entra operando com configurações seguras por padrão. Exemplo: novas instâncias de banco de dados localizam em localhost por padrão, não expõem interface de rede; aplicativos não rodam como root; login padrão não é a senha "admin".
- Quando um controle não está presente por padrão, o estado "default" do sistema pode ser a porta de entrada de um atacante.

## OWASP Top 10

- Referenciação anual de riscos mais críticos para aplicações web, publicada pela OWASP. Os tópicos principais:
  1. **A01:2021 – Broken Access Control** (controle de acesso quebrado): usuários conseguem acessar dados/funcionalidades de outros usuários ou não há verificação de permissão.
  2. **A02:2021 – Cryptographic Failures** (falhas criptográficas): dados sensíveis expostos por falta de criptografia, uso de algoritmos fracos ou armazenamento incorreto.
  3. **A03:2021 – Injection** (injeção): SQL, NoSQL, OS, LDAP, XSS, template injection, etc.
  4. **A04:2021 – Insecure Design** (design inseguro): falhas arquiteturais e de fluxo, não implementação.
  5. **A05:2021 – Security Misconfiguration** (configuração insegura): serviços sem patch, headers inadequados, contas padrão, API sem autenticação, verbose errors.
  6. **A06:2021 – Vulnerable and Outdated Components** (componentes vulneráveis e desatualizados): dependências com vulnerabilidade conhecida.
  7. **A07:2021 – Identification and Authentication Failures** (falhas de identificação e autenticação): reutilização de senhas, validação fraca, timeout de sessão, credenciais expostas.
  8. **A08:2021 – Software and Data Integrity Failures** (falhas de integridade de software e dados): atualizações não verificadas, artefatos não verificados, CI/CD não seguro.
  9. **A09:2021 – Security Logging and Monitoring Failures** (falhas de logging e monitoramento): sem regras de log, logs sem secreção, ausência de alertas.
  10. **A10:2021 – Server-Side Request Forgery (SSRF)** (requisição de servidor mal-intencionada): entrada que faz o servidor fazer solicitação para local interno.

Para a skill de análise, este mapa serve de referenciação para classificar descobertas e associar a CWE.

## SQL Injection e consultas parametrizadas

- **O que é:** quando uma entrada da aplicação é injetada diretamente em uma consulta SQL, alterando a intenção original da consulta.
- **Exemplo de fraqueza:** `SELECT * FROM usuarios WHERE email = '<input>'`.
- **Exemplo de exibição de erro:** se o erro do banco é mostrado ao usuário, um atacante pode forçar consultas inválidas e extrair estrutura do banco.
- **Consulta parametrizada (segura):** usar placeholders e binder de parâmetros, sem concatenar entrada na consulta:
  ```python
  # Python / psycopg2
  cur.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
  ```
  Ou, em ORMs, usar os métodos de busca com parâmetros, não strings dinâmicas.
- **Outras medidas:** não exibir erros do banco no frontend, restringir privilégios do usuário do banco à necessidade mínima, validação de entrada como camada defensiva (não substitui parâmetros).
- **CWE associado:** CWE-89 (SQL Injection).

## XSS

- **O que é:** injeção de script executável no contexto do navegador de outro usuário, quando o aplicativo reflete ou armazena entrada não sanitizada.
- **Tipos:**
  - **Reflected:** entrada refletida imediatamente em resposta (ex.: parâmetro na URL). Exige interação do usuário.
  - **Stored:** entrada é persistida (ex.: comentário) e renderizada para outros usuários.
  - **DOM-based:** a vulnerabilidade está no código JavaScript do lado do cliente que processa dados de forma insegura.
- **Controle:** usar Headers de resposta (`Content-Security-Policy`, `X-Content-Type-Options: nosniff`), HTML-escape de saída, e evitar `innerHTML` com dados não confiáveis. No frontend, uma política de conteúdo estrita impede a maioria dos payloads.
- **CWE associado:** CWE-79 (XSS).

## Autenticação e autorização

- **Autenticação:** verificar quem é o usuário (senha, 2FA, SSO, biometria). Fraquezas: senhas fracas, vômito de tentativas, sem bloqueio, sem expiração de sessão, sem 2FA em produção, exposição de credenciais.
- **autorização:** verificar o que o usuário autenticado pode fazer. Fraquezas: controle de acesso baseado apenas no cliente (JS), verificação de permissão ausente nos endpoints, IDOR (Insecure Direct Object Reference), onde um `?id=123` permite acessar outro registro.
- **Boas práticas:** verificar permissão no servidor para cada operação sensível; usar sessão com timeout; usar rate limiting em endpoints de login; registrar tentativas de autenticação; não expor IDs de recurso diretamente sem verificação.

## Hashing seguro de senhas

- **O que NÃO fazer:** armazenar senha em texto plano, ou usar `MD5`/`SHA-1` (que são rápidos e vulneráveis a brute force e rainbow tables).
- **O que fazer:** usar algoritmos deliberadamente lentos e adaptativos para senhas:
  - **Argon2id** (preferido),
  - **scrypt**,
  - **bcrypt** (com cost factor ajustável),
  - **PBKDF2** (apenas quando ausência de alternativa).
- **Por que:** o objetivo é tornar o truque por força bruta economicamente inviável. O custo de CPU/RAM é medido em "rounds" ou "iterations"; aumentar o fator de custo reduz a velocidade de ataque.
- **Adicional:** sempre usar um "salt" único por senha (gerado pelo algoritmo). Não reutilizar o mesmo salt.

## Gerenciamento de segredos

- **O que são segredos:** chaves de API, strings de conexão, tokens JWT, senhas de banco, credenciais de nuvem, certificados.
- **Riscos:** exposição em código, em logs, em variáveis de ambiente, em arquivos de configuração versionados, em imágenes de container.
- **Boas práticas:** usar um gerenciador de segredos (ex.: Vault, AWS Secrets Manager, GCP Secret Manager, Kubernetes Secrets com crypto, 1Password, etc.); nunca versionar `.env` com segredos; rotacionar credenciais periodicamente; usar escopos mínimos nos tokens; validar caminhos e carregamento apenas de secretos no tempo de execução.

## Atualizações e gerenciamento de patches

- **Risco:** componentes com vulnerabilidades conhecidas (CVE) são um dos maiores vetores de comprometimento, especialmente em frameworks e bibliotecas.
- **Boas práticas:** manter um inventário de dependências (ex.: `package-lock.json`, `requirements.txt`, `go mod`, `pip freeze`), monitorar CVE publicados, testar updates em ambiente staging antes de produção, automatizar a verificação de Patch em servidores.

## Logs e monitoramento

- **O que logar:** autenticações (sucesso e falha), erros críticos, acesso a dados sensíveis, modificações de configuração, eventos de segurança relevantes.
- **O que NÃO logar:** senhas, tokens, dados pessoais sem necessidade, conteúdo de requisições com segredos.
- **Segmentação:** separar logs de aplicação, acesso ao sistema, rede. Enviar para um sistema centralizado (SIEM), com retenção e acesso restrito.
- **Monitoramento:** alertas sobre tentativas de autenticação falhas em massa, abertura de portas inesperadas, modificação de arquivos de config, acesso fora do horário comercial,mspace entre esses conceitos evita que o agente trate uma vulnerabilidade de "crítica" só porque o nome soa grave, e sim porque o risco concreto é baixo ou alto. O que é "O"?
- **Boas práticas:** se o log exibir requisiões, esse log já foi avaliado.

## Segmentação de rede

- **O que é:** dividir a rede em sub-redes ou zonas, de forma que um componente não consiga atacar outro diretamente.
- **Exemplos:** aplicação em zona pública, banco em zona privada, serviços de gerenciamento em rede interna isolada, uso de firewalls/security groups para restringir tráfego.
- **Benefício:** reduz o "cobertura do atacante". Se a API só fica exposta via load balancer e o banco só responde a requisições da API, um ataque ao frontend não abre um acesso direto ao banco.

## Backup e recuperação

- **Objetivo:** possibilitar restauração após falha, ransomware ou exclusão acidental.
- **Boas práticas:** 3-2-1 (mínimo 3 cópias, 2 diferentes mídias, 1 fora da linha), testes periódicos de recuperação, criptografia dos backups, controle de acesso ao armazenamento de backups (não expuser ao mundo).

## Resposta a incidentes

- **Etapas orientadoras:** preparação, identificação, contaminação, contenção, erradicação, recuperação, lições aprendidas.
- **O papel do agente:** em cenários de incidente, manter o agente focado em análise e comunicação, não em ações de response (como "zerar servidor") que precisam de aprovação da equipe responsável.
- **Ressalva:** nenhum relatório de análise substitui um plano de response formal e testes de emergência.

## Referências rápidas

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- MITRE ATT&CK: https://attack.mitre.org/
- CWE: https://cwe.mitre.org/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- NIST SP 800-53 (controles de segurança): https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
