import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from datetime import datetime
import os

# Criar pasta de relatórios
if not os.path.exists("relatorios"):
    os.mkdir("relatorios")

# Ler o Excel
df = pd.read_excel("estoque.xlsx")

# Filtrar produtos em falta
faltando = df[df["Quantidade"] < df["Estoque_Minimo"]]

# Dados do PDF
data_atual = datetime.now().strftime("%d/%m/%Y")
nome_arquivo = f"relatorios/relatorio_estoque_{datetime.now().strftime('%Y-%m-%d')}.pdf"

pdf = canvas.Canvas(nome_arquivo, pagesize=A4)
largura, altura = A4

# Título
pdf.setFont("Helvetica-Bold", 18)
pdf.drawString(2*cm, altura - 2*cm, "RELATÓRIO DE ESTOQUE EM FALTA")

pdf.setFont("Helvetica", 12)
pdf.drawString(2*cm, altura - 3*cm, f"Data: {data_atual} ")

# Cabeçalho da tabela
y = altura - 5*cm
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(2*cm, y, "Produto")
pdf.drawString(9*cm, y, "Quantidade")
pdf.drawString(14*cm, y, "Mínimo")

y -= 1*cm
pdf.setFont("Helvetica", 12)

# Conteúdo
for _, linha in faltando.iterrows():
    pdf.drawString(2*cm, y, str(linha["Produto"]))
    pdf.drawString(9*cm, y, str(linha["Quantidade"]))
    pdf.drawString(14*cm, y, str(linha["Estoque_Minimo"]))
    y -= 0.8*cm

    if y < 2*cm:
        pdf.showPage()
        y = altura - 2*cm

pdf.save()

print(f"\nPDF gerado com sucesso: {nome_arquivo}")

# Print no terminal (opcional)
print("\nRELATÓRIO DE ESTOQUE EM FALTA")
print("-" * 30)

for _, linha in faltando.iterrows():
    print(
        f"Produto: {linha['Produto']} | "
        f"Quantidade: {linha['Quantidade']} | "
        f"Mínimo: {linha['Estoque_Minimo']}"
    )

#SISTEMA CRIADO COM AJUDA DE IA , PARA AFINS DE ESTUDO E APRENDIZADO 