# Sistema de Gerenciamento de Inventário de Hardware e Software

## 1. Introdução: A Causa e a Necessidade
Em ambientes de TI, o gerenciamento de ativos é um desafio constante. Perder o controle de onde estão os equipamentos (computadores, impressoras, etc.) e quais softwares estão instalados pode levar a problemas de segurança, gastos desnecessários com licenças e dificuldades em planejar manutenções e upgrades.

A ideia para este projeto surgiu da necessidade de resolver esse problema de forma simples e eficiente. A intenção é fornecer uma ferramenta que permita a um Analista de Suporte de TI manter um inventário organizado, garantindo que a equipe tenha uma visão clara de todos os ativos, desde o momento da aquisição até seu descarte.
---
## 2. Tecnologias Utilizadas
O projeto foi desenvolvido usando as seguintes tecnologias, escolhidas por sua eficiência, simplicidade e relevância no mercado de TI:

**Python**: A linguagem de programação principal. Foi escolhida por sua sintaxe clara, facilidade de uso e por ser uma ferramenta poderosa para automação de tarefas e scripts, que são habilidades cruciais para um Analista de Suporte.

**SQLite**: Um sistema de gerenciamento de banco de dados (SGBD) leve e baseado em arquivo. A escolha do SQLite permite que o aplicativo funcione sem a necessidade de um servidor de banco de dados externo, o que o torna ideal para ambientes menores e para demonstrações de portfólio. Ele é perfeito para armazenar dados de forma estruturada.

---
## 3. Funcionalidades e Intenção do Aplicativo
O aplicativo foi projetado para ser uma ferramenta de linha de comando (CLI) com um conjunto claro de funcionalidades:

**Gerenciamento de Hardware:**

Adicionar, Editar e Deletar informações de dispositivos como PCs, notebooks e impressoras.

Rastreamento de Status: Permite que o analista altere o status de um dispositivo (por exemplo, de "Em uso" para "Em manutenção" ou "Armazenado").

Controle de Localização: Ajuda a saber onde cada equipamento está localizado fisicamente na empresa.

**Gerenciamento de Software:**

Associação de Software a Hardware: Cada licença de software pode ser associada a um dispositivo específico, facilitando o controle de licenças.

Rastreamento de Versão e Chave de Licença: Evita a pirataria e garante que o software esteja atualizado e licenciado corretamente.

A intenção é que este aplicativo sirva como uma base sólida para a gestão de ativos, podendo ser expandido no futuro com novas funcionalidades, como relatórios automáticos, alertas de licença e uma interface gráfica mais robusta.

---
## 4. Resumo do Projeto
Este projeto de portfólio demonstra a capacidade de um profissional de TI em desenvolver uma solução prática para um problema real de negócios. Ao usar Python para a lógica e SQLite para o armazenamento de dados, criei um Sistema de Gerenciamento de Inventário de Hardware e Software funcional. O sistema não apenas organiza o inventário, mas também serve como uma prova de habilidades técnicas em programação, automação, gerenciamento de banco de dados e resolução de problemas, todas competências essenciais para a função de Analista de Suporte de TI.