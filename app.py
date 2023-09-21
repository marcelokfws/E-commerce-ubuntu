from pypdf import PdfReader

arquivo_pdf = 'CONTRATO.pdf'
with open(arquivo_pdf, 'rb') as ar:
    ler = PdfReader(ar)
    num_pag = len(ler.pages)
    for num in range(num_pag):
        pag = ler.pages[num]
        texto = pag.extract_text() #.replace('Página', '').replace('de 6', '')
        print(texto)

arquivo_txt = open('CONTRATO.txt', 'w', encoding='utf-8')
num_pag = len(ler.pages)
for num in range(num_pag):
    pag = ler.pages[num]
    texto = pag.extract_text()
    arquivo_txt.write(texto)

        
     
       

        


       
       
        
    
