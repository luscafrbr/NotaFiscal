"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal
class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor =+ item._valorItem
        self.valorNota=valor

    def getseq(self):
        return self._itens
    
    def setseq(self, item):
        return self._itens
    
    def imprimirNotaFiscal(self):       
        print("""
---------------------------------------------------------------------------
NOTA FISCAL{}{}{}{}{}/{}/{}
Cliente: {} Nome: {}
CPF: {}
----------------------------------------------------------------------------
ITENS
----------------------------------------------------------------------------
Seq    Descrição {}{} QTD {} Valor Unitário {} Preço
---    --------- {}{} ---- {}--------------{}{} ---------
        """.format('\t', '\t','\t', '\t',self._data.day, self._data.month, self._data.year, self._cliente._id, self._cliente._nome, self._cliente._cnpjcpf, '\t','\t', '\t', '\t', '\t', '\t', '\t', '\t', '\t'))
        for x in self._itens:
            print("{:0>3}    {:30}{}{:12}{:15.2f}".format(x.getSequencial(), x.getDescricao(), x.getQuantidade(), x.getUnitario(), x.getValorItem()))
        
        print("____________________________________________________________________________")
        print("Valor total = ", self.valorNota)