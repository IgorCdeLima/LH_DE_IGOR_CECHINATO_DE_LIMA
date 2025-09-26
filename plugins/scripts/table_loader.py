
import pandas as pd

class TableLoader:

    CHUNKSIZE = 1

    def __init__(self, conn, address_tables):
        self.conn = conn
        self.addres_tables = address_tables

    def table_loader(self):
        try:
            with self.conn.cursor() as cur:
                # checks the existence of the agencias table
                cur.execute("""
                        SELECT EXISTS(
                        SELECT 1
                        FROM information_schema.tables
                        WHERE table_schema = 'public'
                            AND table_name = 'agencias'
                        )
                        """)
                agencias = cur.fetchone()[0]
                if (agencias) is True: self.agencias_table(self.addres_tables[0])
                else: print("could not connect the table agencias")

                # checks the existence of the clientes table
                cur.execute("""
                        SELECT EXISTS(
                        SELECT 1
                        FROM information_schema.tables
                        WHERE table_schema = 'public'
                            AND table_name = 'clientes'
                        )
                        """)
                clientes = cur.fetchone()[0]
                if (clientes) is True: self.clientes_table(self.addres_tables[1])
                else: print("could not connect the table clientes")

                # checks the existence of the colaborador_agencia table
                cur.execute("""
                        SELECT EXISTS(
                        SELECT 1
                        FROM information_schema.tables
                        WHERE table_schema = 'public'
                            AND table_name = 'colaborador_agencia'
                        )
                        """)
                colaborador_agencia = cur.fetchone()[0]
                if (colaborador_agencia) is True: self.colaborador_agencia_table(self.addres_tables[2])
                else: print("could not connect the table colaborador_agencia")

                # checks the existence of the colaboradores table
                cur.execute("""
                        SELECT EXISTS(
                        SELECT 1
                        FROM information_schema.tables
                        WHERE table_schema = 'public'
                            AND table_name = 'colaboradores'
                        )
                        """)
                colaboradores = cur.fetchone()[0]
                if (colaboradores) is True: self.colaboradores_table(self.addres_tables[3])
                else: print("could not connect the table colaboradores")


                # checks the existence of the clientes table
                cur.execute("""
                        SELECT EXISTS(
                        SELECT 1
                        FROM information_schema.tables
                        WHERE table_schema = 'public'
                            AND table_name = 'contas'
                        )
                        """)
                contas = cur.fetchone()[0]
                if (contas) is True: self.contas_table(self.addres_tables[4])
                else: print("could not connect the table contas")

                # checks the existence of the proposta_credito table
                cur.execute("""
                        SELECT EXISTS(
                        SELECT 1
                        FROM information_schema.tables
                        WHERE table_schema = 'public'
                            AND table_name = 'propostas_credito'
                        )
                        """)
                proposta_credito = cur.fetchone()[0]
                if (proposta_credito) is True: self.propostas_credito_table(self.addres_tables[5])
                else: print("could not connect the table proposta_credito")

        except Exception:
            raise

    def agencias_table(self, address_table):
        print("Inserting data into the agencias table ")
        try:
            with self.conn.cursor() as cur:
                for chunk in pd.read_csv(address_table, chunksize=self.CHUNKSIZE):
                    chunk.columns = chunk.columns.str.strip() 
                    for index, row in chunk.iterrows():
                        data = {
                            'cod_agencia': int(row['cod_agencia']),
                            'nome' : row['nome'],
                            'endereco' : row['endereco'],
                            'cidade' : row['cidade'],
                            'uf' :  row['uf'],
                            'data_abertura' : row['data_abertura'],
                            'tipo_agencia' : row['tipo_agencia']
                        }
                        cur.execute(
                            """INSERT INTO public.agencias(cod_agencia, nome, endereco, cidade, uf, data_abertura, tipo_agencia) 
                            VALUES (%(cod_agencia)s, %(nome)s, %(endereco)s, %(cidade)s, %(uf)s, %(data_abertura)s, %(tipo_agencia)s) 
                            ON CONFLICT (cod_agencia) DO NOTHING
                            RETURNING cod_agencia;
                            """, data)
                        
                        result = cur.fetchone()
                        if result:
                            continue
                            print(f"Inserted line: {data['cod_agencia']}")
                        else:
                            continue
                            print(f"line not inserted: {data['cod_agencia']}")

        except Exception:
            raise 
        
        print("insertion completed in the agencias table")
        
    def clientes_table(self, address_table):
        print("Inserting data into the clientes table ")
        try:
            with self.conn.cursor() as cur:
                for chunk in pd.read_csv(address_table, chunksize=self.CHUNKSIZE):
                    chunk.columns = chunk.columns.str.strip()  
                    for index, row in chunk.iterrows():
                        data = {
                            'cod_cliente': int(row['cod_cliente']),
                            'primeiro_nome' : row['primeiro_nome'],
                            'ultimo_nome' : row['ultimo_nome'],
                            'email' : row['email'],
                            'tipo_cliente' :  row['tipo_cliente'],
                            'data_inclusao' : row['data_inclusao'],
                            'cpfcnpj' : row['cpfcnpj'],
                            'data_nascimento' : row['data_nascimento'],
                            'endereco' : row['endereco'],
                            'cep' : row['cep']
                        }
                        cur.execute(
                            """INSERT INTO public.clientes(cod_cliente, primeiro_nome, ultimo_nome, email, tipo_cliente, data_inclusao, cpfcnpj, data_nascimento, endereco, cep) 
                            VALUES (%(cod_cliente)s, %(primeiro_nome)s, %(ultimo_nome)s, %(email)s, %(tipo_cliente)s, %(data_inclusao)s, %(cpfcnpj)s, %(data_nascimento)s, %(endereco)s, %(cep)s) 
                            ON CONFLICT (cod_cliente) DO NOTHING
                            RETURNING cod_cliente;
                            """, data)
                        
                        result = cur.fetchone()
                        if result:
                            continue
                            print(f"Inserted line: {data['cod_cliente']}")
                        else:
                            continue
                            print(f"line not inserted: {data['cod_cliente']}")

        except Exception:
            raise 
        
        print("insertion completed in the clientes table")
        
    def colaborador_agencia_table(self, address_table):
        print("Inserting data into the colaborador_agencia table ")
        try:
            with self.conn.cursor() as cur:
                for chunk in pd.read_csv(address_table, chunksize=self.CHUNKSIZE):
                    chunk.columns = chunk.columns.str.strip()  
                    for index, row in chunk.iterrows():
                        data = {
                            'cod_colaborador': int(row['cod_colaborador']),
                            'cod_agencia' : int(row['cod_agencia']),
                        }
                        cur.execute(
                            """INSERT INTO public.colaborador_agencia(cod_colaborador, cod_agencia) 
                            VALUES (%(cod_colaborador)s, %(cod_agencia)s) 
                            ON CONFLICT (cod_colaborador, cod_agencia) DO NOTHING
                            RETURNING cod_colaborador;
                            """, data)
                        
                        result = cur.fetchone()
                        if result:
                            continue
                            print(f"Inserted line: {data['cod_colaborador']}")
                        else:
                            continue
                            print(f"line not inserted: {data['cod_colaborador']}")

        except Exception:
            raise 
        
        print("insertion completed in the colaborador_agencia table")

    def colaboradores_table(self, address_table):
        print("Inserting data into the colaboradores table ")
        try:
            with self.conn.cursor() as cur:
                for chunk in pd.read_csv(address_table, chunksize=self.CHUNKSIZE):
                    chunk.columns = chunk.columns.str.strip()  
                    for index, row in chunk.iterrows():
                        data = {
                            'cod_colaborador': int(row['cod_colaborador']),
                            'primeiro_nome' : row['primeiro_nome'],
                            'ultimo_nome' : row['ultimo_nome'],
                            'email' : row['email'],
                            'cpf' : row['cpf'],
                            'data_nascimento' : row['data_nascimento'],
                            'endereco' : row['endereco'],
                            'cep' : row['cep']
                        }
                        cur.execute(
                            """INSERT INTO public.colaboradores(cod_colaborador, primeiro_nome, ultimo_nome, email, cpf, data_nascimento, endereco, cep) 
                            VALUES (%(cod_colaborador)s, %(primeiro_nome)s, %(ultimo_nome)s, %(email)s, %(cpf)s, %(data_nascimento)s, %(endereco)s, %(cep)s) 
                            ON CONFLICT (cod_colaborador) DO NOTHING
                            RETURNING cod_colaborador;
                            """, data)
                        
                        result = cur.fetchone()
                        if result:
                            continue
                            print(f"Inserted line: {data['cod_colaborador']}")
                        else:
                            continue
                            print(f"line not inserted: {data['cod_colaborador']}")

        except Exception:
            raise 
        
        print("insertion completed in the colaboradores table")

    def contas_table(self, address_table):
        print("Inserting data into the contas table ")
        try:
            with self.conn.cursor() as cur:
                for chunk in pd.read_csv(address_table, chunksize=self.CHUNKSIZE):
                    chunk.columns = chunk.columns.str.strip()  
                    for index, row in chunk.iterrows():
                        data = {
                            'num_conta': int(row['num_conta']),
                            'cod_cliente' : int(row['cod_cliente']),
                            'cod_agencia' : int(row['cod_agencia']),
                            'cod_colaborador' : int(row['cod_colaborador']),
                            'tipo_conta' : row['tipo_conta'],
                            'data_abertura' : row['data_abertura'],
                            'saldo_total' : row['saldo_total'],
                            'saldo_disponivel' : row['saldo_disponivel'],
                            'data_ultimo_lancamento' :row['data_ultimo_lancamento']
                        }
                        cur.execute(
                            """INSERT INTO public.contas(num_conta, cod_cliente, cod_agencia, cod_colaborador, tipo_conta, data_abertura, saldo_total, saldo_disponivel, data_ultimo_lancamento) 
                            VALUES (%(num_conta)s, %(cod_cliente)s, %(cod_agencia)s, %(cod_colaborador)s, %(tipo_conta)s, %(data_abertura)s, %(saldo_total)s, %(saldo_disponivel)s, %(data_ultimo_lancamento)s) 
                            ON CONFLICT (num_conta) DO NOTHING
                            RETURNING num_conta;
                            """, data)
                        result = cur.fetchone()
                        if result:
                            continue
                            print(f"Inserted line: {data['num_conta']}")
                        else:
                            continue
                            print(f"line not inserted: {data['num_conta']}")

        except Exception:
            raise 
        
        print("insertion completed in the contas table")

    def propostas_credito_table(self, address_table):
        print("Inserting data into the proposta_credito table ")
        try:
            with self.conn.cursor() as cur:
                for chunk in pd.read_csv(address_table, chunksize=self.CHUNKSIZE):
                    chunk.columns = chunk.columns.str.strip()  
                    for index, row in chunk.iterrows():
                        data = {
                            'cod_proposta': int(row['cod_proposta']),
                            'cod_cliente' : int(row['cod_cliente']),
                            'cod_colaborador' : int(row['cod_colaborador']),
                            'data_entrada_proposta' : row['data_entrada_proposta'],
                            'taxa_juros_mensal' : row['taxa_juros_mensal'],
                            'valor_proposta' : row['valor_proposta'],
                            'valor_financiamento' : row['valor_financiamento'],
                            'valor_entrada' : row['valor_entrada'],
                            'valor_prestacao' :row['valor_prestacao'],
                            'quantidade_parcelas' : int(row['quantidade_parcelas']),
                            'carencia': int(row['carencia']),
                            'status_proposta' : row['status_proposta']
                        }
                        cur.execute(
                            """INSERT INTO public.propostas_credito(cod_proposta, cod_cliente, cod_colaborador, data_entrada_proposta, taxa_juros_mensal, valor_proposta, valor_financiamento, valor_entrada, valor_prestacao, quantidade_parcelas, carencia, status_proposta) 
                            VALUES (%(cod_proposta)s, %(cod_cliente)s, %(cod_colaborador)s, %(data_entrada_proposta)s, %(taxa_juros_mensal)s, %(valor_proposta)s, %(valor_financiamento)s, %(valor_entrada)s, %(valor_prestacao)s, %(quantidade_parcelas)s, %(carencia)s, %(status_proposta)s) 
                            ON CONFLICT (cod_proposta) DO NOTHING
                            RETURNING cod_proposta;
                            """, data)
                        result = cur.fetchone()
                        if result:
                            continue
                            print(f"Inserted line: {data['cod_proposta']}")
                        else:
                            continue
                            print(f"line not inserted: {data['cod_proposta']}")

        except Exception:
            raise 
        
        print("insertion completed in the propostas_credito table")
