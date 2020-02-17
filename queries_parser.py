from re import findall, M, I
from os import getcwd

def parse_queries(file_name):
    """
        Irá parsear um arquivo .sql com as queries necessárias
        e irá retornar um dicionário contendo o nome da query no arquivo, como chave
        e a query especificamente como valor.
    """
    pattern = r"--[ ]?name:[ ]?([a-z\-_]*)\n([a-zA-Z _.,0-9\()\n'-:@=\"?>=<\[\]\$%]*);"
    queries = {}

    with open(file_name, 'r') as f:
        file_queries = f.read()
        matches = findall(pattern, file_queries, M | I)
        for query in matches:
            query_name, sql = query
            queries[query_name] = sql.replace('\n', ' ')

    return queries


if __name__ == "__main__":
    queries = parse_queries(f'{getcwd()}/queries/test.sql')
    print(queries)
