import gtts
from playsound import playsound

start_texto = "Para prosseguir, selecione uma opção disponível que poderá lhe ajudar no seu atendimento 👇"

txt_seac = "A secretaria Acadêmica | SEAC é o setor responsável pelo controle, verificação, registro e arquivamento da "
txt_seac +="documentação da vida acadêmica do aluno, desde seu ingresso na Instituição, até a conclusão e/ou expedição do diploma.\n"
txt_seac +="\nA missão da Secretaria Acadêmica é realizar com presteza e eficácia todos os procedimentos que envolvem o controle e o "
txt_seac +="registro acadêmico, assim como orientar os alunos para os mesmos."

seac_contato = """\n
Responsáveis:
Renato Silva de Oliveira (Secretário acadêmico)
Anderson de Brito Rodrigues
Maria Vilanir Gonçalves Duarte da Silva
Rafael da Silva Araújo\n
Informação para contato:
Telefone: (84) 4005-4111
Ramal 7406 / 7436
E-mail: seac.sga@ifrn.edu.br
Canal Telegram: https://t.me/secretariaacademicaifrnsga
"""

txt_coex = """A Coordenação de Extensão (COEX) tem como objetivo central garantir a interação entre o IFRN e a comunidade externa.\n"""
txt_coex += """\nCom isso, busca garantir a divulgação, o desenvolvimento de novas tecnologias e a manutenção da relação com o mundo do trabalho para que desta forma seja efetiva a qualidade da formação dos nossos estudantes."""

coex_contato = """\n
Responsáveis:
Fernando de Oliveira Freire (Coordenador)\n
Informação para contato:
Telefone: (84) 4005-4111 - Ramal 7410
E-mail: 
coex.sga@ifrn.edu.br 
extensão.sga@gmail.com
Canal Telegram: https://t.me/coordenacaodeextensaoifrnsga
Grupo WhatsApp: https://chat.whatsapp.com/LNw9BvA5qsV0H3QOeypzDK
Instagram: https://www.instagram.com/coex.sga/
Link Coex: https://linktr.ee/coex.sga
"""

FAQ = """
\nOlá, caro(a) requerente 🤗 há alguma dúvida para esclarecer ❓ Aqui segue algumas das perguntas frequentes do setor selecionado.
veja e selecione aquela que melhor atende sua expectativa. Espero que isso lhe ajude em sua busca.
Caso não encontre o que procura, minhas recomendações são:
1 - Entre em contato com o setor 🏢
2 - Entre em contato com o gerente 👤 deste sistema para sugerir 💬 alguma implementação.
3 - Busque atendimento presencial com o setor 🏢 nos horários de funcionamento ⏱ 
"""

txt_comum = """Link SUAP: https://suap.ifrn.edu.br/accounts/login/?next=/
Link Requerimento Padrão: https://portal.ifrn.edu.br/campus/saogoncalo/arquivos/formularios-seac/requerimento-padrao/
Com o tal requerimento é possível solicitar:
- Matrículas;
- Cancelamento de matrícula;
- Renovação de matrícula (semestral ou anual);
- Trancamento de matrícula ou disciplinas;
- Adequação de horários / Estudo individualizado;
- Atendimento domiciliar;
- Dispensa de atividades;
- Justificativa de falta;
- Mudança de curso / turma / turno;
- Reposição de atividades;
- Revisão de faltas / notas / situação;
- Transferência """

txt_faq_seac1 = """Como justificar faltas❓ ou\nComo solicitar reposição de atividades❓\n
A solicitação deverá ser realizada através de chamado no SUAP, anexando o requerimento juntamente com os documentos comprobatórios.
"""

txt_faq_seac2 = f"""Como solicitar mudança de tuno ou turma❓\n
A solicitação deverá ser realizada através de chamado no SUAP, anexando o requerimento juntamente com justificativa irrefutável da necessidade de mudança de turno ou turma.
Para menores de 18 anos o requerimento deverá ser assinado pelo responsável juntamente com a cópia do RG (Frente e Verso) do responsável.
{txt_comum}
"""

