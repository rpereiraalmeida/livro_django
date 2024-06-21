### PROJETO DE ESTUDO PÓS DESENVOLVIMENTO WEB COM DJANGO ###

Usuários e Permissões 

 - Admin: possui permissão em todas as áreas do sistema
 - Médico: pode editar seu perfil, adicionando especialidades e locais de trabalho a ele.
 - Paciente: pode editar seu perfil, adicionando preferências de localidades e especialidades e
   poderá realizar buscas de médicos nos sistema.

Telas
  - Admin:
    - Gerenciamento de usuários.
    - Gerenciamento de especialidades.
    - Gerenciamento de tipos de usuários.
    - Gerenciamento de permissões de telas.
    - Vê todas as telas que o médico e o paciente veem.
  - Médico:
    - Gerenciamento do pŕoprio perfil.
    - Vê todas as telas que o paciente vê.
  - Paciente:
    - Login.
    - Gerenciamento do próprio perfil.
    - Busca de Médicos.
    - Favoritos.
   
Criando e customizando as models
  - Speciality: especialidades que serão atribuidas aos médicos
  - DayWeek: dias da semana com atendimento na clinica
  - State: estados do país
  - City: cidades de um estado
  - Neighborhood: bairros de uma cidade
  - Address: endereços de atendimento do médico
  - Rating: tabela onde serão adicionadas as pontuações aos médicos