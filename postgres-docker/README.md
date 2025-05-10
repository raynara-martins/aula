Realizada criação de pasta para melhor organização do projeto da prática 01

postgres-docker/
├── docker/
│   ├── init.sql                     # script sql para população do bd
│   ├── postgres.dockerfile          # dockerfile postgresqk
│   ├── python.dockerfile            # dockerfile python
│   └── csv.dockerfile               # dockrfile para geraçao de csv
├── src/
│   ├── read_database.py            # cod em python para ler os dados
│   ├── generate_and_read_csv.py    # cod em phyton para gerar e ler o csv
│ 
├── docker-compose.yml               # config do dcker compose
├── requirements.txt                 # dependencias do python