txt_faq_seac3 = f"""Como solicitar o aproveitamento de estudos❓\n
A solicitação deverá ser realizada através de chamado no SUAP, anexando o requerimento juntamente com os documentos comprobatórios.\n
O requerimento para aproveitamento de estudos deverá ser acompanhado dos seguintes documentos:\n
I.	Histórico acadêmico;
II.	Programas de disciplinas cursadas, objeto da solicitação; e
III.	Documento que comprove a autorização de funcionamento ou o reconhecimento do curso de origem.

Art. 269. Poderão ser objeto de aproveitamento de estudos as disciplinas:\n
a)  cujos conteúdos e cargas horárias coincidirem em, no mínimo, 70% (setenta por cento) com os programas das disciplinas do respectivo curso oferecido pelo IFRN;
b)  cursadas com aprovação em outros cursos do mesmo nível de ensino ou outros cursos de nível posterior, independentemente da nota final obtida, excetuando-se os cursos técnicos de nível médio nos quais somente poderá ser concedido o aproveitamento de disciplinas cursadas em outro curso técnico de nível médio;
c)  cursadas antes do ingresso do estudante no IFRN;
d)  cursada num prazo máximo de 5 (cinco) anos, decorridos entre o final do período em que a disciplina foi cursada e a data de requerimento do aproveitamento de estudos; e
e)  cujas disciplinas pré-requisitos, quando houver, tiverem sido integralizadas.

§ 1º. A equivalência de estudos poderá ser contabilizada a partir de estudos realizados em uma disciplina ou em duas ou mais disciplinas que se complementam no sentido de integralizar uma disciplina do curso.
§ 2º. A análise de equivalência entre matrizes curriculares será realizada pelo Coordenador de Curso, que encaminhará o processo para análise de equivalência entre programas de disciplinas.
§ 3º. A análise de equivalência entre programas de disciplinas será realizada por pelo menos um docente especialista da disciplina objeto do aproveitamento, que emitirá parecer conclusivo sobre o pleito.
§ 4º. A avaliação da correspondência de estudos deverá recair sobre os conteúdos que integram os programas das disciplinas apresentadas e não sobre a denominação das disciplinas cursadas. § 5º. Será registrada no histórico acadêmico do estudante a média aritmética ponderada da(s) disciplina(s) aproveitadas, tendo como peso a carga horária da(s) disciplina(s) correlata(s).

Art. 270. É vedado o aproveitamento de estudos de disciplinas em que o requerente haja sido reprovado no IFRN.  Organização Didática do IFRN. IFRN, 2012.
Art. 271. Com vistas ao aproveitamento de estudos, os(as) estudantes de nacionalidade estrangeira ou brasileiros(as) com estudos realizados no exterior deverão apresentar documentação legalizada por via diplomática e com equivalência concedida pelo respectivo sistema de ensino.\n
{txt_comum}
"""

txt_faq_seac4 = """Como requerer a certificação de conhecimentos❓\n
A inscrição para a certificação de conhecimentos deverá ser efetuada através de chamado no SUAP, anexando o requerimento com a enumeração das disciplinas requeridas.\n
Art. 272. O processo de certificação de conhecimentos consistirá em uma avaliação teórica ou teórico-prática, conforme as características da disciplina, com calendário de provas a ser divulgado pela Diretoria Acadêmica ofertante.\n
Art. 273. A certificação de conhecimentos será realizada por uma banca examinadora designada pelo respectivo Diretor Acadêmico, ouvido o Coordenador de Curso, e constituída por um membro da equipe técnico-pedagógica e, no mínimo, dois docentes especialistas da(s) disciplina(s) em que o estudante será avaliado, cabendo a essa comissão emitir parecer conclusivo sobre o pleito.\n
Parágrafo único. Será dispensado de cursar uma disciplina o estudante que alcançar aproveitamento igual ou superior a 60 (sessenta) nessa avaliação, sendo registrado no seu histórico acadêmico o resultado obtido no processo.\n
Art. 274. A inscrição para a certificação de conhecimentos deverá ser efetuada através de requerimento ao respectivo Diretor Acadêmico, com a enumeração das disciplinas requeridas.\n 
§ 1º. O número máximo de requerimentos para realização de certificação de conhecimentos não deverá exceder 4 (quatro) avaliações por estudante em cada período letivo.\n
§ 2º. Para cada disciplina do curso, será permitido ao estudante requerer a certificação de conhecimentos uma única vez.\n 
Art. 275. Em caso de ausência a qualquer avaliação de certificação de conhecimentos, esta ficará automaticamente cancelada, não cabendo recurso.\n 
Art. 276. É vedada a certificação de conhecimentos de disciplinas em que o requerente tenha sido reprovado no IFRN.\n 
Art. 277. Para os cursos técnicos na forma integrada, é vedada a certificação de conhecimentos de disciplinas referentes aos núcleos fundamental e estruturante.\n 
"""

txt_faq_seac4 = f"""Emissão de Diploma
A solicitação deverá ser realizada através de chamado no SUAP, anexando cópia do RG, CPF, Certidão de Nascimento/ Casamento e Nada-Consta (O documento é feito virtualmente pela SEAC).
Prazo de atendimento é de até 30 dias.

"""